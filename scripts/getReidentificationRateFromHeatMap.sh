> resultComparison/percentages.csv

#Create Dataframe of test and train and compute the reidentified user
python3 lib/divideProcess.py result_heatMaps/data/*/train.csv result_heatMaps/data/*/test.csv

#Write results
python3 lib_erwan/write_percentage_csv.py resultComparison/results.csv resultComparison/percentages.csv