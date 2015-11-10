
def do_twice(f, a):
    f(a)
    f(a)
    

def print_spam(my_param):
    print 'spam'
value = 9  

def print_twice(my_parameter_2):
	print my_parameter_2

do_twice(print_spam, value)

do_twice(print_twice, value)

