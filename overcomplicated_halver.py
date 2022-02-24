import random

#produce random variable
#add to sum
#divide by n
rando = list()
def randavg():
    x = random.randint(0,1001)
    rando.append(x)
    avg = sum(rando)/len(rando)
    print(avg)

   
for i in range(5000):
    randavg()
print(str(sum(rando)) + " " + str(len(rando)))
