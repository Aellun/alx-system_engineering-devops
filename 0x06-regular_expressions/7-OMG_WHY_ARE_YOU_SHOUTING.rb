#!/usr/bin/env ruby
#this regex that matches only uppercase letters
puts ARGV[0].scan(/[A-Z]*/).join
