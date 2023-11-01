#!/usr/bin/env ruby
the script search string that start with h &  ends with n
puts ARGV[0].scan(/^h.n$/).join
