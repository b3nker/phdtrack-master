numberOfLine=$1
timestamp=$2

#clean le directory
rm -r dataset_erwan/decoupages_dataset
rm -r dataset_erwan/result_ap-attack

#crée les répertoires
mkdir dataset_erwan/decoupages_dataset
mkdir dataset_erwan/result_ap-attack

#Run decoupage dataset erwan
#Lit le dataset et le coupe en fichiers par utilisateur dans le dossier test
python3 dataset_erwan/divideDatasetByUser.py ../dataset/locations.csv dataset_erwan/decoupages_dataset/slicesByUser $numberOfLine

#Run decoupage en intervalle de temps
#Découpe chaque fichier d'utilisateur en X trace de Y secondes
#python3 dataset_erwan/divideTracesByTimestamp.py dataset_erwan/decoupages_dataset/slicesByUser/ dataset_erwan/decoupages_dataset/slicesByTimestamp $timestamp

#Run split train test
python3 dataset_erwan/divideTracesByTrainAndTest.py dataset_erwan/decoupages_dataset/slicesByTimestamp/ dataset_erwan/decoupages_dataset/train dataset_erwan/decoupages_dataset/test