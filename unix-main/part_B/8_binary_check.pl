print("enter the filename:\n");
$filename=<STDIN>;
chop($filename);
if(-e $filename){
    print("file $filename exist\n");
    if(-B $filename){
        print("it is binary file\n");
    }
    else{
        print("it is not a binary file\n")
    }
    }
else{
    print("file $filename does not exist\n")
}
