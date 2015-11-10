
def calculate_tip (total_bill) :
	tip = total_bill * .10
	return tip

print "the tip is %f" % calculate_tip(42.50)
print "the tip is %.2f" % calculate_tip(42.50)
print "the tip is %.3f" % calculate_tip(42.50)
print "the tip is %.0f" % calculate_tip(42.50)


def calculate_tip2 (total_bill, tip_percent):
	tip2 = total_bill * tip_percent 
	return tip2 

print "the tip2 is %.2f" % calculate_tip2(42.50, .2)
print "the tip2 is %.3f" % calculate_tip2(42.50, .3)
print "the tip2 is %.0f" % calculate_tip2(42.50, .0)


def tip_with_friends (total_bill, tip_percent, num_friends):
	tip3 = (total_bill * tip_percent) / num_friends
	return tip3

print "Each person should pay %.2f" % tip_with_friends (42.5, .2, 2)

