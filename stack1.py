def solution(bridge_length, weight, truck_weights):
    delayed = truck_weights.copy()
    arrived = list()
    bridge_info = [0] * bridge_length
    weight_info = 0
    time = 0
    while True:
        time += 1
        temp = bridge_info.pop(0)
        if len(delayed) != 0:
            go = delayed.pop(0)
            if temp != 0:
                arrived.append(temp)
                weight_info -= temp
            if weight_info + go > weight:
                delayed.insert(0, go)
                bridge_info.append(0)
            else:
                bridge_info.append(go)
                weight_info += go
        else:
            if temp != 0:
                arrived.append(temp)
                weight_info -= go
        if len(arrived) == len(truck_weights):
            break
    return time




bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

print(solution(bridge_length, weight, truck_weights))