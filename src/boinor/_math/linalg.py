"""basic linear algebra functions in the _math sub-package"""
from numba import njit as jit
import numpy as np


@jit
def norm(arr):
    """calculate norm of matrix or vector"""
    return np.sqrt(arr @ arr)
