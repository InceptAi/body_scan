from myimports import *
from generate_input_pipeline import *
from split_training_testing import *
from model import *
from shuffle import *
from optparse import OptionParser
#---------------------------------------------------------------------------------------
# train_conv_net(): runs the train op
#
# parameters:      none
#
# returns:         none
#
#-------------------------------------------------------------------------------------
def refresh_tensorboard_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        os.makedirs(folder_name)

def train_conv_net(threat_zone=1):
    model_name = ('tsa-{}-lr-{}-{}-{}-tz-{}'.format('alexnet-v0.1', LEARNING_RATE, IMAGE_DIM,
                                                    IMAGE_DIM, threat_zone ))
    val_features = []
    val_labels = []
   
    refresh_tensorboard_folder(TRAIN_PATH + "/" + model_name) 
    # get train and test batches
    train_set, test_set = get_train_test_file_list(threat_zone)
    
    # instantiate model
    model = alexnet(IMAGE_DIM, IMAGE_DIM, LEARNING_RATE, model_name)
    
    # read in the validation test set
    for j, test_f_in in enumerate(test_set):
        if j == 0:
            val_features, val_labels = input_pipeline(test_f_in, PREPROCESSED_DATA_FOLDER)
        else:
            tmp_feature_batch, tmp_label_batch = input_pipeline(test_f_in, 
                                                                PREPROCESSED_DATA_FOLDER)
            val_features = np.concatenate((tmp_feature_batch, val_features), axis=0)
            val_labels = np.concatenate((tmp_label_batch, val_labels), axis=0)

    val_features = val_features.reshape(-1, IMAGE_DIM, IMAGE_DIM, 1)

    # start training process
    for i in range(N_TRAIN_STEPS):

        # shuffle the train set files before each step
        np.random.shuffle(train_set)
        #train_set = shuffle_train_set(train_set)
        
        # run through every batch in the training set
        for f_in in train_set:
            
            # read in a batch of features and labels for training
            feature_batch, label_batch = input_pipeline(f_in, PREPROCESSED_DATA_FOLDER)
            # make sure to feed equal # of +/- samples
            #unique, counts = numpy.unique(a, return_counts=True)
            feature_batch = feature_batch.reshape(-1, IMAGE_DIM, IMAGE_DIM, 1)
            #print ('Feature Batch Shape ->', feature_batch.shape)                
                
            # run the fit operation
            model.fit({'features': feature_batch}, {'labels': label_batch}, n_epoch=100, 
                      validation_set=({'features': val_features}, {'labels': val_labels}), 
                      shuffle=True, snapshot_step=None, show_metric=True, snapshot_epoch=False, 
                      run_id=model_name)
            
    model.save(MODEL_PATH + "/" + model_name + ".tflearn")

# unit test -----------------------------------
op = OptionParser()
op.add_option("-t", "--tzone", dest="threat_zone", help="Threat Zone", default=None)
(opts, args) = op.parse_args()

if not opts.threat_zone:
    op.print_help()
    op.error("Threat zone is needed")

train_conv_net(opts.threat_zone)
