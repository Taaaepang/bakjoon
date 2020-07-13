import numpy as np
from sklearn.datasets import load_iris
from Class_KNN import KNN


iris = load_iris()

X = iris.data
y = iris.target
y_name = iris.target_names

l = 15
for_test = np.array([(i%l==(l-1)) for i in range(y.shape[0])])
for_train = ~for_test
X_train = X[for_train]
Y_train = y[for_train]
X_test = X[for_test]    # train data(0~13, 15~28,30~43,45~58,60~73,75~88,90~103,105~118,120~133,135~148
Y_test = y[for_test]    # test data(14,29,44,59,74,89,104,119,134)

K = int(input("K = "))  # K를 키보드로 입력 받는다.

nn = KNN(K, X_train, Y_train, y_name)   # KNN 객체 선언
# 모든 test_feature에 대한 weight_majority_vote, majority_vote를 구해서 리스트에 저장.
weight_majority_vote = []
majority_vote = []

for i in range(Y_test.shape[0]): #test_feature 개수 만큼 반복.
    W_name, M_name = nn.Obtain_K_Nearest_Neighbor(X_test[i])
    weight_majority_vote.append(W_name)
    majority_vote.append(M_name)
    # weight_majority_vote, majority_vote를 구해서 리스트에 저장.
print("--------------------Majority Vote-------------------")
for i in range(len(majority_vote)):
    print('Test Data index: ', i, 'computed class: ', majority_vote[i], "True class: ", y_name[Y_test[i]])
print("---------------Weighted Majority Vote---------------")
for i in range(len(weight_majority_vote)):
    print('Test Data index: ', i, 'computed class: ', weight_majority_vote[i], "True class: ", y_name[Y_test[i]])
# majority_vote, weight_majority_vote를 출력.