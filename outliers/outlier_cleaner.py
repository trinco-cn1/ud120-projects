#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range(0, len(ages)):
        age = ages[i][0]
        net_worth = net_worths[i][0]
        pred = predictions[i][0]
        error = abs(net_worth - pred)
        cleaned_data.append((ages[i][0], net_worths[i][0], error))

    length = len(ages)
    cleaned_data = sorted(cleaned_data, key=lambda data:data[2])[:(length * 9) // 10]


    return cleaned_data

