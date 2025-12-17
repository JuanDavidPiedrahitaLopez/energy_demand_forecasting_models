# función para definir el SMAPE

import numpy as np

def symmetric_mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(
        np.abs(y_true - y_pred) / ((np.abs(y_true) + np.abs(y_pred)) / 2)
    )