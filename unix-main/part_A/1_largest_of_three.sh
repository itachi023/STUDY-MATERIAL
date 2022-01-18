#!/bin/sh
echo "enter 3 number"
read x
read y
read z
if [ $x -ge $y ] && [ $x -ge $z ]
then
echo "$x is largest"
elif [ $y -ge $z ] && [ $y -ge $x ]
then
echo "$y is largest"
elif [ $z -ge $y ] && [ $z -ge $x ]
then
echo "$z is largest"
fi
if [ $x -lt $y ] && [ $x -lt $z ]
then
echo "$x is smallest"
elif [ $y -lt $z ] && [ $y -lt $x ]
then
echo "$y is smallest"
elif [ $z -lt $y ] && [ $z -lt $x ]
then
echo "$z is smallest"
fi