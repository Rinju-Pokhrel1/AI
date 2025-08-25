import numpy as np


X = np.array([
    [-1, -1],
    [-1,  1],
    [ 1, -1],
    [ 1,  1],
], dtype=float)

y = np.array([-1, -1, -1, 1], dtype=float)  

Xb = np.hstack([np.ones((X.shape[0], 1)), X])


eta = 1.0
w = np.zeros(Xb.shape[1], dtype=float)
for xi, ti in zip(Xb, y):
    w += eta * ti * xi

def predict(x):
    xb = np.hstack([1.0, x])
    return 1 if np.dot(w, xb) >= 0 else -1

# Test and display as standard 0/1 for clarity
def bipolar_to_binary(b): return 1 if b == 1 else 0

print("Weights (bias, w1, w2):", w)
print("\nTruth table learned by Hebbian AND:")
print("x1 x2 | y_pred")
for xi, ti in zip(X, y):
    y_hat = predict(xi)
    print(f"{bipolar_to_binary(int((xi[0]+1)/2))}  {bipolar_to_binary(int((xi[1]+1)/2))}  |  {bipolar_to_binary(y_hat)}")
