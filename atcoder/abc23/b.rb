#!/bin/ruby

n = gets.chomp.to_i
str = gets.chomp


tejun = (n - 1) / 2



def f(t, s)
  if t == 0 then
    if s == "b" then
      return 0
    else
      return -1
    end
  elsif t % 3 == 0 then
    if (s[0] == "b") && (s[-1] == "b") then
      return f((t - 1), s[1, s.length - 2])
    else
      return -1
    end
  elsif t % 3 == 1 then
    if (s[0] == "a") && (s[-1] == "c") then
      return f((t - 1), s[1, s.length - 2])
    else
      return -1
    end
  else
    if (s[0] == "c") && (s[-1] == "a") then
      return f((t - 1), s[1, s.length - 2])
    else
      return -1
    end
  end
end


ans = f(tejun, str)

if ans == 0 then
  ans = tejun
end

print(ans.to_s + "\n")
