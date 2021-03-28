import os
import sys
import random

TOTAL_NUMBER_USERS = 642548

# inputs
number_of_users = int(sys.argv[1])
path_to_selected_id_users = sys.argv[2]

# check previously selected users
id_user_selected = set()
if os.path.isfile(path_to_selected_id_users):
    with open(path_to_selected_id_users) as f:
        for line in f:
            id_user_selected.add(int(line.rstrip('\n')))
file = open(path_to_selected_id_users, "a")
# add selected id to csv
for i in range(number_of_users):
    while True:
        random_id_user = random.randint(1, TOTAL_NUMBER_USERS)
        if random_id_user not in id_user_selected:
            break
    file.write(str(random_id_user) + '\n')
    id_user_selected.add(random_id_user)
    