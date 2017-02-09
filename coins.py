num_coins = 0
print "You have %d coins." % num_coins
switch = raw_input("Do you want another? (yes/no)")
while switch == "yes":
    num_coins +=1
    print "You have %d coins." % num_coins
    switch = raw_input("Do you want another? (yes/no)")
#could use else:
    print "bye"
# while true: num_coins
