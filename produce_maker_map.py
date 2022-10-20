import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1, 14, 3)
Y = np.arange(1, 10, 2)

makers = np.array('^ 3 P x _ v 2 p + | o 1 s H d , > 8 h D . < 4 * X'.split()).reshape(5, 5)

# makers
"""
array([['^', '3', 'P', 'x', '_'],
       ['v', '2', 'p', '+', '|'],
       ['o', '1', 's', 'H', 'd'],
       [',', '>', '8', 'h', 'D'],
       ['.', '<', '4', '*', 'X']], dtype='<U1')
"""

plt.xkcd() #cartonstyle
for i, h in enumerate(Y):
    for j in range(5):
        plt.scatter(X[j], h, s=100, marker=makers[i][j])
        plt.text(x=X[j]-0.9, y=h+0.35, s=f"maker = '{makers[i][j]}'", fontsize=10)
plt.axis('off')
plt.savefig('makerStyle.png', dpi=200)
plt.show()

