import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])
Xb = np.hstack([np.ones((X.shape[0],1)),X])
w = np.zeros(Xb.shape[1])
eta = 0.1
epochs = 10

for epoch in range(epochs):
    for xi,target in zip(Xb,y):
        output = 1 if np.dot(w,xi) >= 0 else 0
        error = target - output
        w += eta * error * xi

def predict(x):
    xb = np.hstack([1,x])
    return 1 if np.dot(w,xb) >= 0 else 0

print("Final Weights:",w)
print("x1 x2 | y_pred")
for xi in X:
    print(f"{xi[0]}  {xi[1]}  |   {predict(xi)}")
