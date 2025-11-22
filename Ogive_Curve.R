#class intervals
lb = c(0,5,7,9, 11,13)
Ub = c(5,7,9, 11, 13, 15)

#Frequencies
freq= c(5, 11, 26, 10,5)

# less than cumulative freq
lcf = cumsum(freq)
lcf1 = c(0, lcf) #starts from 0

# greater than cumulative freq
gcf = rev (cumsum(freq))
gcf1 = c(gcf,0) #ends with 0

data = data.frame(lb, Ub, lcf1, gcf1)

plot(lb,gcf1, type = "l", main = "ogive curve", xlab = "length of life", ylab =" No. of lamps")
points (lb,gcf1, col = "green", pch = 19)

lines (Ub, lcf1, type="l",col="blue")
points (Ub, lcf1,col = "pink", pch=19)
