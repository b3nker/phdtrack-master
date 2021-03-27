numberOfLine=$1
#timestamp=$2
ratio=$2

#clean le directory
rm -r dataset/users
rm -r dataset/traces
rm -r dataset/test_set
rm -r dataset/train_set
rm -r dataset/accio_output
rm -r dataset/results.csv
rm -r dataset/matches.csv

#Run decoupage dataset benjamin
#Lit le dataset et le coupe en fichiers par utilisateur dans le dossier test
python3 lib_benjamin/split_dataset/decoupage_dataset.py dataset/locations.csv dataset/users $numberOfLine
#dataset_erwan/divideDatasetByUser.py or lib_benjamin/split_dataset/decoupage_dataset.py

#Run split utilisateur en X traces
#Découpe chaque fichier d'utilisateur en X trace de Y secondes
#python3 lib_benjamin/split_dataset/splitTracesByFixedSlices_functional.py dataset/users dataset/traces $timestamp
#dataset_erwan/divideTracesByTimestamp.py or lib_benjamin/split_dataset/splitTracesByFixedSlices_functional.py

#Run split train test
#python3 lib_benjamin/split_dataset/decoupage_panda.py dataset/traces/ dataset/train_set/ dataset/test_set/ $ratio
python3 lib_benjamin/split_dataset/decoupage_percentage.py dataset/users dataset/train_set/ dataset/test_set/ $ratio

mkdir dataset/accio_output
#Run accio with AP-Attack
bash Exemple-ap-attack/run_accio-attack.sh dataset/train_set dataset/test_set dataset/accio_output/

#Find matches Json
matchesJson=$(find dataset/accio_output/ -type f -iname "run*");

#Parse matches into a csv file with the following attributes: id_user, id_predicted
jq -r '(.report.artifacts[] | select(.name=="MatMatchingKSetsnonObf/matches") | .value) | to_entries | map([.key, .value])[] | @csv' $matchesJson | sed 's/"//g' > dataset/matches.csv

#Parse previous csv and find number of records by user to get  : "User_id; Prediction_id; Nb_lines"
python3 user_data_to_csv.py dataset/users/ dataset/matches.csv dataset/results.csv


rm -r dataset/matches.csv