print ("Enter the string\n");
$a=<STDIN>;
print ("enter the times string to be displayed:\n");
chop($b=<STDIN>);
$c= $a x $b;
print("result\n$c");