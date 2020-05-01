#Fra https://www.youtube.com/watch?v=tw7ror9x32s

def func1():
    b = ["banana", "apple", "microsoft"]
    b.append("aaaaa")
    b.sort()
    print(b)
func1()

def func2():
    b = ["banana", "apple", "microsoft"]
    b.append("aaaaa")
    b.sort(reverse=True)
    print(b)
func2()

def func3():
#bytter index 0 og 2 
    b = ["banana", "apple", "microsoft"]
    print(b)
    temp = b[0]
    b[0] = b[2]
    b[2] = temp
    print(b)
func3()