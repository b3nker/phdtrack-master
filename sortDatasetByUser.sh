#sort
pathDataset=$1 
pathSortedDataset=$2 

#sort $pathDataset > $pathSortedDataset 
(head -n1 $pathDataset && tail -n+2 $pathDataset | sort -t"," -k1) > $pathSortedDataset 