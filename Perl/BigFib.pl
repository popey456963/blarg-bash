use strict;
use warnings;

use bignum;

my $phi = (1 + sqrt(5)) / 2;
my $beta = -1/$phi;

printf("%.1f\n", 150000000000000 * log($phi) - log($phi-$beta));