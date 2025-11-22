lbound = c(5,7,9, 11, 13)
ubound = c(7,9, 11, 13,15)
x = (lbound + ubound)/2
Freq = c (5, 11, 26, 10, 5)
data = data.frame(lbound, ubound,x, Freq)
brks = c(lbound[1], ubound)
y = rep (x, Freq)
hist(y, breaks = brks, col ="green", xlab = "lingth of life",ylab= "No. of lamps", main = "Histogram")
lines (x, freq)