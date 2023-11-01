#!/usr/bin/env ruby
#the script that matches 10 digit number
puts ARGV[0].scan(/^\d{10,10}$/).join
