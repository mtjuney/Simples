#!/bin/ruby

(r, c, k) = gets.chomp.split(" ").map{|item| item.to_i}

ame_masses = Hash.new
row_ame_nums = Array.new(r, 0)
cal_ame_nums = Array.new(c, 0)

n = gets.chomp.to_i

i = 0
while(i < n)
  (rr, cc) = gets.chomp.split(" ").map{|item| item.to_i - 1}
  if ame_masses.has_key?(rr.to_s) then
    ame_masses[rr.to_s][cc.to_s] = 1
  else
    ame_masses[rr.to_s] = {cc.to_s => 1}
  end
  row_ame_nums[rr] += 1
  cal_ame_nums[cc] += 1
  i += 1
end

ans_mass_num = 0

row_ame_nums.each_with_index do |row_ame_num, rr|
  if row_ame_num <= k then
    cal_ame_nums.each_with_index do |cal_ame_num, cc|
      get_ame_num = row_ame_num + cal_ame_num
      if ame_masses[rr.to_s][cc.to_s] == 1 then
        get_ame_num -= 1
      end
      if get_ame_num == k then
        ans_mass_num += 1
      end
    end
  end
end


print ans_mass_num.to_s + "\n"
