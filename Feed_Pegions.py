
def checkio(n):
  r = []
  i = 1
  while n > 0:
    x = sum(range(1, i))
    if n < x:
      x = n
    n -= x
    r += [x]
    i += 1
  return max(r)

if __name__ == '__main__':
  assert checkio(1) == 1
  assert checkio(2) == 1
  assert checkio(3) == 2
  assert checkio(5) == 3
  assert checkio(10) == 6
