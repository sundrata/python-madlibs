#these raw inputs allow users to input their desired strings to the madlib
inp1 = raw_input("A color:")
inp2 = raw_input("A color:")

#madlib is the base madlib we will be inserting values to
madlib = "Roses are %s, violets are %s" % (inp1, inp2)

print madlib