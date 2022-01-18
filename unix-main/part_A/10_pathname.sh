if [ $# -ne 1 ]
then
echo "no argument"
exit
fi

curdir=`pwd`
for dir in `echo $1 | tr '/' ' ' `
do
if [ -d $dir ]
then
echo "dir already exist under `pwd` "
cd $dir
else
mkdir $dir
echo "dir created under `pwd` "
cd $dir
fi
done
cd $curdir