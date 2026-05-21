import tensorflow as tf
import numpy as np


def linear_function(x, x0, x1, y0, y1):
    m = (y1 - y0) / (x1 - x0)
    b = y0 - m * x0
    return m * x + b


def piecewise_linear(step, x, y):
    """
    Piecewise linear function.
    
    :param step: current step.
    :param x: list of breakpoints
    :param y: list of values at breakpoints
    :return: value of piecewise linear function with values Y_i at step X_i
    """
    assert len(x) == len(y)
    x = np.array(x)
    if step < x[0]:
        return y[0]
    idx = np.where(step >= x)[0][-1]
    if idx == (len(y) - 1):
        return y[-1]
    else:
        return linear_function(step, x[idx], x[idx + 1], y[idx], y[idx + 1])


def piecewise_linear_schedule(step, schedule):
    schedule = np.array(schedule)
    x_schedule = schedule[:, 0]
    y_schedule = schedule[:, 1]
    value = piecewise_linear(step, x_schedule, y_schedule)
    return tf.cast(value, tf.float32)

