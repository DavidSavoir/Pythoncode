""""def combo(iter_1, iter_2):
  listtuples1=[]
  listtuples2=[]
  for index, value in enumerate(iter_1):
    listtuples1.append([index,value])
  for index, value in enumerate(iter_2):
    listtuples2.append([index,value])
  print(zip(listtuples1, listtuples2))

  FIRST ATTEMPT
  """
#SOLUTION

def combo(items_1, items_2):
  tuples = []
  count = 0

  for items in items_1:
    my_tuple = items_1[count], items_2[count]
    tuples.append(my_tuple)
    count += 1

  return tuples

combo(['swallow', 'snake', 'parrot'], 'abc')
