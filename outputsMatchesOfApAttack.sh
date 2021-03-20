filepath=$1

#select json object "MatMatchingKSetsnonObf/matches" from file in input and convert it's value to csv
jq -r '(.report.artifacts[] | select(.name=="MatMatchingKSetsnonObf/matches") | .value) | to_entries | map([.key, .value])[] | @csv' $filepath | sed 's/"//g' >result.csv 