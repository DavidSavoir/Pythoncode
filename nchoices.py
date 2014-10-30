import random

def nchoices(lst, integer):
  counter = integer
  listofrandom=[]
  while counter > 0:
    counter -=1
    listofrandom.append(random.choice(lst))
  return (listofrandom)

nchoices([1,2,3,4,5,6,7,8,9,0], 5)
