#!/usr/bin/perl

use strict;
use warnings;

# x = {unknown byte}
# k = {unknown byte}
# for (i = 0; i < len(txt); i++)
#   c = txt[i] ^ k
#   print c
#   k = (c + x) % 256

my @bytes = (0x31,0x0a,0x77,0x18,0x78,0x1f,0x73,0x4c,0x31,0x42,0x5e,0x77,0x5a,
             0x31,0x4f,0x3b,0x40,0x13,0x2c,0x51,0x22,0x72,0x05,0x99,0xb2,0xdf,
             0xb7,0x90,0xfd,0x8f,0xf8,0x94,0xad,0xd2,0xa4,0xbd,0xc5,0xd1,0xa6,
             0xe9,0x87,0xa0,0xed,0x8e,0xee,0x94,0xad,0xcf,0xbb,0x94,0xee,0x88,
             0xf3,0x82,0x12,0x78,0x19,0x62,0x3a,0x40,0x4d,0x3f);

X_LOOP:
foreach my $x(0..255) {
    my @msg = ();
    for(my $i = (@bytes - 1); $i > 0; $i--) {
        my $k = ($bytes[$i-1] + $x) % 0x100;
        
        my $byte = $bytes[$i] ^ $k;
        if($byte < 32 || $byte > 126) {
            next X_LOOP;
        }

        push(@msg,$byte);
    }

    foreach(reverse(@msg)) {
        print(chr($_));
    }
    print("\n");
}