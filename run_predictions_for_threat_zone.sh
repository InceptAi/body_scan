if [ "$#" -ne 2 ]; then
    echo "usage: $0 threat_zone positive(0/1)"
    exit
fi
THREAT_ZONE=$1
POSITIVE=$2
ZONE_GREP="Zone${THREAT_ZONE},${POSITIVE}"
MAX_SUBJECTS=100
cat /home/vivek/Work/kaggle/dhs/data/stage1_labels.csv  | grep $ZONE_GREP | cut -d "_" -f 1 | head -n $MAX_SUBJECTS > /tmp/zone_${THREAT_ZONE}_${POSITIVE}
python3 predict_batch.py -t $THREAT_ZONE -f /tmp/zone_${THREAT_ZONE}_${POSITIVE} > output_predictions_${THREAT_ZONE}_${POSITIVE}
#POSITIVE_SUBJECTS=`cat /home/vivek/Work/kaggle/dhs/data/stage1_labels.csv  | grep $ZONE_GREP | cut -d "_" -f 1`
#echo $ZONE_GREP
#rm -f output_predictions_${THREAT_ZONE}_${POSITIVE}
#touch output_predictions_${THREAT_ZONE}_${POSITIVE}
#for SUBJECT_ID in $POSITIVE_SUBJECTS
#do
#    echo "SUBJECT: $SUBJECT_ID"
#    echo "SUBJECT: $SUBJECT_ID" >> output_predictions_${THREAT_ZONE}_${POSITIVE}
#    python3 predict.py -t $THREAT_ZONE -i $SUBJECT_ID >> output_predictions_${THREAT_ZONE}_${POSITIVE}
#done
