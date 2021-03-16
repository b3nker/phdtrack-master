numberOfLine=$1
#timestamp=$2
ratio=$3

#clean le directory
rm -r dataset/test
rm -r dataset/traces
rm -r dataset/test_set
rm -r dataset/train_set

#Run decoupage dataset benjamin
#Lit le dataset et le coupe en fichiers par utilisateur dans le dossier test
python3 dataset_benjamin/decoupage_dataset.py dataset/locations.csv dataset/users $numberOfLine
#dataset_erwan/divideDatasetByUser.py or dataset_benjamin/decoupage_dataset.py 

#Run split utilisateur en X traces
#Découpe chaque fichier d'utilisateur en X trace de Y secondes
#python3 dataset_benjamin/splitTracesByFixedSlices_functional.py dataset/users dataset/traces $timestamp
#dataset_erwan/divideTracesByTimestamp.py or dataset_benjamin/splitTracesByFixedSlices_functional.py

#Run split train test
#python3 dataset_benjamin/decoupage_panda.py dataset/traces/ dataset/train_set/ dataset/test_set/ $ratio
python3 dataset_benjamin/decoupage_percentage.py dataset/users dataset/train_set/ dataset/test_set/ $ratio