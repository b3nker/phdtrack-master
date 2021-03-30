# Library with useful methods
def file_len(file_path):
    with open(file_path) as f:
        for i, l in enumerate(f):
            pass
    try:
        return i + 1
    except NameError:
        print("i is not defined")
        
