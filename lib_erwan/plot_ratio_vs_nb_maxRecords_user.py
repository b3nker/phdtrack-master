PATH_RESULT_MAXRECORDS_USECASE = '../use-case_NbRecords/result_MaxRecords_usecase.csv'

nb_users = []
ratios = []

# Read result csv and store values in data structures
with open(PATH_RESULT_MAXRECORDS_USECASE) as f:
    for line in f:
        infos = line.split(',').rstrip('\n')
        nb_user = int(infos[0])
        reid_ratio = float(infos[1])
        nb_users.append(nb_user)
        ratios.append(reid_ratio)

# Plot