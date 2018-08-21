m=raw_input('enter your number: ')
m=int(m)
if m<50:
    if(m<=20):
        print "your number is between 10 & 20"
    else:
        print "%d is bigger than 20" % m
elif (m>100):
    print("your number is bigger than 100")
else:
    print "your number is smaller than 10"
    if(m<0):
        print("your number is negative:(")
