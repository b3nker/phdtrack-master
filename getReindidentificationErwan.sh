numberOfLine=$1
#timestamp=$2

#clean le directory
rm -r dataset/

#crée les répertoires
mkdir dataset/
mkdir dataset/result_ap-attack

#Run decoupage dataset erwan
#Lit le dataset et le coupe en fichiers par utilisateur dans le dossier test
python3 dataset_erwan/divideDatasetByUser.py ../dataset/locations.csv dataset/users $numberOfLine

#Run decoupage en intervalle de temps
#Découpe chaque fichier d'utilisateur en X trace de Y secondes
#python3 dataset_erwan/divideTracesByTimestamp.py dataset_erwan/decoupages_dataset/slicesByUser/ dataset_erwan/decoupages_dataset/slicesByTimestamp $timestamp

#Run split train test
python3 dataset_erwan/splitFullTracesInTrainAndTest.py dataset/slicesByUser/ dataset/train dataset/test

#run ap-attack
sh Exemple-ap-attack/run_accio-attack.sh dataset/train/ dataset/test/ dataset/result_ap-attack/

OUTPUT_FILE=$(find dataset/ -type f -iname "run*");

#sh outputsMatchesOfApAttack.sh $OUTPUT_FILE dataset/matches.csv dataset/results.csv

#Parse matches into a csv file with the following attributes: id_user, id_predicted
jq -r '(.report.artifacts[] | select(.name=="MatMatchingKSetsnonObf/matches") | .value) | to_entries | map([.key, .value])[] | @csv' $OUTPUT_FILE | sed 's/"//g' > dataset/matches.csv

#Parse previous csv file into a new csv
python3 user_data_to_csv.py dataset/users/ dataset/matches.csv dataset/results.csv
