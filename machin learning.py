import os
import numpy as np

def create_learning_data(file_name):
  f = open(file_name, "w")
  f.write("x,y,z\n")

  np.random.seed(30)
  x = 50 * np.random.rand(100)
  y = 50 * np.random.rand(100)
  z = 3*x + 2*y + 4 + np.random.randn(100)

  for v1, v2, v3 in zip(x, y, z):
	  f.write(str(v1) + "," + str(v2) + "," + str(v3) + "\n")
  f.close()

create_learning_data("sample1")

# 가상 학습 데이터 생성

from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, n_classes=3)

plt.scatter(X[:,0], X[:,1], marker='o', c = y, s=100)
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

# 가상 학습 데이터 생성 2
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

X, y = make_regression(n_samples=200, n_features=2, n_informative=2)

plt.scatter(X[:,0], X[:,1], marker='o', c = y, s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 가상 학습 데이터 생성 3

from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

X, y, c = make_regression(n_samples=200, n_features=2, n_informative=2, coef=True)

plt.scatter(X[:,0], X[:,1], marker='o', c = y, s=100)
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
print(c)
