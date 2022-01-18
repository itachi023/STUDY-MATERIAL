for file in "$@"
do
if [ -f $file ]
then
ufile=`echo $file | tr '[a-z]' '[A-Z]'`
if [ -f $ufile ]
then
echo "file is already exist"
else
mv $file $ufile
fi
else
echo "file doesn't exist"
fi
done