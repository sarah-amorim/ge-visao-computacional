# Replicando a sequência algorítmica da imagem 3.37

img = cv.imread('imagens/img3-37.jpeg')

blur_85 = cv.GaussianBlur(img, (85,85), 7)
blur_43 = cv.GaussianBlur(img, (43,43), 7)

diff = cv.subtract(blur_85, blur_43)

cv.imshow('difference', diff)
cv.waitKey(0)
cv.destroyAllWindows()