import numpy as np


def mean_squared_error(y_true, y_pred):
    """Mean squared error regression loss

    Parameters
    ----------

    y_true : array-like of shape (n_samples,)
        Ground truth (correct) target values.
    y_pred : array-like of shape (n_samples,)
        Estimated target values.

    Returns
    -------

    loss: float
    A non-negative floating point value (the best value is 0.0)

    """
    mse = np.average((y_true - y_pred) ** 2)
    return mse


def root_mean_squared_error(y_true, y_pred):
    """Root mean squared error regression loss

    Parameters
    ----------

    y_true : array-like of shape (n_samples,)
        Ground truth (correct) target values.
    y_pred : array-like of shape (n_samples,)
        Estimated target values.

    Returns
    -------

    loss: float
    A non-negative floating point value (the best value is 0.0)

    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse


def mean_absolute_error(y_true, y_pred):
    """Mean absolute error regression lose

    Parameters
    ----------

    y_true : array-like of shape (n_samples,)
        Ground truth (correct) target values.
    y_pred : array-like of shape (n_samples,)
        Estimated target values.

    Returns
    -------
    loss: float
    Output is non-negative floating point. The best value is 0.0.
    """
    mae = np.average(np.abs(y_true - y_pred))
    return mae
