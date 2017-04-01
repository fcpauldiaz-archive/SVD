import numpy as np
import matplotlib.image as img
from matplotlib import pyplot as plt
from PIL import Image

#cargar una imagen de un archivo
def loadImage(nombreImage = 'leon.jpeg', mostrarImagen = True):
  img = Image.open(nombreImage)
  if (mostrarImagen == True):
    img.show()
  return img

#convertir una imagen
#a una matriz
def convertirImagen(imagen, mostrarImagen = False):
  #RGB
  #LA
  #CMYK
  #YCbCr
  #HSV
  imagen_gris = imagen.convert('LA')
  imagen_gris_matriz = np.array(list(imagen_gris.getdata(band=0)), float)
  imagen_gris_matriz.shape = imagen_gris.size[1], imagen_gris.size[0]
  imagen_matriz = np.matrix(imagen_gris_matriz)
  if (mostrarImagen == True): 
    plt.imshow(imagen_matriz, cmap='gray')
    plt.show()
  return imagen_matriz


def SVD(imagen_matriz):
  #SINGULAR VALUE DECOMPOSITION
  U_svd, sigma, V_svd = np.linalg.svd(imagen_matriz)
  n = 100 #Entre mayor n mayor es la resolucion
  frobenius = []
  for i in range(25, n+1, 5):
    #multiplicar la matriz U * D * V para reconstruir la matriz original
    #n decide la cantidad de elementos a obtener de las matrices.
    U =  np.matrix(U_svd[:, :i])
    D =  np.diag(sigma[:i]) #obtener solo la diagonal
    V =  np.matrix(V_svd[:i, :])
    imagen_reconstruida =  U*D*V 
    plt.imshow(imagen_reconstruida, cmap='gray')
    frob = (np.linalg.norm(imagen_matriz) - np.linalg.norm(imagen_reconstruida))
    titulo = "n = " + str(i) + " norma frobenius " + str(frob)
    frobenius.append(frob)
    plt.title(titulo)
    plt.show()
  x = range(len(frobenius))
  plt.plot(x, frobenius, 'ro')
  plt.show()


imagen = loadImage('leon.jpeg')
matriz = convertirImagen(imagen)
SVD(matriz)
