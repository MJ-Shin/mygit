#setup
n=0

#set function
def setup():
    global n
    n = 100

def loop():
    global n
    n = n+1
    if (n%2==0):
        print(n)

#main
    setup()
    while True:
        loop()
    
