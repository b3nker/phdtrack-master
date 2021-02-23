inputDir=$1 # les données input de trilateration c les données avec 3 columns (lat, lng, timestamp) , et non pas sous la forme d'accio

outputDir=$2 # il faut créer ce repertoir avant de lancer l'executable.

range=$3

java -jar trilaterationv3.jar "$inputDir/" $outputDir 0.6 $range  

# les valeurs 0.6 (km) = delta  et 1 (km) = range ( c des parametres de ce LPPM) à faire varier pour tester 
