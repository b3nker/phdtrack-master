import matplotlib.pyplot as plt

PATH_RESULT_MAXRECORDS_USECASE = 'dataset/result_%MaxRecords_usecase.csv'

nb_users = [] # x-coordinates
ratios = [] # y-coordinates

# Read result csv and store values in data structures
with open(PATH_RESULT_MAXRECORDS_USECASE, 'r') as f:
    for line in f:
        infos = line.rstrip('\n').split(',')
        nb_user = int(infos[0])
        reid_ratio = float(infos[1])
        nb_users.append(nb_user)
        ratios.append(reid_ratio)
print(nb_users)
print(ratios)

# Plot
plt.plot(nb_users, ratios)
plt.xlabel('Number of users')
plt.ylabel('Re-identificiation ratio (%)')
plt.show()