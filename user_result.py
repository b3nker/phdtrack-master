import sys
import matplotlib.pyplot as plt
import numpy as np

# Inputs
inputFile = sys.argv[1]

# Well predicted
id_wp = []
records_wp = []

# Badly predicted
id_bp = []
records_bp = []

with open(inputFile) as open_file_object:
    for line in open_file_object:
        infos = line.rstrip("\n").split(',')
        if infos[0] == infos[1]:  # compare id and prediction_id
            id_wp.append(infos[0])
            records_wp.append(int(infos[2]))
        else:
            id_bp.append(infos[0])
            records_bp.append(int(infos[2]))

# Sorting in descending order
records_bp, id_bp = zip(*sorted(zip(records_bp, id_bp), reverse=True))
records_wp, id_wp = zip(*sorted(zip(records_wp, id_wp), reverse=True))

# Computing a few statistics
percentage = round(len(id_wp) / (len(id_wp) + len(id_bp)), 2)
mean_nb_record_wp = np.sum(records_wp) / len(records_wp)
mean_nb_record_bp = np.sum(records_bp) / len(records_bp)

# Plot 1
y_pos = np.arange(len(id_wp))
plt.bar(y_pos, records_wp, align='center', alpha=0.5)
plt.xticks(y_pos, id_wp)
plt.ylabel('#records')
plt.xlabel('User ids')
plt.title('Number of record per user re-identified')
plt.show()

# Plot 2
y_pos = np.arange(len(id_bp))
plt.bar(y_pos, records_bp, align='center', alpha=0.5)
plt.xticks(y_pos, id_bp)
plt.ylabel('#records')
plt.title('Number of record per user badly re-identified')
plt.xlabel('User ids')
plt.show()

# printing data
print('re-identification (%): ', percentage, '\n' +
      'mean #records (re-identified): ', round(mean_nb_record_wp), '\n' +
      'mean #records (not re-identified): ', round(mean_nb_record_bp))
