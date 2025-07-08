class Father:
  def add(self, x, y):
    return x + y


class Mother(Father):
  def sub(self, x, y):
    return x - y

class Brother(Mother):
  def mul(self, x, y):
    return x * y

class Sister(Brother):
  def div(self, x, y):
    return x / y

inst_obj = Sister()
print(inst_obj.add(20, 30))
print(inst_obj.sub(30, 20))
print(inst_obj.mul(15, 15))


print("hello")
