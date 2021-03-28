import sys

#input
csv_file_path = sys.argv[1]
unique_set = set()
with open(csv_file_path) as f:
    for line in f:
        if line not in unique_set:
            unique_set.add(line)
        else:
            print(line) 
