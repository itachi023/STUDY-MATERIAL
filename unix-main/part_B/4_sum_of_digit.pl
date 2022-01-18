#!/usr/bin/perl
foreach $num(@ARGV)
{
    $orignal_no=$num;
    $sum=0;
    until($num==0)
    {
        $digit=$num%10;
        $sum=$sum+$digit;
        $num=int($num/10)
    }
    print("$sum\n");
}