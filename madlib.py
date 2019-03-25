#these raw inputs allow users to input their desired strings to the madlib
name = raw_input("Name:")
pronoun = raw_input("Pronoun:")
noun = raw_input("Noun:")

#madlib is the base madlib we will be inserting values to
madlib = """%s went for a walk in the park. %s
found a %s. %s decided to take the %s home.""" % (name, pronoun, noun, name, noun)

print madlib