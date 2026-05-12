import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    # Konstruktor: simpan learning rate dan max epoch
    def __init__(self, alpha=0.1, epoch=10):
        self.alpha = alpha
        self.epoch = epoch

    # Menghitung y_in atau net
    def weighted_sum(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    # Fungsi aktivasi Bipolar (Threshold 0)
    def predict(self, X):
        return np.where(self.weighted_sum(X) >= 0.0, 1, -1)

    # Fungsi visualisasi garis pemisah
    def plot_decision_boundary(self, X, t, epoch):
        plt.scatter(X[:, 0], X[:, 1], c=t.ravel(), marker='o', edgecolors='k', cmap=plt.cm.RdYlBu)
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        
        x_vals = np.linspace(x_min, x_max, 100)
        # Rumus garis pemisah dari bobot dan bias[cite: 6]
        y_vals = -(self.w_[0] + self.w_[1] * x_vals) / self.w_[2]
        
        plt.plot(x_vals, y_vals, 'b', label=f'Decision boundary (Epoch {epoch+1})')
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.title(f"Decision Boundary Pada Epoch {epoch+1}")
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.legend()
        plt.show()

    # Fungsi utama pelatihan (Training)[cite: 6]
    def fit(self, X, t):
        self.w_ = np.zeros(1 + X.shape[1]) # Inisialisasi bobot & bias = 0[cite: 6]
        
        with open("Hasil Perceptron.txt", "w") as f:
            f.write("Masalah OR dengan Perceptron\n---\n")
            
            for epoch in range(self.epoch):
                f.write(f"\nEpoch {epoch + 1}/{self.epoch}\n-----\n")
                errors = []
                
                for xi, target in zip(X, t):
                    y_pred = self.predict(xi)
                    error = target - y_pred
                    errors.append(error)
                    
                    # Update bobot & bias dengan Delta Rule[cite: 6]
                    update = self.alpha * error
                    self.w_[1:] += update * xi
                    self.w_[0] += update
                    
                    f.write(f"Input: {xi}, Target: {target}, Predict: {y_pred}, Error: {error}, Bobot: {self.w_[1:]}, Bias: {self.w_[0]}\n")
                
                self.plot_decision_boundary(X, t, epoch)
                sse = sum(np.array(errors)**2)
                f.write(f"Sum Square Error (SSE): {sse}\n")
                
                if sse == 0: # Berhenti jika error sudah nol[cite: 6]
                    f.write(f"\nPelatihan berhenti pada epoch ke-{epoch + 1} karena SSE mencapai target.")
                    break