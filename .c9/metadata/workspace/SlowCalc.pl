{"filter":false,"title":"SlowCalc.pl","tooltip":"/SlowCalc.pl","undoManager":{"mark":4,"position":4,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":31,"column":1},"action":"insert","lines":["#!/usr/bin/perl","","use warnings;","use strict;","","# fucking slow","","calc(99);","","sub calc {","    ","    my ($num) = @_;","    my $num2 = 0;","","    for(my $i = 0; $i < $num; $i++) {","        for(my $j = 0; $j < $num; $j++) {","            for (my $k = 0; $k < $num; $k++) {          ","                for(my $l = 0; $l < $num; $l++) {","                    $num2 =  unpack \"l\", pack \"l\", $num2 + length($i . \" to \" . $j . \" to \" . $k . \" to \" . $l) * $num;","                    $num2 = unpack \"l\", pack \"l\", $num2 + 4 * $num;","                    if($num < 10) {","                        $num2 = unpack \"l\", pack \"l\", $num2 + $num;","                    } else {","                        $num2 = unpack \"l\", pack \"l\", $num2 + 10 + (2 * ($num-10));","                    }","                }","            }","        }","        print(\"$i\\n\");","    }","    print \"val: $num2\\n\";","}"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":5},"end":{"row":7,"column":7},"action":"remove","lines":["99"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["2"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":["2"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["9"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["9"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":0},"end":{"row":13,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1418753889426,"hash":"a0a2d87670551b345dc2b417c85bdbe996e2d1fb"}