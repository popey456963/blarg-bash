#!/usr/bin/perl 
use strict; 
use warnings; 

#Required Variables
my @levelinfo; 
my ($tempstring, $path); 
my $i; 
&read_website(""); #Function to get source

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
 $path = "."x$i; 
 $tempstring = &bruteforce($path); 
 $i++; 
}while($tempstring eq "False"); 
print "$tempstring";

sub bruteforce{ 
 my $tempstring; 
 my $path = $_[0]; 
 my $i = index($path, "\."); 
 if($i > -1){ 
  substr($path, $i, 1) = "R"; 
  $tempstring = &bruteforce($path); 
 }else{ 
   $tempstring = &Verify($path); 
   if($tempstring eq "False"){return $tempstring;} 
   else{return $path;} 
 } 
 if($tempstring ne "False"){return $tempstring;} 
 else{ 
  substr($path, $i, 1) = "D"; 
  $tempstring = &bruteforce($path); 
  return $tempstring; 
 } 
} 

sub Verify{ 
 my ($map_x, $map_y) = (1, 1); 
 my $count = -1; 
 do{ 
  $count++; 
  if($count == length($path)){$count = 0;} 
  if(substr($_[0], $count, 1) eq "R"){$map_x++;} 
  elsif(substr($_[0], $count, 1) eq "D"){$map_y++;} 
 }while(substr($levelinfo[0], $map_y*$levelinfo[3]+$map_x, 1) eq "."); 
 if(substr($levelinfo[0], $map_y*$levelinfo[3]+$map_x, 1) eq "X"){return "False";} 
 else{return "True";} 
} 

sub read_website { 
 use LWP::Simple; #Package to get HTML source
  my $htmlsource = get("http://www.hacker.org/runaway/index.php?name=popey456963&password=password123&gotolevel=25") 
   || die "Cannot Reach Website"; #Read HTML content or die
  my $number = index($htmlsource, "FVterrainString="); 
  my $number2 = index($htmlsource, "\"", $number) - $number; 
 $htmlsource = substr($htmlsource, index($htmlsource, "FVterrainString="), $number2); 
 @levelinfo = split("&", $htmlsource); 
 foreach $number (0..$#levelinfo) { 
  $levelinfo[$number] = substr($levelinfo[$number], (index($levelinfo[$number], "=") + 1)); 
 } 
}