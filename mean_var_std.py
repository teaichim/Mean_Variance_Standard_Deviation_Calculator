import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    arr = np.array(list)
    
    matrix = arr.reshape(3, 3)

    calculations = {
        'mean': [np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist(), np.mean(arr).tolist()],
        'variance': [np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist(), np.var(arr).tolist()],
        'standard deviation': [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), np.std(arr).tolist()],
        'max': [np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist(), np.max(arr).tolist()],
        'min': [np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist(), np.min(arr).tolist()],
        'sum': [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), np.sum(arr).tolist()]
    }


    return calculations