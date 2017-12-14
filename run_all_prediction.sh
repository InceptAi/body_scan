THREAT_ZONES_TO_RUN=`cat /home/vivek/Work/kaggle/dhs/body_scan/models_home`
for CURRENT_THREAT_ZONE in $THREAT_ZONES_TO_RUN
do
    echo "ZONE : $CURRENT_THREAT_ZONE"
    #echo "/home/vivek/Work/kaggle/dhs/body_scan/run_predictions_for_threat_zone.sh $CURRENT_THREAT_ZONE 1"
    #/home/vivek/Work/kaggle/dhs/body_scan/run_predictions_for_threat_zone.sh $CURRENT_THREAT_ZONE 1
    echo "/home/vivek/Work/kaggle/dhs/body_scan/run_predictions_for_threat_zone.sh $CURRENT_THREAT_ZONE 0"
    /home/vivek/Work/kaggle/dhs/body_scan/run_predictions_for_threat_zone.sh $CURRENT_THREAT_ZONE 0
done
