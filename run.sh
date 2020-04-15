#! /bin/bash

echo "Executing Crop.py"
python3 crop.py > /dev/null
if [[ $? -ne 0 ]]
then
  echo "Crop.py failed" 1>&2
  exit 1
fi
echo "Crop.py Executed succesfully"

echo "Executing Percentage.py"
python3 percentage.py > /dev/null
if [[ $? -ne 0 ]]
then
  echo "Percentage.py failed" 1>&2
  exit 1
fi
echo "Percentage.py Executed succesfully"

echo "Data generated succesfully, output in 'data.txt'"
exit 0
