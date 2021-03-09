
json="geoi.json"
workdir=$1
urlData=$2

possibleLog="$workdir""//log-XXXXXXXXXXX.txt"
log=$(mktemp $possibleLog) 


#Prepare data for accio ( Add the 4th column of IDs)
python3 prepareTraceForAccio.py $urlData "$workdir/data-accio"

#Run accio
java -jar accio.jar run -workdir $workdir -params "url=$workdir/data-accio"  $json >> $log


#exemple d'utilisation de get path: 

#path_geoi=$(bash getPath.sh $log $workdir "GeoIndistinguishability/data")

#pour les autres LPPMs à la place de "GeoIndistinguishability/data" : "Promesse/data" , "HeatMapConfusion/out"




