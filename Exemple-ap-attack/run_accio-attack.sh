json="ap-attack.json"  # "poi-attack.json"
urlTrain=$1
urlTest=$2
workdir=$3
cellSize="800.meters"



possibleLog="$workdir""//log-XXXXXXXXXXX.txt"
log=$(mktemp $possibleLog) 


#Preparer les données pour accio ( Add the 4th column of IDs)
#python prepareTraceForAccio.py $urlTrain "$workdir/train-accio"
#python prepareTraceForAccio.py $urlTest "$workdir/test-accio"

#Run accio
java -jar  accio.jar run -workdir $workdir -params "urlTrain=$urlTrain urlTest=$urlTest cellSize=$cellSize"  $json >> $log

#Pour recuperer l'accuracy ( taux de re-identification des traces de mobilité): 
accuracy=$(bash getRate.sh "AP-Attack rate" $log)   # "POI-Attack rate" dans le cas de poi-attack
echo "$accuracy"

#bash Exemple-ap-attack/run_accio-attack.sh mini-priva/result-mini-priva/train-merged-accio/  mini-priva/result-mini-priva/test-accio/ Exemple-ap-attack/result/

