import numpy as np
import Perceptron as p

# Inisialisasi input dan target Bipolar sesuai tabel Hal. 55[cite: 6]
X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
t = np.array([1, 1, 1, -1])

# Jalankan model dengan alpha 0.1 dan epoch 10[cite: 6]
model = p.Perceptron(alpha=0.1, epoch=10)
model.fit(X, t)