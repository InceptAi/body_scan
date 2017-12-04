from myimports import *
#----------------------------------------------------------------------------------------
# def get_subject_labels(infile, subject_id): lists threat probabilities by zone
#
# infile:                          labels csv file
#
# subject_id:                      the individual you want the threat zone labels for
#
# returns:                         a df with the list of zones and contraband (0 or 1)
#
#---------------------------------------------------------------------------------------

def get_subject_labels(infile, subject_id):

    # read labels into a dataframe
    df = pd.read_csv(infile)

    # Separate the zone and subject id into a df
    df['Subject'], df['Zone'] = df['Id'].str.split('_',1).str
    df = df[['Subject', 'Zone', 'Probability']]
    threat_list = df.loc[df['Subject'] == subject_id]
    
    return threat_list
    

    
# unit test ----------------------------------------------------------------------
#print(get_subject_labels(THREAT_LABELS, '00360f79fd6e02781457eda48f85da90'))


#------------------------------------------------------------------------------------------------
# get_subject_zone_label(zone_num, df):    gets a label for a given subject and zone
#
# zone_num:                                a 0 based threat zone index
#
# df:                                      a df like that returned from get_subject_labels(...)
#
# returns:                                 [0,1] if contraband is present, [1,0] if it isnt
#
#-----------------------------------------------------------------------------------------------

def get_subject_zone_label(zone_num, df):
    
    # Dict to convert a 0 based threat zone index to the text we need to look up the label
    zone_index = {0: 'Zone1', 1: 'Zone2', 2: 'Zone3', 3: 'Zone4', 4: 'Zone5', 5: 'Zone6', 
                  6: 'Zone7', 7: 'Zone8', 8: 'Zone9', 9: 'Zone10', 10: 'Zone11', 11: 'Zone12', 
                  12: 'Zone13', 13: 'Zone14', 14: 'Zone15', 15: 'Zone16',
                  16: 'Zone17'
                 }
    # get the text key from the dictionary
    key = zone_index.get(zone_num)
    
    # select the probability value and make the label
    if df.loc[df['Zone'] == key]['Probability'].values[0] == 1:
        # threat present
        return [0,1]
    else:
        #no threat present
        return [1,0]

    
# unit test --------------------------------
print(get_subject_labels(THREAT_LABELS, '00360f79fd6e02781457eda48f85da90'))
label = get_subject_zone_label(5, get_subject_labels(THREAT_LABELS, '00360f79fd6e02781457eda48f85da90'))
print (np.array(label))
