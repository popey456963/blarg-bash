#!/usr/bin/perl 

use strict;
use warnings;

use Math::Prime::Util::GMP ':all';

my $sum = 0;

my $min = 49999951;
my $max = 50000000;
my $number = 1;

for(my $i = 1; $i <= $max; $i++) {
    print("$i/$max\n");
    $number = next_prime($number);
    if($i >= $min) {
        $sum += $number;
    }
}

print "$sum\n";