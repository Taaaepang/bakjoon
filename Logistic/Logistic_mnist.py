import numpy as np
import sys, os

sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from Logistic.Logistic_class import *
import matplotlib.pyplot as plt

mnist = load_mnist()
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True) # mnist 데이터 받기.

def weight_init(X, Y):
    '''weight 초기화 함수'''
    weight = np.random.rand(X.shape[1], Y.shape[1])     # (bias term + feature수) x (class의 개수 종류 수)크기의 배열에
    return weight                                       # 정규분포된 난수를 각각 초기화한다.

def one_hot_encoding(Y):                                # class는 0, 1, 2 등 class에 해당되는 숫자로 표현되어있다.
    num = np.unique(Y, axis=0)                          # data의 해당되는 class가 들어있는 y를 input으로 받아.
    num = np.eye(num.shape[0])[Y]                       # 공통되는 것을 다 추려 unique하게 class를 분별하여,
    return num                                          # 0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] 처럼 변환된다.
                                                        # 모든 class에 대해 변환한다.

def Bias_term(X):                                       # Logistic Regression을 사용하려면 데이터 feature에서
    list1 = [0] * X.shape[0]                            # 제일 앞에 bias term 1을 줘야한다.
    for i in range(X.shape[0]):                         # 모든 데이터에 대해 배열 앞에 bias term을 추가한다.
        list1[i] = np.insert(X[i], 0, 1)
    return np.array(list1)

idx = input("Single or Multi ?= ")                      # keyboard 로 부터 class 식별방식,
learning_rate = float(input("learning rate ?= "))       # learning rate, epoch 를 받는다.
epoch = int(input("epoch ?= "))
cost = list()

T_train = one_hot_encoding(t_train)                     # 각 데이터 셋에 대한 bias term추가, weight 초기값 생성,
X_train = Bias_term(x_train)                            # one hot encoding을 한다.
weight = weight_init(X_train, T_train)
X_test = Bias_term(x_test)
T_test = one_hot_encoding(t_test)

if idx == "single" or idx == "Single":
    # single class 식별.
    select = int(input("class(0~9) == "))               # 어떤 class를 식별할지 입력받는다.
    # 학습과, 손실 함수 계산을 위한 train 데이터 셋, 선택한 class에 실제 y값, 선택한 class에 해당되는 weight 값,
    # learning rate 및 분기를 위한 idx를 매개변수로한 Logistic_single 객체를 생성.
    Logistic_single = Logistic_regression(X_train, T_train[:, select], weight[:, select], learning_rate, idx)
    for i in range(epoch):                              # epoch만큼 학습 반복 및 손실 값 출력.
        Logistic_single.learn()
        cost.append(Logistic_single.cost_function())    # 그래프를 그리기위해 손실값을 리스트에 삽입.
        print("epoch = ", i+1, "cost = ", cost[i])
    T_test = T_test[:, select]
    print("class = ", select)
    Logistic_single.predict(X_test, T_test)             # test 데이터 셋과, 선택한 class의 실제 y값을 매개변수로 하여,
                                                        # 계산된 Hypothesis와 실제 class값을 비교하여 정확도를 출력.

elif idx == "Multi" or idx == "multi":
    # Multi class 식별
    # 학습과, 손실 함수 계산을 위한 train 데이터 셋, 선택한 class에 실제 y값, 선택한 class에 해당되는 weight 값,
    # learning rate를 매개변수로 Logistic_multi 객체를 생성.
    Logistic_multi = Logistic_regression(X_train, T_train, weight, learning_rate)
    for i in range(epoch):                              # epoch만큼 학습 반복 및 손실 값 출력.
        Logistic_multi.learn()
        cost.append(Logistic_multi.cost_function())     # 그래프를 그리기위해 손실값을 리스트에 삽입.
        print("epoch = ", i+1, "cost = ", cost[i])
    Logistic_multi.predict(X_test, T_test)          # test 데이터 셋과, class의 실제 y값을 매개변수로 하여,
                                                    # 계산된 Hypothesis와 모든 실제 class값을 비교하여 정확도를 출력.
plt.xlabel("Iteration")
plt.ylabel("Cost")

plt.plot(range(epoch), cost)                        # x축은 epoch, y축은 cost 변화를 그래프로 출력한다.
plt.show()
