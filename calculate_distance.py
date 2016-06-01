import re
import math

def distance(lstA,lstB):

    coordA = [float(x) for x in lstA]
    coordB = [float(x) for x in lstB]

    d = math.sqrt((coordB[0]-coordA[0])**2 +(coordB[1]-coordA[1])**2 )
    return d

with open('test.txt','r') as file:
  cont = 1
  for row in file:
    result = re.match(r'^(\d+[.]?\d+)(\s)(\d+[.]?\d+)',row)

    if (cont == 1):
      coordA = [result.group(1),result.group(3)]
    else:
      coordB = [result.group(1),result.group(3)]

    if (cont == 2):
      print(distance(coordA,coordB))
      cont=1
    else:
      cont +=1
