from myimports import *
from generate_input_pipeline import input_pipeline
def test_input(prediction_input_list):
    val_features = []
    val_labels = []
    # read in the validation test set
    for j, test_f_in in enumerate(prediction_input_list):
        if j == 0:
            val_features, val_labels = input_pipeline(test_f_in, PREDICTION_DATA_FOLDER)
        else:
            tmp_feature_batch, tmp_label_batch = input_pipeline(test_f_in,
                                                                PREDICTION_DATA_FOLDER)
            val_features = np.concatenate((tmp_feature_batch, val_features), axis=0)
            val_labels = np.concatenate((tmp_label_batch, val_labels), axis=0)

    print (' -> features shape {}:{}:{}'.format(len(val_features),
                                                len(val_features[0]),
                                                len(val_features[0][0])))
    print (' -> labels shape   {}:{}'.format(len(val_labels), len(val_labels[0])))
    val_features = val_features.reshape(-1, IMAGE_DIM, IMAGE_DIM, 1)
    print (' -> features shape {}:{}:{}'.format(len(val_features),
                                                len(val_features[0]),
                                                len(val_features[0][0])))
    print (' -> labels shape   {}:{}'.format(len(val_labels), len(val_labels[0])))
    

test_input(['preprocessed_TSA_scans-tz10-250-250-b1.npy'])
