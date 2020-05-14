import time
localtime = time.asctime( time.localtime(time.time()) )
print("Hello there: ")

word=input("kuch kaho: ")

if word == 'hi':
    print('Hi!')
elif word == 'hello':
    print('Hello')
elif word == 'bye':
    print('Good Bye!!')
elif word == 'kya kr rahe ho':
    print('Time Pass!!')
elif word == 'kaho ho':
    print('room me')
elif word == 'kya time ho raha h':
    print (localtime)
elif word == 'or weekend ka kya plan h':
    print('tmhari kh ke lunga!!')
elif word == 'anda khilao be':
    print('bhago Bhosdike!!')
elif word == 'kab miloge':
    print("tmhare sone ke bad or uthne se phle..")
else:
    print("or kuch kam ni h kya yaha time pass kr raha h !!")