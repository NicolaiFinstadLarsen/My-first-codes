# guess the number 


import random 
import time

print(" \nI want you to guess the number between a start and a stop point. \nKeep going! \nTo stop write 00.1")

n = int(input("Start: "))
m = int(input("Stop: "))
x = random.randrange(n,m)
#print(x)
ans = float(input("What is your guess? "))

while ans != x:
  #print(x)
  if ans == 00.1:
    print("Hate to see you out chicken out like that..")
    break
  elif x<ans:
    print("To high")
    ans = float(input("Try again: "))
    continue
  elif x>ans:
    print("To low")
    ans = float(input("Try again: ")) 
    continue

if x == ans:
  print("Wow, amazing!")
  
time.sleep(10)
