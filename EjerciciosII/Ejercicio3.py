from matplotlib import pyplot as plt
list_x = []
list_y = []

def retornar_escalarP(x0,y0,x1,y1,ix,iy):
  nx = x0 * x1 + (1 - x1) * (ix)
  ny = y0 * y1 + (1 - y1) * (iy)
  list_x.append(nx)
  list_y.append(ny)
  return nx,ny

def escalar(x, y, ex, ey):
  listax = x
  listay = y
  vix = listax[0]
  viy = listay[0]
  vx = ex
  vy = ey
  print('=Vector de Escalamiento es: (',vx,',',vy,')=')
  for v1,v2 in zip(listax,listay):
    print (v1,v2)
    print('el punto Escalado de:', '(',v1,',',v2,') es:',retornar_escalarP(v1,v2,vx,vy, vix, viy))
    
  plt.fill(list_x, list_y, color='purple', alpha=0.1)
  plt.fill(listax, listay, color='blue', alpha=0.1)
  plt.show()

escalar([1,3,5], [1,5,1], 3, 2)