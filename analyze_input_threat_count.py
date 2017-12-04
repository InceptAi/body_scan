from myimports import *

#----------------------------------------------------------------------------------------
# get_hit_rate_stats(infile):  gets the threat probabilities in a useful form
#
# infile:                      labels csv file
#
# returns:                     a dataframe of the summary hit probabilities
#
#----------------------------------------------------------------------------------------

def get_hit_rate_stats(infile):
    # pull the labels for a given patient
    df = pd.read_csv(infile)
    # Separate the zone and patient id into a df
    df['Subject'], df['Zone'] = df['Id'].str.split('_',1).str
    df = df[['Subject', 'Zone', 'Probability']]

    # make a df of the sums and counts by zone and calculate hit rate per zone, then sort high to low
    df_summary = df.groupby('Zone')['Probability'].agg(['sum','count'])
    df_summary['Zone'] = df_summary.index
    df_summary['pct'] = df_summary['sum'] / df_summary['count']
    df_summary.sort_values('pct', axis=0, ascending= False, inplace=True)
    return df_summary

# unit test -----------------------
#df = get_hit_rate_stats(THREAT_LABELS)
#df.head()



#------------------------------------------------------------------------------------------
# chart_hit_rate_stats(df_summary): charts threat probabilities in desc order by zone
#
# df_summary:                 a dataframe like that returned from get_hit_rate_stats(...)
#
#-------------------------------------------------------------------------------------------

def chart_hit_rate_stats(df_summary):
    fig, ax = plt.subplots(figsize=(15,5))
    sns.barplot(ax=ax, x=df_summary['Zone'], y=df_summary['pct']*100)
    #plt.show()

# unit test ------------------
#chart_hit_rate_stats(df)


#------------------------------------------------------------------------------------------
# print_hit_rate_stats(df_summary): lists threat probabilities by zone
#
# df_summary:               a dataframe like that returned from get_hit_rate_stats(...)
#
#------------------------------------------------------------------------------------------

def print_hit_rate_stats(df_summary):
    # print the table of values readbly
    print ('{:6s}   {:>4s}   {:6s}'.format('Zone', 'Hits', 'Pct %'))
    print ('------   ----- ----------')
    for zone in df_summary.iterrows():
        print ('{:6s}   {:>4d}   {:>6.3f}%'.format(zone[0], np.int16(zone[1]['sum']), zone[1]['pct']*100))
    print ('------   ----- ----------')
    print ('{:6s}   {:>4d}   {:6.3f}%'.format('Total ', np.int16(df_summary['sum'].sum(axis=0)), 
                                             ( df_summary['sum'].sum(axis=0) / df_summary['count'].sum(axis=0))*100))

# unit test -----------------------
#print_hit_rate_stats(df)


#testing get_hit_rate_stats
print (THREAT_LABELS) 
df = get_hit_rate_stats(THREAT_LABELS)
#print (df)
print_hit_rate_stats(df)
#df.head()
#chart_hit_rate_stats(df)

