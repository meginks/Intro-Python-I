# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    x = 99
    print(x)
    

changeX()
# This (below) prints 12. What do we have to modify in changeX() to get it to print 99? We have to print the x inside the scope of the function -- see invoked function above
print(x)

# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        y = 999
        print(y)

    inner()
    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope". -- Same as before -- we have to print inside the scope of the inner function and then invoke the function inside the outer function or it won't recognize the difference.
    print(y)

outer()
