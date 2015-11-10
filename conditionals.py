#my_name = "Jessica"
#partners_name = "Kelsey"
#if (my_name > partners_name):
#	print "My name is greater!"
#elif (partners_name > my_name):
#	print "Their name is greater."
#else:
#	print "Our names are equal!"

#todays_date = float(raw_input("What is the day of the month?"))
#if (todays_date >= 15.0):
#	print "Oh, we're halfway there!"
#else:
#	print "Living on a prayer"

today = raw_input("What day of the week is it?: ").lower()
if (today == "monday"):
	print "Yay class day!"
elif (today == "tuesday"):
	print "Sigh, it's only Tuesday."
elif (today == "wednesday"):
	print "Humpday!"
elif (today == "thursday"):
	print "#tbt"
elif (today == "friday"):
	print "TGIF!"
else:
	print "Yeah, it's the weekend!"



age = 30

if (age >= 18):
	print "Yay! I can Vote"

elif(age <= 18):
	print "Aww I cant vote"


if (age >= 18 and age>= 21):
	print "I can vote and go to a bar"

elif (age >= 18 and age<= 21):
	print "I cant vote and go to a bar"


number1 = 8
number2 = 9

if (0 == number1 % 2 and number2 % 2):
	print "The Number 8 is even"

else:
	print "the number 8 is odd"