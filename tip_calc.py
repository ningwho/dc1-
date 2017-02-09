tip = 22

if tip >= 20:
    print 'good.'
elif tip <= 15:
    print 'fair.'
else:
    print 'bad.'

    total_bill = float(raw_input("Total bill amount? "))
    service = raw_input("Level of service? ")
    good = float(.20 * total_bill)
    fair = float(.15 * total_bill)
    bad = float(.10 * total_bill)
    good_bill = float(good + total_bill)
    fair_bill = float(good + total_bill)
    bad_bill = float(bad + total_bill)


    if service == "good":
        print "tip amount: %f" % good
        print "total amount: %f" % good_bill
    elif service == "fair":
        print "Tip amount: %0.2f" % fair
        print "total amount: %0.2f" % fair_bill 
    elif service == "bad":
        print "Tip amount: %.2f" % bad
        print "total amount: %.2f" % bad_bill
