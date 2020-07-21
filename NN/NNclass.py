import numpy as np

def softmax(x):
    """vector의 합이 1이되게 비율을 조정."""
    exp_a = np.exp(x-np.max(x, axis=0))     # 기존의 softmax는 하나의 결과에 대한 계산만 가능했으므로,
    sum_exp_a = np.sum(exp_a, axis=1)       # 계산 값이 행렬로 들어오는 것에 대한 코드를 수정했습니다.
    for i in range(exp_a.shape[0]):
        exp_a[i] = exp_a[i] / sum_exp_a[i]
    return exp_a

def sigmoid(x):
    """ sigmoid 함수 정의. """
    return 1 / (1 + np.exp(-x))

def cross_entropy_error(y, t):
    """ 교차 엔트로피 손실 값 계산. one hot encoding 필수."""
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        epsilon = 1e-7 # 작은값 # log(x)에서 x 값이 0이되지않게 더해준다.
    batch_size = y.shape[0] # 여러 데이터에 대한 계산된 값이 행렬로 들어 있으므로 평균을 구하기 위해 사용한다.
    return -np.sum(t*np.log(y+1e-7)) / batch_size  # 실제 class 값(t)가 1인 것에 대한 y의 값에 대한 평균을 구한다.
                                                   # 만약 y = 1 (예측이 매우잘됨) 이면 cost가 0이므로, 오차가
                                                   # 거의 없다는 것이다.
                                                   # y의 데이터 셋들은 합이 1이므로 -log_e(x) 식에서 x가 1에서
                                                   # 멀어지면, 즉 실제 값이 1인 인덱스의 값이 1에서 멀어지면
                                                   # cost가 급증하게 된다.

def one_hot_encoding(Y):
    """one hot encoding 함수"""
    num = np.unique(Y, axis=0)
    num = np.eye(num.shape[0])[Y]
    return num

class Neural_Network():
    """1개의 neural network."""
    def __init__(self, input_size, hidden_size, output_size):
        """ weight, bias term init."""
        self.params = {}
        # W1 : Input -> Hidden layer.
        # b1 : Input layer's bias term.
        self.params['W1'] = np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.random.randn(hidden_size)
        # W2 : Hidden layer -> Output layer
        # b2 : Hidden layer's bias term.
        self.params['W2'] = np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.random.randn(output_size)

        self.input_size = input_size            # input data의 feature 수.
        self.output_size = output_size          # output data의 class 수.
        self.X = np.array(list())               # train_set을 저장해 둠.
        self.y = np.array(list())               # train_set에 해당되는 class값을 저장해둠.
        self.train_loss = []                    # 학습과정에서 손실값의 추이를 확인하기 위해 선언.
        self.train_accuracy = []                # 학습과정에서 정확도의 추이를 확인하기 위해 선언.

    def predict(self, x):
        """주어진 input x로 W1, b1, W2, b2를 이용하여 output 값 계산."""
        # Input layer -> Hidden layer.
        z2 = np.dot(x, self.params['W1']) + self.params['b1']
        a2 = sigmoid(z2)
        # Hidden layer --> Output layer.
        z3 = np.dot(a2, self.params['W2']) + self.params['b2']
        y = softmax(z3)         # 각 데이터에 대한 계산된 output값의 합이 1이 되게 비율 조정.
        return y


    def loss(self, x, t):
        """ 교차 엔트로피 에러를 통해 실제 y값에 대한 오차를 구한다."""
        z = self.predict(x)
        loss = cross_entropy_error(z, t)
        return loss

    def accuracy(self, x, t):
        """batch된 train_set을 학습시키고, train_set과의 정확도 측정, test_set과의 정확도를 측정한다."""
        accuracy = 0.0
        y = self.predict(x)
        for i in range(y.shape[0]):
            if y[i].argmax() == t[i].argmax():  # 계산된 output값과 실제 class값이 들어있는 백터에서 가장 큰
                accuracy += 1                   # 원소를 가지고 있는 인덱스를 찾아 같은지 비교해서 정확도를 계산한다.
        accuracy = accuracy / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        """손실 값에 대한 수치미분을 통해 W1, b1, W2, b2를 수정한다."""
        h = 1e-4
        result = {}
        for i in ('W1', 'b1', 'W2', 'b2'):
            grad = np.zeros_like(self.params[i])
            for idx in range(self.params[i].shape[0]):
                tmp_val = (self.params[i])[idx]  # f(x+h) 계산 x = W1, b1, W2, b2
                (self.params[i])[idx] = tmp_val + h
                fxh1 = self.loss(x, t)  # 각 W1, b1, W2, b2에 대해서 손실값 계산.
                (self.params[i])[idx] = tmp_val - h
                fxh2 = self.loss(x, t)           # f(x-h) 계산
                grad[idx] = (fxh1 - fxh2) / (2 * h)     # 계산된 손실 값을 수치미분.
                (self.params[i])[idx] = tmp_val         # 원래 W1, b1, W2, b2으로 수정.
            result[i] = grad
        return result  # W1, b1, W2, b2에 대해 모든 수치미분 값을 반환.

    def learn(self, lr, epoch, batch_size):
        """ numerical gradient 를 사용하여 학습 """
        mask = np.random.choice(self.X.shape[0], 120)
        X = self.X[mask]                    # 120개의 train_set으로 분할.
        y = one_hot_encoding(self.y[mask])
        for i in range(epoch):
            batch = np.random.choice(X.shape[0], batch_size)    # 입력된 batch_size만큼 분할.
            train_batch_X = X[batch]
            train_batch_y = y[batch]
            grad = self.numerical_gradient(train_batch_X, train_batch_y)    # batch된 train_set에 대한 학습.
            for j in ('W1', 'b1', 'W2', 'b2'):
                self.params[j] -= lr * grad[j]      # batch된 train_set에 대한 학습을 하고,
            loss = self.loss(X, y)                  # 120개의 train_set에 대한 손실 값 측정.
            accuracy = self.accuracy(X, y)          # 120개의 train_set에 대한 정확도 측정.
            self.train_loss.append(loss)
            self.train_accuracy.append(accuracy)

            print("cost, accuracy ", loss, ", ", accuracy)  # 손실 값과 정확도에 대한 추이 출력.
        print("train accuracy = ", self.accuracy(train_batch_X, train_batch_y))     # 최종 학습에 대한
                                                                                    # train_set에 대한 정확도 출력.