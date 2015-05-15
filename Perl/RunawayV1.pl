#!/usr/bin/perl 
use strict; 
use warnings; 

#Required Variables
my @levelinfo; 
my ($tempstring, $pfad); 
my $i; 
&read_website(""); 

$i = 0; 
$levelinfo[3] += 2; 
$levelinfo[4] += 2; 
$tempstring = "X"x$levelinfo[3]; 
for (1..($levelinfo[4]-2)){ 
 $tempstring .= "X".substr($levelinfo[0], $i, $levelinfo[3]-2)."L"; 
 $i += $levelinfo[3] - 2; 
} 
$tempstring .= "X"."L"x($levelinfo[3]-2)."X"; 
$levelinfo[0] = $tempstring; 


$i = $levelinfo[2]; 
do{ 
 print "$i\n";
 $pfad = "."x$i; 
 $tempstring = &bruteforce($pfad); 
 $i++; 
}while($tempstring eq "falsch"); 
print "$tempstring";

sub bruteforce{ 
 my $tempstring; 
 my $pfad = $_[0]; 
 my $i = index($pfad, "\."); 
 if($i > -1){ 
  substr($pfad, $i, 1) = "R"; 
  $tempstring = &bruteforce($pfad); 
 }else{ 
   $tempstring = &verifizieren($pfad); 
   if($tempstring eq "falsch"){return $tempstring;} 
   else{return $pfad;} 
 } 
 if($tempstring ne "falsch"){return $tempstring;} 
 else{ 
  substr($pfad, $i, 1) = "D"; 
  $tempstring = &bruteforce($pfad); 
  return $tempstring; 
 } 
} 

sub verifizieren{ 
 my ($mom_x, $mom_y) = (1, 1); 
 my $zaehler = -1; 
 do{ 
  $zaehler++; 
  if($zaehler == length($pfad)){$zaehler = 0;} 
  if(substr($_[0], $zaehler, 1) eq "R"){$mom_x++;} 
  elsif(substr($_[0], $zaehler, 1) eq "D"){$mom_y++;} 
 }while(substr($levelinfo[0], $mom_y*$levelinfo[3]+$mom_x, 1) eq "."); 
 if(substr($levelinfo[0], $mom_y*$levelinfo[3]+$mom_x, 1) eq "X"){return "falsch";} 
 else{return "richtig";} 
} 

sub read_website { 
 use LWP::Simple; #Packet, um den HTML-Inhalt auszulesen, initialisieren 
  my $htmlinhalt = get("http://www.hacker.org/runaway/index.php?name=popey456963&password=password123") 
   || die "KANN WEBSITE NICHT OEFFNEN"; #auslesen des HTML-Inhaltes 
  my $zahl = index($htmlinhalt, "FVterrainString="); 
  my $zahl2 = index($htmlinhalt, "\"", $zahl) - $zahl; 
 $htmlinhalt = substr($htmlinhalt, index($htmlinhalt, "FVterrainString="), $zahl2); 
 @levelinfo = split("&", $htmlinhalt); 
 foreach $zahl (0..$#levelinfo) { 
  $levelinfo[$zahl] = substr($levelinfo[$zahl], (index($levelinfo[$zahl], "=") + 1)); 
 } 
}