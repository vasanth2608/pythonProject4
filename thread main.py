import threading
t = threading.current_thread() # return the current thread object
print("current thread:",t) # print the thread name,insetifier and status
print("thread name:",t.name)
print("thread identifier:",t.ident)
print("is the thread  alive:",t.is_alive())
t.name='Mythread'
print("After name change:",t.name)
