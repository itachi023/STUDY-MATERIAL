#!/usr/bin/perl
die("no arg")if(@ARGV==0);
foreach $arg(@ARGV)
{
    $arg=~ tr /a-z/A-Z/;
    print("$arg\n");
}
