#!/usr/bin/env ruby
#This script search for the input pattern
puts ARGV[0].scan(/hbt{2,5}n/).join
