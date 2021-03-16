import sys
import matplotlib.pyplot as plt

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
            records_wp.append(infos[2])
        else:
            id_bp.append(infos[0])
            records_bp.append(infos[2])

fig = plt.figure()
fig
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(id_bp, records_bp)  # x, y
plt.legend("Well predicted users")
plt.show()
