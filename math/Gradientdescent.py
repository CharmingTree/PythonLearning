import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(100)
x2 = np.random.rand(100)
y = 0.2 * x * 0.5 # 임의

def plot_prediction(pred, Y):
    plt.figure(figsize=(8,6))
    plt.scatter(x,Y)
    plt.scatter(x,pred)
    plt.show()

## Gradient Descecnt imp

w = np.random.uniform(-1,1)
w2 = np.random.uniform(-1, 1)
b = np.random.uniform(-1, 1)

learning_rate = 0.7

for epoch in range(200):
    y_Pred = w * x + w2 * x2 + b

    error = np.abs(y_Pred - y).mean()

    if error < 0.001:
        break

    # gradient descent computing
    w_grad = learning_rate * ((y_Pred - y) * x).mean()
    w2_grad = learning_rate * ((y_Pred -y) * x).mean()
    b_grad = learning_rate * ((y_Pred - y)).mean()

    # w,b 값 갱신
    w = w - w_grad
    w2 = w2 - w2_grad
    b = b - b_grad
 
    if epoch % 10 == 0:
        y_Pred = w * x + w2 * x2 + b
        plot_prediction(y_Pred, y)
