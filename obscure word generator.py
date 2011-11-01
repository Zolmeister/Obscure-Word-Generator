#obscure word generator
import random
print("hit enter for a random obscure word")
input()
f=open("obscure words").read()
table=[]
table=f.split("\n")
while 1:
    line=random.randint(0,15526)
    print(table[line])
    input()
