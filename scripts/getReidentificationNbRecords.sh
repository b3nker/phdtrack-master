numberOfUserPetIteration=$1
restartProcess=$2

PATH_FILES=../use-case_NbRecords/

#clean the directory
rm -r $PATH_FILES/result_ap-attack

#Create the directory
mkdir $PATH_FILES/result_ap-attack

#Run decoupage dataset erwan
#Lit le dataset et le coupe en fichiers par utilisateur dans le dossier test
python3 $PATH_FILES/extractUsersWithLargeTraces.py $PATH_FILES/nbRecordsPerUser.csv $PATH_FILES/usersToRead $restartProcess usersRead.csv $numberOfUserPetIteration

#Run split train test
python3 ../lib_erwan/splitFullTracesInTrainAndTest.py $PATH_FILES/usersToRead/ $PATH_FILES/train $PATH_FILES/test

#run ap-attack
sh ../Exemple-ap-attack/run_accio-attack.sh $PATH_FILES/train/ $PATH_FILES/test/ $PATH_FILES/result_ap-attack/
OUTPUT_FILE=$(find ../use-case_NbRecords/result_ap-attack/ -type f -iname "run*");

#sh outputsMatchesOfApAttack.sh $OUTPUT_FILE dataset/matches.csv dataset/results.csv

#Parse matches into a csv file with the following attributes: id_user, id_predicted
jq -r '(.report.artifacts[] | select(.name=="MatMatchingKSetsnonObf/matches") | .value) | to_entries | map([.key, .value])[] | @csv' $OUTPUT_FILE | sed 's/"//g' > $PATH_FILES/matches.csv

#Parse previous csv file into a new csv
python3 ../lib/user_data_to_csv.py $PATH_FILES/usersToRead/ $PATH_FILES/matches.csv $PATH_FILES/final_results.csv

#Plot diagram
python3 ../lib/user_result.py $PATH_FILES/final_results.csv
