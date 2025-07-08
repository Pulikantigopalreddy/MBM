class Father:
  def add(x, y):
    return x + y


class Mother(Father):
  def sub(x, y):
    return x - y

class Brother(Mother):
  def mul(x, y):
    return x * y

class Sister(Brother):
  def div(x, y):
    return x / y

inst_obj = Sister()
print(inst_obj.add(20, 30))
print(inst_obj.sub(30, 20))
print(inst_obj.mul(15, 15))
