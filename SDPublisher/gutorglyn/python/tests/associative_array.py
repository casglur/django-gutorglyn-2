
value = raw_input("Enter letter: ") # Enter letter such as 'a'

def function_1():
    print "1"

functions = {
    'a': function_1,
}

func = functions[value]
func()