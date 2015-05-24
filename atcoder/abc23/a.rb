#!/bin/ruby

t = gets.chomp.to_i

t10 = t / 10
t1 = t - (t10 * 10)

print((t10 + t1).to_s + "\n")
