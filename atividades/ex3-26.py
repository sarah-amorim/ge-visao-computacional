import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plotar_histograma(img, titulo = 'Histograma'):
    frequencias, bins = np.histogram(img, bins=256, range=(0, 256))
    plt.figure(figsize=(10, 5))
    plt.plot(bins[:-1], frequencias, color='red')
    plt.title(titulo)
    plt.xlabel("Intensidade")
    plt.ylabel("Número de pixels")
    plt.grid(True)
    plt.show()

# The two images shown in the following figure are quite different, but their histograms are the same. Suppose that each image is blurred using a 3x3 box kernel.

img_chess = cv.imread('chessboard.jpg', cv.IMREAD_GRAYSCALE)
img_blackwhite = cv.imread('blackwhite.jpeg', cv.IMREAD_GRAYSCALE)
#plotar_histograma(img_chess, 'Chessboard image before blur')
#plotar_histograma(img_blackwhite, 'Black and white image before blur')

'''
(a) Would the histograms of the blurred images still be equal? Explain
Não, os histogramas não serão iguais. Quando o blur for aplicado, as transições entre preto e branco vão ser 
substituídas por mais valores de intensidade de cinza. Isso vai gerar uma alteração no histograma. 
'''

'''
(b) If your answer is no, either sketch the two histograms or give two tables detailing the histogram components
É possível perceber que a diferença entre os histogramas é mínima. Mas a imagem quadriculada apresentou mais variaçẽes.
'''
img_chess_blur = cv.blur(img_chess, (3,3))
img_blackwhite_blur = cv.blur(img_blackwhite, (3,3))
#plotar_histograma(img_chess_blur, 'Chessboard image after blur')
#plotar_histograma(img_blackwhite_blur, 'Black and white image after blur')