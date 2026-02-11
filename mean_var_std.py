def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    
    import numpy as np
    mat = np.array(lista).reshape(3, 3)
    mean = [mat.mean(axis=0).tolist(), mat.mean(axis=1).tolist(), mat.mean().tolist()]
    variance = [mat.var(axis=0).tolist(), mat.var(axis=1).tolist(), mat.var().tolist()]
    standerd_dev = [mat.std(axis=0).tolist(), mat.std(axis=1).tolist(), mat.std().tolist()]
    maximum = [mat.max(axis=0).tolist(), mat.max(axis=1).tolist(), mat.max().tolist()]
    minimum = [mat.min(axis=0).tolist(), mat.min(axis=1).tolist(), mat.min().tolist()]
    sum = [mat.sum(axis=0).tolist(), mat.sum(axis=1).tolist(), mat.sum().tolist()]     
    return {
             'mean': mean,
             'variance': variance, 
             'standard deviation': standerd_dev,
             'max': maximum,
             'min': minimum,
             'sum': sum
             }     
