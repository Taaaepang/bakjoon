def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = list()
    for i in range(bridge_length):
        stack.append(0)
    weight_br = 0
    i = 0
    weight_truck = truck_weights.copy()
    arrive_truck = list()
    while True:
        answer += 1
        temp = stack.pop(0)
        if temp != 0:
            arrive_truck.append(temp)
            weight_br -= temp
        if len(weight_truck) > 0:
            if weight_br + weight_truck[0] <= weight:
                tmp = weight_truck.pop(0)
                weight_br += tmp
                stack.append(tmp)
        if len(stack) < bridge_length:
            stack.append(0)
        if len(arrive_truck) == len(truck_weights):
            break
    return answer


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(bridge_length, weight, truck_weights))