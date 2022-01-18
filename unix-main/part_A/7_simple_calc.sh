#!/bin/sh
echo "option are + - / *"
echo "enter two numbers"
read a
read b
echo "\nenter ur choice"
read ch
case $ch in
'+')y=`expr $a + $b`
echo "result is $y";;
'-')y=`expr $a - $b`
echo "result is $y";;
'*')y=`expr $a \* $b`
echo "result is $y";;
'/')y=`expr $a / $b`
echo "result is $y";;
esac


