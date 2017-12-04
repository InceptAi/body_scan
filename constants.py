# constants


#---------------------------------------------------------------------------------------
# Constants
#
# INPUT_FOLDER:                 The folder that contains the source data
#
# PREPROCESSED_DATA_FOLDER:     The folder that contains preprocessed .npy files 
# 
# STAGE1_LABELS:                The CSV file containing the labels by subject
#
# THREAT_ZONE:                  Threat Zone to train on (actual number not 0 based)
#
# BATCH_SIZE:                   Number of Subjects per batch
#
# EXAMPLES_PER_SUBJECT          Number of examples generated per subject
#
# FILE_LIST:                    A list of the preprocessed .npy files to batch
# 
# TRAIN_TEST_SPLIT_RATIO:       Ratio to split the FILE_LIST between train and test
#
# TRAIN_SET_FILE_LIST:          The list of .npy files to be used for training
#
# TEST_SET_FILE_LIST:           The list of .npy files to be used for testing
#
# IMAGE_DIM:                    The height and width of the images in pixels
#
# LEARNING_RATE                 Learning rate for the neural network
#
# N_TRAIN_STEPS                 The number of train steps (epochs) to run
#
# TRAIN_PATH                    Place to store the tensorboard logs
#
# MODEL_PATH                    Path where model files are stored
#
# MODEL_NAME                    Name of the model files
#
#----------------------------------------------------------------------------------------
INPUT_FOLDER = '/home/vivek/Work/kaggle/dhs/data/stage1'
PREPROCESSED_DATA_FOLDER = '/home/vivek/Work/kaggle/dhs/preprocessed/'
STAGE1_LABELS = '/home/vivek/Work/kaggle/dhs/data/stage1_labels.csv'
#THREAT_ZONE = 1
BATCH_SIZE = 16
EXAMPLES_PER_SUBJECT = 182

FILE_LIST = []
TRAIN_TEST_SPLIT_RATIO = 0.2
#TRAIN_SET_FILE_LIST = []
#TEST_SET_FILE_LIST = []

IMAGE_DIM = 250
LEARNING_RATE = 1e-3
N_TRAIN_STEPS = 1
TRAIN_PATH = '/home/vivek/Work/kaggle/dhs/train/'
MODEL_PATH = '/home/vivek/Work/kaggle/dhs/model/'
#MODEL_NAME = ('tsa-{}-lr-{}-{}-{}-tz-{}'.format('alexnet-v0.1', LEARNING_RATE, IMAGE_DIM, 
#                                                IMAGE_DIM, THREAT_ZONE )) 
COLORMAP = 'pink'
APS_FILE_NAME = '/home/vivek/Work/kaggle/dhs/data/stage1/00360f79fd6e02781457eda48f85da90.aps'
BODY_ZONES = '/home/vivek/Work/kaggle/dhs/data/body_zones.png'
THREAT_LABELS = '/home/vivek/Work/kaggle/dhs/data/stage1_labels.csv'
