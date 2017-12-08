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

def predict_threat_probability(input_aps_file, threat_zone=1):
    model_name = ('tsa-{}-lr-{}-{}-{}-tz-{}'.format('alexnet-v0.1', LEARNING_RATE, IMAGE_DIM,
                                                    IMAGE_DIM, threat_zone ))
    val_features = []
    val_labels = []
    
    # instantiate model
    model = alexnet(IMAGE_DIM, IMAGE_DIM, LEARNING_RATE, model_name)
    current_model_path = MODEL_PATH + model_name + ".tflearn"
    print ('current path {0}'.format(current_model_path))
    model.load(current_model_path)
    
    # get train and test batches
    val_features, val_lables = input_pipeline(input_aps_file, PREPROCESSED_DATA_FOLDER)
    
    
    '''
    # read in the validation test set
    for j, test_f_in in enumerate(test_set):
        if j == 0:
            val_features, val_labels = input_pipeline(test_f_in, PREPROCESSED_DATA_FOLDER)
        else:
            tmp_feature_batch, tmp_label_batch = input_pipeline(test_f_in, 
                                                                PREPROCESSED_DATA_FOLDER)
            val_features = np.concatenate((tmp_feature_batch, val_features), axis=0)
            val_labels = np.concatenate((tmp_label_batch, val_labels), axis=0)
    '''
    val_features = val_features.reshape(-1, IMAGE_DIM, IMAGE_DIM, 1)
    print ("input features shape : {}".format(val_features.shape))
    prediction = model.predict(val_features)
    print ("prediction output shape : {}".format(prediction.shape))
    #print ("File {0}".format(input_aps_file))
    #print ("prediction {0}".format(prediction))

# unit test -----------------------------------
op = OptionParser()
op.add_option("-t", "--tzone", dest="threat_zone", help="Threat Zone", default=None)
op.add_option("-i", "--input", dest="input_aps_file", help="Input 250x250 file", default=None)
(opts, args) = op.parse_args()

if not opts.threat_zone:
    op.print_help()
    op.error("Threat zone is needed")

if not opts.input_aps_file:
    op.print_help()
    op.error("Input aps file is needed")

predict_threat_probability(input_aps_file=opts.input_aps_file, threat_zone=opts.threat_zone)
