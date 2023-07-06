#!/usr/bin/env ruby

log_entries = ARGV[0]

regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

log_entries.scan(regex) do |sender, receiver, flags|
  puts "#{sender},#{receiver},#{flags}"
end
