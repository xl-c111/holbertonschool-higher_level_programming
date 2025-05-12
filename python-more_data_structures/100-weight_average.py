#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        total_scores = 0
        total_weights = 0
        for score, weight in my_list:
            total_scores += score * weight
            total_weights += weight
            weight_average = total_scores / total_weights
        return weight_average
