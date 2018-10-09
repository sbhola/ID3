import ID3

data1 = [
  dict(a= 1, b= 0, c= 1, Class= 'B'),
  dict(a= 0, b= 1, c= 0, Class= 'A'),
  dict(a= 1, b= 1, c= 1, Class= 'A'),
  dict(a= 1, b= 1, c= 0, Class= 'B'),
  dict(a= 0, b= 1, c= 1, Class= 'A')
]

data2 = [
  dict(a= 1, b= 0, c= 1, Class= 'A'),
  dict(a= 0, b= 1, c= 0, Class= 'A'),
  dict(a= 1, b= 1, c= 1, Class= 'A'),
  dict(a= 1, b= 1, c= 0, Class= 'A'),
  dict(a= 0, b= 1, c= 1, Class= 'A')
]

data3 = [
  dict(a= 0, b= 1, c= 0, Class= 1),
  dict(a= 1, b= 1, c= 1, Class= 1),
  dict(a= 1, b= 1, c= 0, Class= 0),
  dict(a= 1, b= 0, c= 1, Class= 0),
  dict(a= 0, b= 1, c= 1, Class= 1)
]


data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]
tree = ID3.ID3(data, 0)
if tree != None:
  ans = ID3.evaluate(tree, dict(a=1, b=0))
  if ans != 1:
    print("ID3 test failed.")
  else:
    print("ID3 test succeeded.")
else:
  print("ID3 test failed -- no tree returned")
