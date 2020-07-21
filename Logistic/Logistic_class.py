import numpy as np
import math as m
import sys

def sigmoid(x):
    """ Sigmoid 함수 정의. """
    return 1 / (1 + np.exp(-x))

class Logistic_regression:
    """ Logistic Regression class 정의 """
    def __init__(self, X, y, w, lr, single=None):
        self.X = X                      # Train input 데이터 셋 m x n(데이터 수 x (bias term + feature))
        self.y = y                      # Train 데이터의 해당 되는 실제 class 셋 m x t(데이터수 x class 종류 수)
        self.w = w                      # Theta 가중치 n x t. (n : feature 수, t : class 종류 수)
        self.num_feature = X.shape[1]   # 하나의 Train 데이터의 차수 크기.
        self.num_data = X.shape[0]      # Train input 데이터 셋의 크기
        self.lr = lr                    # input learning rate 값
        self.hwx = np.array(list())     # Hypothesis 함수 output
        self.condition = single         # single class 일 경우 분기 조건으로 사용.


    def cost_function(self):
        ''' 손실 함수 정의 '''
        hwx = self.hwx + 1e-7           # 계산한 Hypothesis 값이 0으로 수렴하는 경우
        r_hwx = (1 - self.hwx) + 1e-7   # log0 연산을 못하기 때문에 작은 수를 더해준다.

        # 손실 함수 정의
        # - (1 / 데이터 수)
        # x ((실제 데이터에 대한 class 값 x log_10 (계산한 hypothesis 함수 값) => 백터 연산을 이용하여 한번에 구함.
        # + (1 - 실제 데이터에 대한 class 값) x log_10(1 - 계산한 hypothesis 함수 값)) => 백터 연산.
        # 백터 연산을 하면 각 데이터 마다 연산이 완료된 행렬형태로 되있으므로,
        # 처음 데이터 부터 마지막 데이터까지 계산 한 값의 합을 구해야한다.
        # 행 마다 더하면 되므로, numpy.sum 함수를 사용하여 행끼리 더할 수 있도록 axis=0을 지정한다.
        cost = -(1/self.num_data)*np.sum((self.y*np.log10(hwx) + (1 - self.y)*np.log10(r_hwx))
                                         , axis=0)
        return cost         # epoch 마다 theta(weight)에 대한 손실 함수 J(theta)를 반환한다.
    def learn(self):
        """ Gradient descent 방식을 사용하여 가중치 theta 를 수정한다. """
        wx = np.dot(self.X, self.w)                 # Train 데이터 셋 (bias term + feature)들과
                                                    # 웨이트(w0~w5)를 행렬 곱셈한다.
                                                    # numpy.dot 함수를 사용하여 single(5x1), multi(5x(3or10))
                                                    # 경우의 상관없이 한번에 행렬 곱셈 값을 구한다.
                                                    # 데이터 수 x class 종류 수에 모양을 가진 행렬을 반환한다.

        eMin = -np.log(np.finfo(type(0.1)).max)     # epoch 마다 수정된 가중치 마다 Hypothesis 계산을 한다.
        zSafe = np.array(np.maximum(wx, eMin))      # 앞에서 구한 행렬 곱셈 값이 sigmoid 함수 에서 지수연산으로
        self.hwx = sigmoid(zSafe)                   # 시스템에서 나타낼 수 있는 수보다 큰 수가 나올 수 있는,
                                                    # overflow가 발생할 수 있으므로, numpy의 finfo().max를 통해
                                                    # float 값의 최대 값을 자연로그를 취하면 약 709가 나온다
                                                    # 음수화를 한 후, 계산 한 Hypothesis 값과 행렬 비교하여 큰 수를
                                                    # sigmoid 함수에 input 하여 overflow를 방지한다.

        self.w = self.w - ((self.lr / self.num_data) * np.dot(np.transpose(self.X), self.hwx - self.y))
        # Gradient descent 정의. (j: 0 ~ bias term + feature) => 백터연산을 통해 모든 번째의 가중치를 한번에 구함.
        # 수정된 j번째 가중치 = 현재 j번째 가중치 - (learning rate / 데이터의 수)
        # x (각 데이터의 계산된 hwx - 각 데이터의 실제 y값)을 모든 데이터에 대해 더한 값.
        # x 입력된 train 데이터의 j 번째 모든 bias term 또는 feature 들.
        # 전치를 통해 계산 순서를 바꿔서 한번에 계산.

        '''
        np.dot(np.transpose(self.X), self.hwx - self.y)의 예시 Iris multi class 식별상황.
        입력 된 train 데이터 셋 (d1 = 첫번째 입력 train 데이터)         class 0 1 2 
       d1 |x0 x1 x2 x3 x4|                   |x0 x0  ....               |y1 y1 y1|
       d2 |x0 x1 x2 x3 x4|                   |x1 x1  ....               |y2 y2 y2|
       d3 |x0 x1 x2 x3 x4|     => 전치 =>    |x2 x2  ....               |y3 y3 y3|            
       d4 |x0 x1 x2 x3 x4|                   |x3 x3  ....               |y4 y4 y4|
       d5 |x0 x1 x2 x3 x4|                   |x4 x4  ....               |y5 y5 y4|
       ......
        d1 d2  ......         Hypothesis 계산 값 - 실제 y값
                              (hwx1 : 첫번째 데이터에 대한 각 class의 종류 수에 해당되는 계산 된 값들)  
       |x0 x0  ......         |h1-y1 h2-y2 h3-y3| hwx1      |(h1-y1)x0 +..., (h2-y2)x0 +..., (h3-y3)x0 +...|       
       |x1 x1  ......         |h1-y1 h2-y2 h3-y3| hwx2      |(y1-y1)x1 +..., (h2-y2)x1 +..., (h3-y3)x1 +...|
       |x2 x2  ......     X   |h1-y1 h2-y2 h3-y3| hwx3    =>|(h1-y1)x2 +..., (h2-y2)x2 +..., (h3-y3)x2 +...|    
       |x3 x3  ......         |h1-y1 h2-y2 h3-y3| hwx4      |(h1-y1)x3 +..., (h2-y2)x3 +..., (h3-y3)x3 +...|   
       |x4 x4  ......         |h1-y1 h2-y2 h3-y3| hwx5      |(h1-y1)x4 +..., (h2-y2)x4 +..., (h3-y3)x4 +...|   
                               ......                       ... : 앞을 포함하여 m번 덧셈 (데이터 수)
        
        실제 구하는 값
        i번째 데이터의 hypothesis 값 - i번째 데이터의 해당되는 실제 class 값(multi) x i번째 데이터 값의 j번째 feature.
        = (hwxi's h1 - di's y) * di's xj
        에 대해 (i : 0 ~ m(데이터 수))모든 데이터의 대한 위의 값을 더하면
        = ((hwx1's h1 - d1's y) x d1's xj) + ((hwx2's h1 - d2's y) x d2's xj)+...+((hwxm's h1 - dm's y) x dm's xj)
        가 되고 이것을 모든 j에 대해 연산을 하면 위에 식과 같아지게 되며 가중치 weight와 같은 크기의 행렬이 된다.
        
        백터 연산을 통해 한번에 가중치를 수정한다.
        '''

    def predict(self, x_test, y_test):
        """ 실제 class값과 학습된 weight를 이용한 hypothesis 계산값과 비교한다."""
        wx = np.dot(x_test, self.w)
        eMin = -np.log(np.finfo(type(0.1)).max)
        zSafe = np.array(np.maximum(wx, eMin))
        hwx = np.array(sigmoid(zSafe))              # Test_set과 학습된 가중치(theta)에 대한 Hypothesis 계산

        if self.condition:                          # single class일 경우 분기
            for i in range(hwx.shape[0]):           # 계산된 Hypothesis가 0.5초과 이면 1, 이하면 0으로 바꾼다.
                if hwx[i] > 0.5:
                    hwx[i] = 1
                else:
                    hwx[i] = 0
        else:                                       # multi class일 경우 분기.
            for i in hwx:
                for j in range(hwx.shape[1]):
                    if i[j] > 0.5:
                        i[j] = 1
                    else:
                        i[j] = 0
        accuracy = 0
        arr = hwx == y_test
        for i in arr:
            if i.all() == True:     # Numpy 행렬 연산을 통해 비교를 해서 한 행이 같을 경우,
                accuracy += 1       # 즉 계산된 Hypothesis 와 실제 y가 같을 경우 정확도 변수를 1증가 합니다.
        print("accuracy = ", accuracy / x_test.shape[0])    # 맞춘 횟수 / 테스트 데이터 셋 크기 => 정확도.






