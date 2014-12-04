#!/bin/bash

# download the zip file
python download_grade_zip.py

# go into downloads (for most unix based machines) 
# and grab most recent file

Z=$(ls -t ~/Downloads | head -n1)
#Z1=$(echo "$Z" | tr ' ' '\')
#Z2=$(echo "$Z1" | tr '(' ' (')
cp ~Downloads/"$Z" .
# cp ./$ZIP ~/Desktop