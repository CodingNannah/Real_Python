# Syntax of Defining a Function:
# def function_name([parameters]):
#     statement(s)

# function_name is unique & has (), even if empty
# parameters are optional, comma-separated, & may be passed to the function
# : colon is required to end the function header
# statement(s) are the indented part of the body to be executed when the function is called
# ******************************

# Syntax of Calling a Function:
# function_name([arguments])

# function_name carries parentheses, even when empty
# arguments are values passed into the function, which correspond with parameters

def f():
    s = '--Inside f()'
    print(s)

print('Before calling f()')
f()
print('Afer calling f()')

# *****************************

# Define a stub: an empty function that does nothing:

def f():
    pass

f()

# *****************************

# Argument Passing:
# Type 1: Positional or Required - 
# most straight-forward but least flexible way to pass data to a function
# specified by a comma-separated list inside the function's parentheses
# parameters (formal parameters) behave like variables defined to the function
# parameters and arguments must agree in order - unless using keywords that match parameters with an =!
# parameters and arguments must agree in number - cannot leave any out!
# When function is called, specify a corresponding list of arguments (actual parameters); arguments are bound to the parameters in order of assignment

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

f(6, 'bananas', 1.74)
# run = 6 bananas cost $1.74

f('bananas', 6, 1.74)
# run = bananas 6 cost $1.74

f('bananas', 1.74, 6)
# Beware! Out of order arguments may create incorrect results!
# run = bananas 1.74 cost $6.00

# Too few arguments:
# f(6,'bananas')
# run = TypeError: f() missing 1 required argument: 'price'

# Too many arguments:
# f(6, 'bananas', 1.74, 'ripe')
#TypeError: f() takes 3 arguments, 4 were given

# Keyword Arguments:
f(qty=3, item='kumquats', price=1.97)
# run = 3 kumquats cost 1.97

f(item='kumquats', price=1.97, qty=3)
# using keywords in any order produces the same result
# run = 3 kumquats cost 1.97

# Referencing a non-matching keyword:
#f(qty=4, item='apples', cost=2.17)
# TypeError: f() got an unexpected keyword argument 'cost'

# Calling with Positional and Keyword Arguments:
# positional arguments must come first!
f(6, 1.74, item='bananas')
# f(6, item='bananas', 1.74)
# SyntaxError: positional argument (1.74) follows keyword argument (item='bananas')