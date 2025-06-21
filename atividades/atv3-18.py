import numpy as np

# You are given the following kernel and image:
w = np.array([[1,2,1],[2,4,2],[1,2,1]])
print(f"Kernel:\n{w}\n")
#print(f"Kernel shape:{w.shape}")

f = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
print(f"Image:\n{f}\n")
#print(f"Image shape:{f.shape}")

'''
(a) Give a sketch of the area encircled by the large ellipse in Fig. 3.28 
when the kernel is centred at point (2,3) (2nd row, 3rd col) of the image
shown above. Show specific values of w and f. 
'''
specific_f = f[0:3, 1:4]
print(f"Specific values of f:\n{specific_f}\n")

'''
(b) Compute the convolution w★f using the minimum zero padding needed.
Show the details of your computations when the kernel is centered on point
(2,3) of f; and then show the final convolution result.
'''
pad_f = np.pad(f, pad_width=1, mode='edge')
print(f"Image after padding:\n{pad_f}\n")
#print(f"Image shape:{pad_f.shape}")

def convolution(kernel, centered_image):
    # Kernel in 180°
    flips_cols = np.flip(kernel, axis=1)
    new_kernel = flips_cols[::-1]

    multi = new_kernel * centered_image
    sum_pixels = 0
    for row in multi:
        for element in row:
            sum_pixels += element
    return sum_pixels


print(f"Value of convolution when the kernel is centered on point(2,3): {convolution(w, specific_f)}")

'''
Repeat (b), but for the correlation, w ☆ f
'''
def correlation(kernel, centered_image):
    multi = kernel * centered_image
    sum_pixels = 0
    for row in multi:
        for element in row:
            sum_pixels += element
    return sum_pixels

print(f"Value of correlation when the kernel is centered on point(2,3): {correlation(w, specific_f)}")