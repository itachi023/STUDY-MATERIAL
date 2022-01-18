clear
while true
do
echo "1.copy a file"
echo "2.remove a file"
echo "3.move a file"
echo "4.quit"
echo "enter your choice"
read choice
case "$choice" in
1) echo "enter file name to copy"
read f1
echo "enter filename"
read f2
if [ -f $f1 ]
then
cp $f1 $f2
else
echo "$f1 does not exist"
fi
;;
2)echo "enter file name to remove"
read r1
if [ -f $r1 ]
then
rm -i $r1
else
echo "$r1 does not exist"
fi
;;
3)echo "enter filename to move"
read f1
echo "end of destination"
read f2
if [-f $f1]
then
if [ -d $f2]
then
mv $f1 $f2
fi
else
echo "$f1 does not exist"
fi
;;
4)echo "exit"
exit;;
esac
done
