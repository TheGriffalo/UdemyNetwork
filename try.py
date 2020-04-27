try:
    print (4/0)
except ZeroDivisionError:
    print("Not allowed!")
finally:
    print("I don't care, I'm getting printed anyway...")