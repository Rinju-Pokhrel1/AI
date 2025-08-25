import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(1)
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

w1 = np.random.uniform(-1,1,(input_neurons,hidden_neurons))
w2 = np.random.uniform(-1,1,(hidden_neurons,output_neurons))
b1 = np.zeros((1,hidden_neurons))
b2 = np.zeros((1,output_neurons))

lr = 0.5
epochs = 10000

for epoch in range(epochs):
    hidden_input = np.dot(X,w1)+b1
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output,w2)+b2
    final_output = sigmoid(final_input)

    error = y - final_output
    d_output = error * sigmoid_derivative(final_output)
    error_hidden = d_output.dot(w2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    w2 += hidden_output.T.dot(d_output)*lr
    b2 += np.sum(d_output,axis=0,keepdims=True)*lr
    w1 += X.T.dot(d_hidden)*lr
    b1 += np.sum(d_hidden,axis=0,keepdims=True)*lr

print("Final Output:")
print(final_output.round(3))
