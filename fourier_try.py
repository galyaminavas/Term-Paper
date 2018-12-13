import numpy as np
from PIL import Image, ImageOps
from scipy.fftpack import rfft
import os

list_of_files = os.listdir('sphere_png')
sorted(list_of_files)

big_vector = []
input_vector_file = open('in.txt', 'w')
i = 1
for file in list_of_files:
    img = Image.open('sphere_png\\' + file)
    img_gray = ImageOps.grayscale(img)
    fit = ImageOps.fit(image=img_gray, size=(20, 20), method=0, bleed=0.0, centering=(0.5, 0.5))
    arr = np.array(fit)
    big_vector.append(arr)
    print('{} picture, file: {}'.format(i, file), file=input_vector_file)
    for input_elem in arr:
        print(input_elem, file=input_vector_file)
    i += 1
input_vector_file.close()

after_transform = rfft(big_vector)
output_vector_file = open('out.txt', 'w')
j = 1
for out_elem in after_transform:
    print('{} element'.format(j), file=output_vector_file)
    print(out_elem, file=output_vector_file)
    j += 1
output_vector_file.close()
