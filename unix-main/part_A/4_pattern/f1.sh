#!/bin/sh
if [ $# -eq 0 ]
then 
echo "no arg"
else
grep "$1" $2
fi