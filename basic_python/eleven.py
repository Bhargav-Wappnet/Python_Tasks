"""
Write a Python program to generate a 3*4*6 3D array whose each element is *
"""

array_3d = []
for i in range(3):
    array_2d = []
    for j in range(4):
        array_1d = []
        for k in range(6):
            array_1d.append('*')
        array_2d.append(array_1d)
    array_3d.append(array_2d)

print(array_3d)
