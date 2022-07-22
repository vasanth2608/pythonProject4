import threading
def func1():
  print("function 1")
def func2():
  print("function 2")
th1 = threading.Thread(name ="My frist thread",target = func1)
th2 = threading.Thread(target = func2)
th1.start()
th2.start()