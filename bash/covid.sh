#!/bin/bash
#This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
STATES=$(echo $DATA | jq '.[0].states')
LAST=$(echo $DATA | jq '.[0].lastModified')
TODAY=$(date)

printf "\nOn $TODAY, there were $POSITIVE positive cases,\n$NEGATIVE negative cases, and $DEATH deaths in a total of $STATES states.\nThis data was last modified on $LAST\n"
