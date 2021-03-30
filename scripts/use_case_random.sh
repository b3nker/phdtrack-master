nbUsers=$1
ratio=$2
## Cleaning repos
mkdir dataset/accio_output
#rm -r dataset/users
### 1st step : Extract all users data in separated files
## Hypothesis -> Raw data are sorted by users
#python3 lib/splitDSByUser.py dataset/locations_sorted.csv dataset/users/



rm -r dataset/train_set
rm -r dataset/test_set
rm -r dataset/selected_random_users.csv
rm -r dataset/result_random_usecase.csv

for i in {1..10}
do
### 1st step : clean repo
rm -r dataset/accio_output/*
rm -r dataset/matches.csv
rm -r dataset/added_users.csv
### 2nd step : Select and ADD "N" random users iteratively to a CSV + split into %train and %test
python3 lib_benjamin/use_case_random/select_random_users.py $nbUsers dataset/selected_random_users.csv
python3 lib_benjamin/use_case_random/decoupage_percentage_list_users.py dataset/users/ dataset/train_set/ dataset/test_set/ dataset/added_users.csv "$ratio"
### 3rd step :  compute re-identification rate
bash Exemple-ap-attack/run_accio-attack.sh dataset/train_set dataset/test_set dataset/accio_output/
matchesJson=$(find dataset/accio_output/ -type f -iname "run*");
jq -r '(.report.artifacts[] | select(.name=="MatMatchingKSetsnonObf/matches") | .value) | to_entries | map([.key, .value])[] | @csv' $matchesJson | sed 's/"//g' > dataset/matches.csv
### 4th step : Write it into a csv {nb_users, rate}
python3 lib_benjamin/use_case_random/write_percentage_csv.py dataset/selected_random_users.csv dataset/matches.csv
done
