from myimports import *
from split_training_testing import *
#---------------------------------------------------------------------------------------
# input_pipeline(filename, path): prepares a batch of features and labels for training
#
# parameters:      filename - the file to be batched into the model
#                  path - the folder where filename resides
#
# returns:         feature_batch - a batch of features to train or test on
#                  label_batch - a batch of labels related to the feature_batch
#
#---------------------------------------------------------------------------------------
def input_pipeline(filename, path):

    preprocessed_tz_scans = []
    feature_batch = []
    label_batch = []
    
    #Load a batch of preprocessed tz scans
    preprocessed_tz_scans = np.load(os.path.join(path, filename))
        
    #Shuffle to randomize for input into the model
    np.random.shuffle(preprocessed_tz_scans)
    
    # separate features and labels
    for example_list in preprocessed_tz_scans:
        for example in example_list:
            feature_batch.append(example[0])
            label_batch.append(example[1])
    
    feature_batch = np.asarray(feature_batch, dtype=np.float32)
    label_batch = np.asarray(label_batch, dtype=np.float32)
    
    return feature_batch, label_batch

# unit test ------------------------------------------------------------------------
#train_set, test_set = get_train_test_file_list()
train_set=['preprocessed_TSA_scans-tz10-250-250-b1.npy']
print ('Train Set -----------------------------')
for f_in in train_set:
    print("In train set:{0}".format(f_in))
    feature_batch, label_batch = input_pipeline(f_in, PREDICTION_DATA_FOLDER)
    print (' -> features shape {}:{}:{}'.format(len(feature_batch), 
                                                len(feature_batch[0]), 
                                                len(feature_batch[0][0])))
    print (' -> labels shape   {}:{}'.format(len(label_batch), len(label_batch[0])))

'''    
print ('Test Set -----------------------------')
for f_in in test_set:
    print("In test set:{0}".format(f_in))
    feature_batch, label_batch = input_pipeline(f_in, PREPROCESSED_DATA_FOLDER)
    print (' -> features shape {}:{}:{}'.format(len(feature_batch), 
                                                len(feature_batch[0]), 
                                                len(feature_batch[0][0])))
    print (' -> labels shape   {}:{}'.format(len(label_batch), len(label_batch[0])))
'''
#feature_batch, label_batch = input_pipeline(filename="preprocessed_TSA_scans-tz17-250-250-b10.npy", path=PREPROCESSED_DATA_FOLDER)
#print (' -> features shape {}:{}:{}'.format(len(feature_batch), 
#                        len(feature_batch[0]), 
#                        len(feature_batch[0][0])))
#print (' -> labels shape   {}:{}'.format(len(label_batch), len(label_batch[0])))
#print (' -> labels {}'.format(label_batch))
#print (' -> labels {}'.format(feature_batch[0]))
