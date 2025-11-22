lbound = c(5,7,9, 11, 13)
ubound =  c(7,9,11, 13,15)
x = (lbound + ubound)/2
freq = c (5,11,26,10, 5)
data = data.frame(lbound,ubound,x,freq)
plot(x,freq,xlab = "ength of time in oo hrs",ylab = "No. of lamps ",main = "polygon")
lines(x,freq)