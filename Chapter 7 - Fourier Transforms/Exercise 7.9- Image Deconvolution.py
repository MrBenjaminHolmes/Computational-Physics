import numpy as np
import matplotlib.pyplot as plt

sigma = 25
E = 1e-3
imageRaw = np.loadtxt("Resources/blur.txt", float)

plt.imshow(imageRaw, cmap="gray")
plt.show()

guassBlur = np.zeros_like(imageRaw)
rows, columns = guassBlur.shape

def blurFunc(x,y):
    return np.exp(-((x**2)+(y**2))/(2*(sigma**2)))

for x in range(rows):
    for y in range(columns):

        if x > rows // 2:
            x_coord = x - rows
        else:
            x_coord = x

        if y > columns // 2:
            y_coord = y - columns
        else:
            y_coord = y

        guassBlur[x, y] = blurFunc(x_coord, y_coord)

plt.imshow(guassBlur, cmap="gray")
plt.show()

FTrawImage = np.fft.rfft2(imageRaw)
FTblur = np.fft.rfft2(guassBlur)

error = 1e-3

FTrawImage = np.fft.rfft2(imageRaw)
FTblur = np.fft.rfft2(guassBlur)

InverseFT = np.zeros_like(FTrawImage)

np.divide(
    FTrawImage,
    FTblur,
    out=InverseFT,
    where=np.abs(FTblur) >= error
)

Inverse = np.fft.irfft2(InverseFT)

plt.imshow(Inverse, cmap="gray")
plt.show()