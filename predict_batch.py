from myimports import *
from generate_input_pipeline import *
from split_training_testing import *
from model import *
from shuffle import *
from optparse import OptionParser
from preprocess_prediction_data import preprocess_prediction_data
#---------------------------------------------------------------------------------------
# train_conv_net(): runs the train op
#
# parameters:      none
#
# returns:         none
#
#-------------------------------------------------------------------------------------

def setup_model_and_process_input(threat_zone, input_file=None, input_subject=None):
    model_name = ('tsa-{}-lr-{}-{}-{}-tz-{}'.format('alexnet-v0.1', LEARNING_RATE, IMAGE_DIM,
                                                    IMAGE_DIM, threat_zone ))
    # instantiate model
    model = alexnet(IMAGE_DIM, IMAGE_DIM, LEARNING_RATE, model_name)
    current_model_path = MODEL_PATH + model_name + ".tflearn"
    #print ('current path {0}'.format(current_model_path))
    model.load(current_model_path)

    #if input_file is not none, read it else pass the input subject
    if input_file: 
        with open(input_file) as f:
            for line in f:
                line = line.rstrip('\n')
                predict_threat_probability(input_subject_id=line, threat_zone=threat_zone, model=model)
    else:
        predict_threat_probability(input_subject_id=line, threat_zone=threat_zone, model=model)
             

def predict_threat_probability(input_subject_id, threat_zone, model):
    print('predict for zone:{}, subject:{}'.format(threat_zone, input_subject_id)) 
    val_features = []
    val_labels = []
    prediction_input_list = []
    #preprocess
    preprocess_prediction_data(input_subject_id)   

    if os.listdir(PREDICTION_DATA_FOLDER) == []:
        print ('No preprocessed data available.  Skipping preprocessed data setup..')
        return
    else:
        prediction_input_list = [f for f in os.listdir(PREDICTION_DATA_FOLDER)
                     if re.search(re.compile('-tz' + str(threat_zone) + '-'), f)]
 
    # read in the validation test set
    for j, test_f_in in enumerate(prediction_input_list):
        if j == 0:
            val_features, val_labels = input_pipeline(test_f_in, PREDICTION_DATA_FOLDER)
        else:
            tmp_feature_batch, tmp_label_batch = input_pipeline(test_f_in, 
                                                                PREDICTION_DATA_FOLDER)
            val_features = np.concatenate((tmp_feature_batch, val_features), axis=0)
            val_labels = np.concatenate((tmp_label_batch, val_labels), axis=0)
    
    val_features = val_features.reshape(-1, IMAGE_DIM, IMAGE_DIM, 1)
    #print ("input features shape : {}".format(val_features.shape))
    prediction = model.predict(val_features)
    #print ("prediction output shape : {}".format(prediction.shape))
    #print ("File {0}".format(input_aps_file))
    print ("prediction {0}".format(prediction))

# unit test -----------------------------------
op = OptionParser()
op.add_option("-t", "--tzone", dest="threat_zone", help="Threat Zone", default=None)
op.add_option("-i", "--input", dest="input_subject_id", help="Input Subject Id", default=None)
op.add_option("-f", "--input_file", dest="input_subject_id_file", help="Input Subject Id File", default=None)
(opts, args) = op.parse_args()

if not opts.threat_zone:
    op.print_help()
    op.error("Threat zone is needed")

if not opts.input_subject_id and not opts.input_subject_id_file:
    op.print_help()
    op.error("Input subject id or file is needed")

tf.logging.set_verbosity(tf.logging.ERROR)
setup_model_and_process_input(threat_zone=opts.threat_zone, input_file=opts.input_subject_id_file, input_subject=opts.input_subject_id)
