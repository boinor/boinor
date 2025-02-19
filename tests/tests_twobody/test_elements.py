from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose
from numpy.testing import assert_allclose

from boinor.twobody.elements import (
    circular_velocity,
    get_inclination_critical_argp,
)


def test_simple_circular_velocity():
    """test for calculating the circular velocity"""
    k = 398600 * u.km**3 / u.s**2
    a = 7000 * u.km

    expected_V = 7.5460491 * u.km / u.s

    V = circular_velocity(k, a)

    assert_quantity_allclose(V, expected_V)


def test_get_inclination_critical_args():
    """test for calculating the critical inclination"""

    # values obtained DOI 10.1007/BF01228962
    R = 6378.163 * u.km
    J2 = 1.0826e-3
    J3 = 2.531e-6
    a = 8000 * u.km
    ecc = 0.10
    expected_inc = -1.2121427186368146 * u.rad

    inc = get_inclination_critical_argp(R, J2, J3, a, ecc)

    assert_allclose(expected_inc, inc)
