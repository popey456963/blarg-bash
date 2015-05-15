#!/usr/bin/env ruby
 
require 'net/http'
 
USERNAME = 'XXX'
PASSWORD = 'XXX'
URL = '/www.hacker.org/challenge/chal.php?id=78'
 
@cookies = nil
 
def request
  url = /hackerorgsolution.blogspot.com/2014/09/URI.parse("#{URL}&name=#{USERNAME}&password=#{PASSWORD}")
  res = Net::HTTP.start(url.host, url.port) { |http| http.get(url) }
  @cookies = res.get_fields('set-cookie').to_s
  @cookies = @cookies[/PHPSESSID=(.*?);/]
  return res.body
end
 
def submit answer
  url = /hackerorgsolution.blogspot.com/2014/09/URI.parse("#{URL}&name=#{USERNAME}&password=#{PASSWORD}&answer=#{answer}&go=Submit")
  res = Net::HTTP.start(url.host, url.port) { |http|
    http.get(url, {'Cookie' => @cookies,'Referer' => URL})
  }
end
 
res = request
 
solution = res[/<b>(.*)<\/b>/,1].gsub('<span style="font-size:8%">FOO</span>','')
solution = solution.gsub(' ','+')
 
submit solution