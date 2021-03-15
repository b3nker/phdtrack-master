#Run decoupage dataset benjamin
#Lit le dataset et le coupe en fichiers par utilisateur dans le dossier test
python3 ../dataset_benjamin/decoupage_dataset.py locations.csv test 10000

#Run split utilisateur en X traces
#Découpe chaque fichier d'utilisateur en X trace de Y secondes
python3 ../dataset_benjamin/splitTracesByFixedSlices_functional.py test test_traces 36000

#Run split train test
python3 ../dataset_benjamin/decoupage_panda.py test_traces/ train_set/ test_set/ 0.8
