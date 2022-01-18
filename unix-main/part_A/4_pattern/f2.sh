#! /bin/sh
if [ $# -eq 0 ]
then
echo "Enter the pattern"
read pattern
echo "Enter the filename"
read filename
grep $pattern $filename
else
sh f1.sh $1 $2
fi
