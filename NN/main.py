import numpy as np
from sklearn.datasets import load_iris
from NNclass import *
import matplotlib.pyplot as plt
def one_hot_encoding(Y):
    num = np.unique(Y, axis=0)
    num = np.eye(num.shape[0])[Y]
    return num

iris = load_iris()
X, y, y_name = iris.data, iris.target, iris.target_names

# epoch, learning rate, hidden layer node 수, batch_size를 키보드로부터 입력을 받는다.
epoch, lr, hidden, batch_size = input("epoch, lr, hidden, batch_size(ex 300 0.01 5 10) = ").split()
epoch, lr, hidden, batch_size = int(epoch), float(lr), int(hidden), int(batch_size)

# Neural_Network에 대한 객체 생성 및 Iris 데이터 초기화.
iris_NN = Neural_Network(4, hidden, 3)
iris_NN.X = X
iris_NN.y = y

iris_NN.learn(lr, epoch, batch_size)    # epoch만큼 각각 batch_size만큼 랜덤 batch된 train_set에 대한 학습시작.

plot = np.array(iris_NN.train_loss)
plot1 = np.array(iris_NN.train_accuracy)
mask = np.random.choice(X.shape[0], 30)     # 30개의 test_set을 분할.
X = X[mask]
y = one_hot_encoding(y[mask])

accuracy = iris_NN.accuracy(X, y)           # test_set에 대한 정확도 측정.
print("Test accuracy = ", accuracy)

# train_set에 대한 손실 값과 정확도 그래프 출력.
plt.plot(range(epoch), plot, 'r', label='cost')
plt.plot(range(epoch), plot1, 'b', label='accuracy')
plt.legend(loc='center right')
plt.show()

