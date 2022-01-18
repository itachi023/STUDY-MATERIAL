{
if(length($0) <= 40)
print $0
else{
    x=$0
    while(length(x) > 40){
        printf "%s \n", substr(x,1,40);
        x=substr(x,41,length(x)-40);
    }
    printf "%s\n",x
}
}
