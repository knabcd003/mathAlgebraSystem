

from math import factorial
import xdrlib

compare_list_sin = []
def sin_func(x):
  n = 0
  func = 0
  while True:
    func += (((-1)**n)*(x**((2*n) + 1)))/factorial((2*n) + 1)
    compare_list_sin.append(func)
    n += 1
    if len(compare_list_sin) == 2:
      if compare_list_sin[0] == compare_list_sin[1]:
        return compare_list_sin[1]
        break
      else:
        compare_list_sin.pop(0)

compare_list_cos = []
def cos_func(x):
  n = 0
  func = 0
  while True:
    func += (((-1)**n)*(x**((2*n))))/factorial((2*n))
    compare_list_cos.append(func)
    n += 1
    if len(compare_list_cos) == 2:
      if compare_list_cos[0] == compare_list_cos[1]:
        return compare_list_cos[1]
        break
      else:
        compare_list_cos.pop(0)

compare_list_exp = []
def exp_func(x):
  n = 0
  func = 0
  while True:
    func += ((x**((n))))/factorial((n))
    compare_list_exp.append(func)
    n += 1
    if len(compare_list_exp) == 2:
      if compare_list_exp[0] == compare_list_exp[1]:
        return compare_list_exp[1]
        break
      else:
        compare_list_exp.pop(0)

cos_func(2)

g = input("degrees or radians: ")
x = int(input("What is your value: "))
if g[0].lower() == "d":
  x = (x * (3.14159))/(180)
print(x)