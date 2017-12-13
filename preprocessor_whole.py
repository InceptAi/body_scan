from myimports import *
from tsahelper_whole import *
MAX_NEGATIVE_SAMPLES = SAMPLES_PER_BATCH * 10
#---------------------------------------------------------------------------------------
# preprocess_tsa_data(): preprocesses the tsa datasets
#
# parameters:      none
#
# returns:         none
#---------------------------------------------------------------------------------------
def check_if_positive_sample(label):
    return np.array_equal(label, [0, 1])

def preprocess_tsa_data():
    
    # OPTION 1: get a list of all subjects for which there are labels
    df = pd.read_csv(STAGE1_LABELS)
    df['Subject'], df['Zone'] = df['Id'].str.split('_',1).str
    SUBJECT_LIST = df['Subject'].unique()

    # OPTION 2: get a list of all subjects for whom there is data
    #SUBJECT_LIST = [os.path.splitext(subject)[0] for subject in os.listdir(INPUT_FOLDER)]
    
    # OPTION 3: get a list of subjects for small bore test purposes
    #SUBJECT_LIST = ['00360f79fd6e02781457eda48f85da90','0043db5e8c819bffc15261b1f1ac5e42',
    #                '0050492f92e22eed3474ae3a6fc907fa','006ec59fa59dd80a64c85347eef810c7',
    #                '0097503ee9fa0606559c56458b281a08','011516ab0eca7cad7f5257672ddde70e']
    
    # intialize tracking and saving items
    batch_num = 1
    threat_zone_positives = []
    threat_zone_negatives = []
    start_time = timer()
    num_positives = 0
    num_negatives = 0
    
    for subject in SUBJECT_LIST:

        # read in the images
        print('--------------------------------------------------------------')
        print('t+> {:5.3f} |Reading images for subject #: {}'.format(timer()-start_time, 
                                                                     subject))
        print('pos samples:{}'.format(len(threat_zone_positives)))
        print('neg samples:{}'.format(len(threat_zone_negatives)))
        print('--------------------------------------------------------------')
        images = read_data(INPUT_FOLDER + '/' + subject + '.aps')

        # transpose so that the slice is the first dimension shape(16, 620, 512)
        images = images.transpose()

        # for each threat zone, loop through each image, mask off the zone and then crop it
        for tz_num, threat_zone_x_crop_dims in enumerate(zip(tsa.zone_slice_list, 
                                                             tsa.zone_crop_list)):

            threat_zone = threat_zone_x_crop_dims[0]
            crop_dims = threat_zone_x_crop_dims[1]

            # get label
            label = np.array(tsa.get_subject_zone_label(tz_num, 
                             tsa.get_subject_labels(STAGE1_LABELS, subject)))

            if check_if_positive_sample(label):
                num_positives = num_positives + 1
            else:
                num_negatives = num_negatives + 1

            for img_num, img in enumerate(images):

                #print('Threat Zone:Image -> {}:{}'.format(tz_num, img_num))
                #print('Threat Zone Label -> {}'.format(label))
                
                if threat_zone[img_num] is not None:

                    # correct the orientation of the image
                    #print('-> reorienting base image') 
                    base_img = np.flipud(img)
                    #print('-> shape {}|mean={}'.format(base_img.shape, 
                    #                                   base_img.mean()))

                    # convert to grayscale
                    #print('-> converting to grayscale')
                    rescaled_img = tsa.convert_to_grayscale(base_img)
                    #print('-> shape {}|mean={}'.format(rescaled_img.shape, 
                    #                                   rescaled_img.mean()))

                    # spread the spectrum to improve contrast
                    #print('-> spreading spectrum')
                    high_contrast_img = tsa.spread_spectrum(rescaled_img)
                    #print('-> shape {}|mean={}'.format(high_contrast_img.shape,
                    #                                   high_contrast_img.mean()))

                    # get the masked image
                    #print('-> masking image')
                    masked_img = tsa.roi(high_contrast_img, threat_zone[img_num])
                    #print('-> shape {}|mean={}'.format(masked_img.shape, 
                    #                                   masked_img.mean()))

                    # crop the image
                    #print('-> cropping image')
                    cropped_img = tsa.crop(masked_img, crop_dims[img_num])
                    #print('-> shape {}|mean={}'.format(cropped_img.shape, 
                    #                                  cropped_img.mean()))

                    # normalize the image
                    #print('-> normalizing image')
                    normalized_img = tsa.normalize(cropped_img)
                    #print('-> shape {}|mean={}'.format(normalized_img.shape, 
                    #                                   normalized_img.mean()))

                    # zero center the image
                    #print('-> zero centering')
                    zero_centered_img = tsa.zero_center(normalized_img)
                    #print('-> shape {}|mean={}'.format(zero_centered_img.shape, 
                    #                                   zero_centered_img.mean()))

                    # append the features and labels to this threat zone's example array
                    #threat_zone_examples.append([[tz_num], zero_centered_img, label])
                    if check_if_positive_sample(label):
                        #print ('-> appending example to pos threat zone {}'.format(tz_num))
                        threat_zone_positives.append([[tz_num], zero_centered_img, label])
                    else:
                        if len(threat_zone_negatives) < MAX_NEGATIVE_SAMPLES:
                            #print ('-> appending example to neg threat zone,count {},{}'.format(tz_num, len(threat_zone_negatives)))
                            threat_zone_negatives.append([[tz_num], zero_centered_img, label])
                        #else:
                        #    print ('-> Dropping neg sample'.format(tz_num, len(threat_zone_negatives)))

                #else:
                #    print('-> No view of tz:{} in img:{}. Skipping to next...'.format( 
                #                tz_num, img_num))
                #print('------------------------------------------------')

        # each subject gets EXAMPLES_PER_SUBJECT number of examples (182 to be exact, 
        # so this section just writes out the the data once there is a full minibatch 
        # complete.
        #if ((len(threat_zone_examples) % (BATCH_SIZE/2 * EXAMPLES_PER_SUBJECT)) == 0):
        if len(threat_zone_positives) > (SAMPLES_PER_BATCH/2):
            print ('-> shape {:d}:{:d}:{:d}:{:d}:{:d}:{:d}'.format(
                                                    len(threat_zone_positives),
                                                    len(threat_zone_positives[0]),
                                                    len(threat_zone_positives[0][0]),
                                                    len(threat_zone_positives[0][1][0]),
                                                    len(threat_zone_positives[0][1][1]),
                                                    len(threat_zone_positives[0][2])))
 
            save_data(batch_num, threat_zone_positives, threat_zone_negatives)
            #reset for next batch 
            del threat_zone_positives
            del threat_zone_negatives
            threat_zone_positives = []
            threat_zone_negatives = []
            batch_num += 1
    
    # we may run out of subjects before we finish a batch, so we write out 
    # the last batch stub
    if (len(threat_zone_positives) > 0):
        save_data(batch_num, threat_zone_positives, threat_zone_negatives)

# unit test ---------------------------------------

def save_data(batch_num, threat_zone_positives, threat_zone_negatives):
   for tz_num, tz in enumerate(tsa.zone_slice_list):
        tz_examples_to_save = []
        # write out the batch and reset
        print(' -> writing: ' + PREPROCESSED_DATA_FOLDER + 
                                    'preprocessed_TSA_scans-tz{}-{}-{}-b{}.npy'.format( 
                                    tz_num+1,
                                    len(threat_zone_positives[0][1][0]),
                                    len(threat_zone_positives[0][1][1]), 
                                    batch_num))

        # get this tz's examples
        # get +ves
        tz_examples_positives = [example for example in threat_zone_positives if example[0] == [tz_num]]
        # drop unused columns
        tz_examples_to_save.append([[features_label[1], features_label[2]] 
                                    for features_label in tz_examples_positives])

        # get -ves, only max len(threat_zone_positives)
        tz_examples_negatives = [example for example in threat_zone_negatives if example[0] == [tz_num]]
        max_negatives = len(tz_examples_positives) * 2
        if len(tz_examples_negatives) > max_negatives:
            np.random.shuffle(tz_examples_negatives)
            tz_examples_negatives = tz_examples_negatives[:max_negatives]
        
        # drop unused columns
        tz_examples_to_save.append([[features_label[1], features_label[2]] 
                        for features_label in tz_examples_negatives])

        print ('-> In save data, shape of positives - {}'.format(len(tz_examples_positives)))
        print ('-> In save data, shape of negatives - {}'.format(len(tz_examples_negatives)))
        print ('-> In save data, pos shape {:d}:{:d}:{:d}:{:d}:{:d}:{:d}'.format(
                                len(threat_zone_positives),
                                len(threat_zone_positives[0]),
                                len(threat_zone_positives[0][0]),
                                len(threat_zone_positives[0][1][0]),
                                len(threat_zone_positives[0][1][1]),
                                len(threat_zone_positives[0][2])))
        print ('-> In save data, neg shape {:d}:{:d}:{:d}:{:d}:{:d}:{:d}'.format(
                                len(threat_zone_negatives),
                                len(threat_zone_negatives[0]),
                                len(threat_zone_negatives[0][0]),
                                len(threat_zone_negatives[0][1][0]),
                                len(threat_zone_negatives[0][1][1]),
                                len(threat_zone_negatives[0][2])))

 
        # save batch.  Note that the trainer looks for tz{} where {} is a 
        # tz_num 1 based in the minibatch file to select which batches to 
        # use for training a given threat zone
        np.save(PREPROCESSED_DATA_FOLDER + 
                            'preprocessed_TSA_scans-tz{}-{}-{}-b{}.npy'.format(tz_num+1, 
                            len(threat_zone_positives[0][1][0]),
                            len(threat_zone_positives[0][1][1]), 
                            batch_num), 
                            tz_examples_to_save)
        del tz_examples_to_save

preprocess_tsa_data()
