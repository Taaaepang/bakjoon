from collections import Counter
import sys
import math as mt

class KNN:
    def __init__(self, K, X, y, y_name):
        '''K Nearest Neighbor'''
        self.K = K  # 비교할 가까운 점의 갯수.
        self.X = X  # Train_Feature.
        self.y = y  # Train_Target(class).
        self.y_name = y_name  # 0 : setosa, 1 :  versicolor, 2 : virginica.
        self.distance_list = []  # 하나의 testcase와 모든 train_set의 거리.
        self.nearest_point = []  # K 값에 따른 가장 가까운 점들.
        self.nearest_distance = []  # 가중치 계산을 위한 가까운 점과의 거리.

    def Calculate_distance(self, test_feature):
        '''한개 test_feature과 모든 train_feature의 거리를 구한다.'''
        for i in self.X:  # 하나의 train_feature 차례대로 접근.
            k = 0  # test_feature 접근을 위해 index 역할.
            distance = 0  # 거리를 임시 저장하기 위한 변수.
            for j in i:  # feature안에 하나의 x값 접근. 총 4번 접근.
                distance += (j - test_feature[k]) ** 2  # 4개의 x값에 대해 (train_feature_x - test_feature_x_)^2 한값을 더함.
                k += 1  # train_feature_x에 대해 test_feature_x의 인덱스를 맞춘다.
            self.distance_list.append(mt.sqrt(distance))
            # distance 변수를 square root => train_feature와 train_feature거리를 리스트에 삽입.

    def Obtain_K_Nearest_Neighbor(self, test_feature):
        '''k개 가까운 점을 찾아 weight_majority_vote, majority_vote를 계산한다'''
        self.Calculate_distance(test_feature)  # 하나의 test_feature에 대한 모든 train_feature과의 거리를 저장.
        sorted_list = []
        sorted_list = self.distance_list[:]
        sorted_list.sort()  # 모든 train_feature과의 거리를 리스트에 복사한 뒤 오름차순 정렬.
        for i in range(0, self.K):  # 가까운 거리에 해당되는 K개의 feature을 순서대로 뽑아내서,
            for idx, val in enumerate(self.distance_list):
                if sorted_list[i] == val:  # 정렬된 거리와 train_feature 들의 거리와 비교해서 같으면,
                    self.nearest_point.append(idx)  # feature의 해당되는 train_set의 index를 리스트에 추가.
                    self.nearest_distance.append(val)  # 가중치를 위해 거리 저장.
                    break  # 찾으면 다음 가까운 점을 찾는다. K번 반복.
        W_name, M_name = self.Get_votes()     # weight_majority_vote, majority_vote를 구해서 변수에 삽입.
        self.distance_list.clear()
        self.nearest_point.clear()
        self.nearest_distance.clear()   # 다음 test_feature의 거리를 구하기 위해 초기화.
        return W_name, M_name   # weight_majority_vote, majority_vote 반환.

    def Get_votes(self):
        ''' weight_majority_vote, majority_vote를 구해서 반환.'''
        majority_vote = []  # majority_vote 계산을 위한 list.
        weights = []    # weight_majority_vote 계산을 위해 가중치를 계산.
        name = ''   # 가중치 계산 후 weight_majority_vote에 따른 아이리스 이름을 저장.
        A = B = C = 0 # 가중치 비교 변수. A: Setosa, B: Versicolor, C: Virginic

        for i in self.nearest_point:
            majority_vote.append(self.y[i])     # K개의 가까운 feature의 class 저장.
        for i in self.nearest_distance:
            if 1/i > sys.maxsize - 1:       # overflow 처리
                we = sys.maxsize - 1
            else:
                we = 1/i
            weights.append(we)   # 가중치 = 1 / 거리

        class_number = Counter(majority_vote)   # class 갯수 . ex) [1, 1, 2] => ({'1' : 2, '2' : 1})

        for i in range(0, self.K):   # weight는 각 nearest_point와 가중치의 정보를 가지고 있으므로,
            if majority_vote[i] == 0:  # class에 맞는 name에 해당되는 변수에 가중치를 더해준다.
                A += weights[i]
            elif majority_vote[i] == 1:
                B += weights[i]
            elif majority_vote[i] == 2:
                C += weights[i]
        if max(A, B, C) == A:   # A, B, C중 제일 큰 변수를 찾아서, 그것에 해당되는 꽃 이름을 name에저장.
            name = self.y_name[0]
        elif max(A, B, C) == B:
            name = self.y_name[1]
        elif max(A, B, C) == C:
            name = self.y_name[2]
        return name, self.y_name[class_number.most_common(1)[0][0]] # weight_majority_vote, majority_vote 반환.
