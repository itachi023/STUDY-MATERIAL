#!/bin/sh
echo "enter the string"
read string
if [ -z $string ]
then
echo "null string"
exit
else
echo "enter the character"
read ch 
x=`expr "$string" : '[^'$ch']*'$ch''`
echo "position $x"
z=`expr "$string" : '.*\(...\)' `
echo "$z"
fi