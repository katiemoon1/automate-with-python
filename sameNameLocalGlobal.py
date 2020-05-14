def spam():
    # this is the global variable
    global eggs
    eggs = 'spam'


def bacon():
    eggs = 'bacon'


def ham():
    print(eggs)


# this is global
eggs = 42
spam()
print(eggs)
