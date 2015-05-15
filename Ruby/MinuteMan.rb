#!/usr/bin/env ruby
 
require 'net/http'
 
def request
  res = Net::HTTP.get_response(URI('http://www.hacker.org/challenge/misc/minuteman.php'))
  return res.body
end
 
@html = request
 
while true
  data = request
  if data != @html
    puts Time.now, data
    break
  end
  sleep 20
end