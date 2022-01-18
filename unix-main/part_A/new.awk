BEGIN{
FS="|" 
printf "Employee Record\n\t\tnum\t\tsalary\n"
}
{
da=0.25*$6
hra=0.50*$6
gp=$6+da+hra
tot[1]+=$6
tot[2]+=da
tot[3]+=hra
tot[4]+=gp
cnt++

printf "\t\t%d\t\t%d\n",$1,$6
}
END{
printf "Employee Record\n\t\t","Basic DA DRA Gross"
printf "\t\tAverage %5d %5d %5d %5d\nEND OF RECORD\n",tot[1]/cnt,tot[2]/cnt,tot[3]/cnt,tot[4]/cnt
}