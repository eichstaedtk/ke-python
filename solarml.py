import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def predict(X, w, b):
    return X * w + b


def loss(X, Y, w, b):
    return np.average((predict(X, w, b) - Y) ** 2)


def train(X, Y, iterations, lr):
    w = b = 0
    for i in range(iterations):
        current_loss = loss(X, Y, w, b)
        print("Iteration %4d => Loss: %.6f" % (i, current_loss))

        if loss(X, Y, w + lr, b) < current_loss:
            w += lr
        elif loss(X, Y, w - lr, b) < current_loss:
            w -= lr
        elif loss(X, Y, w, b + lr) < current_loss:
            b += lr
        elif loss(X, Y, w, b - lr) < current_loss:
            b -= lr
        else:
            return w, b

    raise Exception("Couldn't converge within %d iterations" % iterations)


def graph(x, y, xnew, ypredict):
    sns.set()

    plt.axis([0, 15, 0, 70])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel('Sonnenstunden', fontsize=30)
    plt.ylabel('KW', fontsize=30)

    plt.plot(x, y, "bo")
    plt.plot(xnew, ypredict, "r-")
    plt.show()


X, Y = np.loadtxt("solar.txt", skiprows=1, unpack=True)

X_new = np.array([9.4, 0.5, 8, 6, 14])
Y_Predict = predict(X_new, 3.630, 13.110)


graph(X, Y, X_new, Y_Predict)

w, b = train(X, Y, iterations=10000, lr=0.01)
print("\nw=%.3f, b=%.3f" % (w, b))

# Predict the number of pizzas
print("Prediction: x=%d => y=%.2f" % (9, predict(9, w, b)))
