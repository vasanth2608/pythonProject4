try:
    length =10
    width = 5
    length/width
except NameError:
    print("variable has been used before defining it")
except ZeroDivisionError:
    print("Division by Zero is invalid kindly change ur iput")
except Exception:
    print("New error has occured")
finally:
    print("i will be exceuted atlest once")

