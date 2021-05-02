# PhD Track : Re-identification rate on MCOC Dataset

 Introduction project to research as part of INSA Lyon / Passau dual degree together with LIRIS lab.
 Based on LIRIS's privamov team [previous work](https://github.com/privamov/accio), we aimed at computing the re-identification rate of accio with different attacks and LPPMs.

This project allows the computation of the re-identification rate with different parameters:
 - Percentage of train/test
 - User selection (random, most traces)
 - Duration of traces
 
 We also tried to extract heat-maps from accio to speed-up the runtime of our scripts, but without success.
 
 Last part was to scale up. We launched our experiments on Grid'5000 clusters.
## Requirements
- Java
- Python3+ (numpy, pandas, psutil, matplotlib)
- Jq
- accio

## Project Structure
- **scripts** : Contains scripts to launch experiments
- **json** : Contains file configuration for attacks' scripts
- **lib** : Contains common python libaries
- **lib_benjamin** : Contains python files to select users based on randomness
- **lib_erwan** : Contains python files to select users based on their number of records


## Authors
[KERMANI Benjamin](https://github.com/b3nker)
[VERSMEE Erwan](https://github.com/erwan-png)

## Licence

LIRIS / INSA Lyon