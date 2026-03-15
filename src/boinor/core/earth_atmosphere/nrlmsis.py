"""Low-level calculations for the NRLMSIS atmospheric model, version 2.0.

References: :cite:t:`NRLMSIS`:

"""

from dataclasses import dataclass

import numpy as np

#: Bates profile reference height and joining height
#: :cite:t:`Bates1959`:
#: this is only the value without unit
core_zetaB = 122.5


@dataclass
class Bates_temperature_profile:
    T_ex: float
    T_B: float
    sigma: float


def t_of_zeta(zeta, tp):
    """calculate temperature T depending on geopotential height zeta
    in:  zeta, float	geopotential height
    in:  tp, Bates termospheric temperate profile (type Bates_temperature_profile)

    out: T(zeta), float

    there are different calculations for zeta >= and < zetab
    see :cite:t:`NRLMSIS`: page 3
    """
    if zeta >= core_zetaB:
        return tp.T_ex - (tp.T_ex - tp.T_B) * np.exp(-tp.sigma * (zeta - core_zetaB))
    else:
        message = "case zeta < zetab not yet implemented"
        raise NotImplementedError(message)

    message = "how did we arrive here"
    raise NotImplementedError(message)
