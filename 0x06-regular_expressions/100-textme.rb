#!/usr/bin/env ruby
#Return: from,to & message([sender],[Receiver],[flags])
#The sender phone number or name (including country code if present)
#The receiver phone number or name (including country code if present)
#The flags that were used
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
