"""Low-level calculations for the NRLMSIS atmospheric model, version 2.0.

References: :cite:t:`NRLMSIS`:

"""

from numba import njit as jit
import numpy as np


@jit
def dummy_function():
    i=999
