a, b = gets.strip.split.map(&:to_i)

if [a, b].max > 8
    puts ":("
else
    puts "Yay!"
end

