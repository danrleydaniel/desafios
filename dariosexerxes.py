import sys

dicio = {
  0: [1,2],
  1: [2,3],
  2: [3,4],
  3: [4,0],
  4: [0,1]
}

pontD = 0
pontX = 0

jogadas = int(input(""))

if ((jogadas % 2 == 0) or (jogadas > 999)):
  sys.exit()

while (jogadas > 0):
  d, x = input().split()
  d = int(d)
  x = int(x)
  #if(not ((0 <= d) or (x <= 4)) or (d != x)):
  #  sys.exit()
  
  if(d in dicio[x]):
    pontX += 1
  elif (x in dicio[d]):
    pontD += 1

  jogadas -= 1

if(pontX > pontD):
  print("xerxes")
else:
  print("dario")
