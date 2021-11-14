from random import randint

k = int(input())

lists = [sorted([randint(0, 20) for i in range(randint(1, 3))]) for j in range(k)]

def merge(*lists):
  lists = lists[0]
  new_list = []
  for element in lists:
    new_list += element
  return sorted(new_list)

print(merge(lists))
