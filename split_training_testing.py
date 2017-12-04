from myimports import *
from tsahelper import *
#---------------------------------------------------------------------------------------
# get_train_test_file_list(): gets the batch file list, splits between train and test
#
# parameters:      none
#
# returns:         none
#
#-------------------------------------------------------------------------------------

def get_train_test_file_list(threat_zone):
    
    global FILE_LIST
    train_set = []
    test_set = []

    if os.listdir(PREPROCESSED_DATA_FOLDER) == []:
        print ('No preprocessed data available.  Skipping preprocessed data setup..')
    else:
        FILE_LIST = [f for f in os.listdir(PREPROCESSED_DATA_FOLDER) 
                     if re.search(re.compile('-tz' + str(threat_zone) + '-'), f)]
        print('file list:{0}'.format(len(FILE_LIST)))
        if (len(FILE_LIST) == 1):
            train_test_split = 1
        else:    
            train_test_split = len(FILE_LIST) - \
                           max(int(len(FILE_LIST)*TRAIN_TEST_SPLIT_RATIO),1)
        train_set = FILE_LIST[:train_test_split]
        test_set = FILE_LIST[train_test_split:]
        print('Train/Test Split -> {} file(s) of {} used for testing'.format( 
              len(FILE_LIST) - train_test_split, len(FILE_LIST)))
    return train_set, test_set
        
# unit test ----------------------------
#get_train_test_file_list()
