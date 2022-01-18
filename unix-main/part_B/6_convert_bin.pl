#!/usr/bin/perl
foreach $number(@ARGV){
    $original=$number;
    until($number==0){
        $bit=$number%2;
        unshift(@bit_arr,$bit);
        $number=int($number/2);
    }
    $binary_number=join("",@bit_arr);
    print("the binary of $original is $binary_number\n");
    $#bin_arr="\0";


}