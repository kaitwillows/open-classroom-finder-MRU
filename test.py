x = 0

def myfunc():
  print(x)

myfunc()


y = 0
def kys():
    local_y = y
    print(local_y)
    local_y = local_y + 1
    y = local_y
kys()

print(y)
