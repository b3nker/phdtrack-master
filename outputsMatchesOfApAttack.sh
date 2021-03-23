filepath=$1
outputPathAndName=$2
finalPathCsvFile=$3


#Parse matches into a csv file with the following attributes: id_user, id_predicted
jq -r '(.report.artifacts[] | select(.name=="MatMatchingKSetsnonObf/matches") | .value) | to_entries | map([.key, .value])[] | @csv' $filepath | sed 's/"//g' > $outputPathAndName

#Parse previous csv file into a new csv
python3 user_data_to_csv.py dataset/users/ $outputPathAndName $finalPathCsvFile