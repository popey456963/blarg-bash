require 'gmp'
 
# http://www.angio.net/pi/digits/10000.txt
 
d = File.read("pi.txt")[2,2048]
 
solved = false
 
(1..2048).reverse_each { |s|
  print "\rtrying length #{s}..."
  (0..d.size).each { |x|
    subsequences = d[x,s]
    next unless subsequences.size == s
    z = GMP::Z(subsequences,10)
    if z.probab_prime? != 0
      print "\rtrying length #{s}...OK\n"
      puts "\nanswer: #{z}"
      solved = true
    end
  }
  break if solved
}