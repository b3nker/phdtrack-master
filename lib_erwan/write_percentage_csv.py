import sys
sys.path.append('.')  # relative to where you execute the command/script
from lib.utils import file_len

# Write data in the following format {nb of users, %re-identification}

# Inputs
path_matches_csv = sys.argv[1]
PATH_RESULT_MAXRECORDS_USECASE = 'usecase_NbRecords/result_%MaxRecords_usecase.csv'
number_users = file_len("usecase_NbRecords/usersRead.csv")
print(number_users)

#find number of re-identified users
number_reidentified = 0
with open(path_matches_csv) as f:
    for line in f:
        infos = line.rstrip("\n").split(',')
        user_id = infos[0]
        user_prediction = infos[1]
        if(user_id == user_prediction):
            number_reidentified += 1

# Compute re-identification ratio
reid_rate = round(number_reidentified/number_users, 2)

# Write to csv
file = open(PATH_RESULT_MAXRECORDS_USECASE, "a")
file.write(str(number_users) + ',' + str(reid_rate) + '\n')

print('number_users : ', number_users, '--> re-id rate : ', reid_rate)