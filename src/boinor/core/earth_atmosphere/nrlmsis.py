"""Low-level calculations for the NRLMSIS atmospheric model, version 2.0.

References: :cite:t:`NRLMSIS`:

"""

from dataclasses import dataclass

import numpy as np

#: Bates profile reference height and joining height
#: :cite:t:`Bates1959`:
#: this is only the value without unit
core_zetaB = 122.5

#: Convert degree to radian
deg2rad = np.pi / 180.0

#: Earth's gravitational constant
GM = 398600.4418  # km^3/s^2
#: Angular rotation speed of Earth
omega = 7292115.0e-11  # rad/s
#: Potenial on the reference ellipsoid
U0 = -62.63685171  # km2/s2
#: standardd gravity
g0 = 9.80665e-3  # km/s2
#: transformation between geodetic and ellipsoidal coordinates
#: calculation is using reference ellipsoid WGS-84
#: see :cite:t:`Featherstone2008ClosedformTB`:
# XXX can we use these values from somewhere else?
a = 6378137  # equatorial radius (m) = semi-major axis of ellipsoid
f_inverse = 298.257223563  # inverse flattening 1/f
f = 1 / f_inverse  # flattening
b = a * (1 - f)  # semi-minor axis of ellipsoid
e = np.sqrt(2 * f - f * f)  # numerical eccentricity of ellipsoid
E = a * e  # linear eccentricity of ellipsoid


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


def alt_to_gph(latitude, altitude):
    """convert geodetic latitude and altitude to geopotential height
       see :cite:t:`NRLMSIS`: Appendix A

    in: latitude, float    geodetic latitude, unit = rad
    in: altitude, float    altitude

    out: geopotential height, float
    """

    """-----------------------------------------------------------"""
    """ convert geodetic latitude and altitude to ellipsoidal coordinates
    see :cite:t:`Featherstone2008ClosedformTB`:
    """

    sinlat = np.sin(latitude)
    coslat = np.cos(latitude)

    #: radius of curvature in the prime vertival of the surface of the geodetic ellipsoid
    v = a / np.sqrt(1 - e * e * sinlat * sinlat)

    #: distance from rotation axis
    x = (v + altitude) * coslat  # XXX is this ok? in featherstone (1) there is also a sin(lambda)
    #: distance from equatorial plane
    z = (v * (1 - e * e) + altitude) * sinlat

    r2 = x * x + z * z
    #: ellipsodial parameter
    u2 = (r2 - E * E) / 2.0 + np.sqrt((r2 - E * E) * (r2 - E * E) / 4.0 + z * z * E * E)
    u = np.sqrt(u2)
    #: ellipsodial colatitude
    cos2delta = (z * z) / u2

    """-----------------------------------------------------------"""
    """ calculate geopotential U
    see :cite:t:`Jekeli2007`:
    """

    q = 0.5 * ((1 + 3 * u2 / (E * E)) * np.atan(E / u) - 3 * u / E)
    q0 = 0.5 * ((1 + 3 * b * b / (E * E)) * np.atan(E / b) - 3 * b / E)
    U = -1 * (
        GM / E * np.atan(E / u) + 0.5 * omega * a * a * q / q0 * (cos2delta - 1 / 3) + 0.5 * omega * omega * x * x
    )  # XXX take care of units

    """-----------------------------------------------------------"""
    """ calculate geopotential height zeta
    """
    zeta = (U - U0) / g0

    return zeta


def alt_to_gph_deg(latitude, altitude):
    """convert geodetic latitude and altitude to geopotential height
       see :cite:t:`NRLMSIS`: Appendix A

    in: latitude, float    geodetic latitude, unit = deg
    in: altitude, float    altitude

    out: geopotential height, float
    """

    return alt_to_gph(latitude * deg2rad, altitude)


def alt_to_gph_rad(latitude, altitude):
    """convert geodetic latitude and altitude to geopotential height
       see :cite:t:`NRLMSIS`: Appendix A

    in: latitude, float    geodetic latitude, unit = rad
    in: altitude, float    altitude

    out: geopotential height, float
    """

    return alt_to_gph(latitude, altitude)
