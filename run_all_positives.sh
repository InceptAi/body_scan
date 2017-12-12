if [ "$#" -ne 1 ]; then
    echo "usage: $0 threat_zone"
    exit
fi
THREAT_ZONE=$1
ZONE_GREP="Zone${THREAT_ZONE},1"
POSITIVE_SUBJECTS=`cat /home/vivek/Work/kaggle/dhs/data/stage1_labels.csv  | grep $ZONE_GREP | cut -d "_" -f 1`
echo $ZONE_GREP
rm -f output_positives_$THREAT_ZONE
touch output_positives_${THREAT_ZONE}
for SUBJECT_ID in $POSITIVE_SUBJECTS
do
    echo "SUBJECT: $SUBJECT_ID"
    echo "SUBJECT: $SUBJECT_ID" >> output_positives_${THREAT_ZONE}
    python3 predict.py -t $THREAT_ZONE -i $SUBJECT_ID >> output_positives_${THREAT_ZONE}
done
