#Clean the directories
rm -r result_heatMaps
#Create the directory
mkdir result_heatMaps/
mkdir result_heatMaps/data/

json="ap-attack_heatMap.json"  
workdir=result_heatMaps

possibleLog="$workdir""//log-XXXXXXXXXXX.txt"
log=$(mktemp $possibleLog) 

#Run accio
java -jar  accio.jar run -workdir $workdir $json >> $log

