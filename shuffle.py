from myimports import *
#---------------------------------------------------------------------------------------
# shuffle_train_set(): shuffle the list of batch files so that each train step
#                      receives them in a different order since the TRAIN_SET_FILE_LIST
#                      is a global
#
# parameters:      train_set - the file listing to be shuffled
#
# returns:         shuffled list of files
#
#-------------------------------------------------------------------------------------

def shuffle_train_set(train_set):
    print ('before shuffling ->', train_set)
    sorted_file_list = random.shuffle(train_set)
    print ('after shuffling ->', sorted_file_list)
    return sorted_file_list
    
# Unit test ---------------
#print ('Before Shuffling ->', TRAIN_SET_FILE_LIST)
#shuffle_train_set(TRAIN_SET_FILE_LIST)
#print ('After Shuffling ->', TRAIN_SET_FILE_LIST)
