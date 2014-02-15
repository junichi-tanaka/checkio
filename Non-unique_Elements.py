
def checkio(list):
  l = []
  for elem in list:
    if list.count(elem) > 1:
      l.append(elem)
  return l

def myassert(x, y):
  print(x)
  if x != y:
    raise

if __name__ == '__main__':
  myassert(checkio([1, 2, 3, 1, 3]), [1, 3, 1, 3])
  myassert(checkio([1, 2, 3, 4, 5]), [])
  myassert(checkio([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])
  myassert(checkio([10, 9, 10, 10, 9, 8]), [10, 9, 10, 10, 9])
