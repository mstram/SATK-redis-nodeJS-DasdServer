#!/usr/bin/ruby
require 'redis'
r = Redis.new

print "\n(ruby r1)"
res = system "./py-redis 0 1 3"
#res = system "./p1.py #{a} #{b} #{ar}"

print "\n res:#{res}"

print "\n\n(ruby got) rec: #{r.get('rec')}\n"