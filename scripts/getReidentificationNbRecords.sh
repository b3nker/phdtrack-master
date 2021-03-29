numberOfUserPerIteration=$1
restartProcess=$2

PATH_FILES=../use-case_NbRecords

rm $PATH_FILES/result_MaxRecords_usecase.csv
rm $PATH_FILES/matches.csv
#rm $PATH_FILES/usersRead.csv
rm -r $PATH_FILES/usersToRead/

i=1
END=10
while [ $i -le $END ];
do
currentNumberOfUsersRead=$(($i * $numberOfUserPerIteration))
echo $i
echo $currentNumberOfUsersRead
#Clean the directories
rm -r $PATH_FILES/result_ap-attack
rm -r $PATH_FILES/test
rm -r $PATH_FILES/train
#rm $PATH_FILES/final_results.csv

#Create the directory
mkdir $PATH_FILES/result_ap-attack

#Extract Traces of users with biggest data
python3 $PATH_FILES/extractUsersWithLargeTraces.py $PATH_FILES/nbRecordsPerUser.csv $PATH_FILES/usersToRead $restartProcess $PATH_FILES/usersRead.csv $currentNumberOfUsersRead

#Run split train test
python3 ../lib_erwan/splitFullTracesInTrainAndTest.py $PATH_FILES/usersToRead/ $PATH_FILES/train $PATH_FILES/test

#Run ap-attack
sh ../Exemple-ap-attack/run_accio-attack.sh $PATH_FILES/train/ $PATH_FILES/test/ $PATH_FILES/result_ap-attack/
OUTPUT_FILE=$(find ../use-case_NbRecords/result_ap-attack/ -type f -iname "run*");

#Parse matches into a csv file with the following attributes: id_user, id_predicted
jq -r '(.report.artifacts[] | select(.name=="MatMatchingKSetsnonObf/matches") | .value) | to_entries | map([.key, .value])[] | @csv' $OUTPUT_FILE | sed 's/"//g' > $PATH_FILES/matches.csv

#Write result to csv
python3 ../lib_erwan/write_percentage_csv.py $currentNumberOfUsersRead $PATH_FILES/matches.csv
i=$(($i+1))
done

#Plot diagram
python3 ../lib_erwan/plot_ratio_vs_nb_maxRecords_user.py

#Parse previous csv file into a new csv
#python3 ../lib/user_data_to_csv.py $PATH_FILES/usersToRead/ $PATH_FILES/matches.csv $PATH_FILES/final_results.csv

#Plot diagram
#python3 ../lib/user_result.py $PATH_FILES/final_results.csv
