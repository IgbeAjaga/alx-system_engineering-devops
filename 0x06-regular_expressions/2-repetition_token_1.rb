#!/usr/bin/env ruby
regex = /hb[t]{0,1}n/
puts ARGV[0].scan(regex).join
