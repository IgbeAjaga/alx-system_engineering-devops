#!/usr/bin/env ruby

regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

ARGF.each do |line|
  match = line.match(regex)
  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end
