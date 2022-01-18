foreach $number(@ARGV)
{
    $original=$number;
    until($number==0){
        $bit=$number%2;
        unshift(@bit_arr,$bit);
        $number=int($number/2);
    }
    $binary=join("",@bit_arr);
    print("$original = $binary\n");
    $#bin_arr=-1;

}