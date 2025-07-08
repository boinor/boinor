from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose
import numpy as np
import pytest

from boinor.bodies import Earth, Sun
from boinor.twobody.states import (
    BaseState,
    ClassicalState,
    ModifiedEquinoctialState,
    RVState,
)


def test_state_has_attractor_given_in_constructor():
    _d = 1.0 * u.AU  # Unused distance
    _ = 0.5 * u.one  # Unused dimensionless value
    _a = 1.0 * u.deg  # Unused angle
    ss = ClassicalState(Sun, (_d, _, _a, _a, _a, _a), None)
    assert ss.attractor == Sun


def test_classical_state_has_elements_given_in_constructor():
    # Mars data from HORIZONS at J2000
    a = 1.523679 * u.AU
    ecc = 0.093315 * u.one
    inc = 1.85 * u.deg
    raan = 49.562 * u.deg
    argp = 286.537 * u.deg
    nu = 23.33 * u.deg
    ss = ClassicalState(
        Sun, (a * (1 - ecc**2), ecc, inc, raan, argp, nu), None
    )
    assert ss.p == a * (1 - ecc**2)
    assert ss.ecc == ecc
    assert ss.inc == inc
    assert ss.raan == raan
    assert ss.argp == argp
    assert ss.nu == nu


def test_rv_state_has_rv_given_in_constructor():
    r = [1.0, 0.0, 0.0] * u.AU
    v = [0.0, 1.0e-6, 0.0] * u.AU / u.s
    ss = RVState(Sun, (r, v), None)
    assert (ss.r == r).all()
    assert (ss.v == v).all()


def test_mean_motion():
    # From Vallado Example 1-1.
    attractor = Earth
    period = 86164.090518 * u.s
    a = 42164.1696 * u.km
    # Unused variables.
    _ecc = 0 * u.one
    _inc = 1.85 * u.deg
    _raan = 50 * u.deg
    _argp = 200 * u.deg
    _nu = 20 * u.deg

    ss = ClassicalState(
        attractor, (a * (1 - _ecc**2), _ecc, _inc, _raan, _argp, _nu), None
    )

    expected_mean_motion = (2 * np.pi / period) * u.rad
    n = ss.n

    assert_quantity_allclose(n, expected_mean_motion)


def test_coe_to_mee_raises_singularity_error_orbit_equatorial_and_retrograde():
    a = 10000 * u.km
    ecc = 0.3 * u.one
    inc = 180 * u.deg  # True retrograde equatorial case.
    raan = 49.562 * u.deg
    argp = 286.537 * u.deg
    nu = 23.33 * u.deg

    ss = ClassicalState(
        Sun, (a * (1 - ecc**2), ecc, inc, raan, argp, nu), None
    )
    with pytest.raises(ValueError) as excinfo:
        ss.to_equinoctial()
    assert (
        "Cannot compute modified equinoctial set for 180 degrees orbit inclination due to `h` and `k` singularity."
        in excinfo.exconly()
    )


def test_state_methods():
    _d = 1.0 * u.AU  # distance
    _n = 0.5 * u.one  # dimensionless value
    _a = 1.0 * u.deg  # angle

    bs = BaseState(Sun, (_d, _n, _a, _a, _a, _a), None)
    mes = ModifiedEquinoctialState(Sun, (_d, _n, _a, _a, _a, _a), None)

    # these functions are not and should not be implemented in the BaseState()
    with pytest.raises(NotImplementedError, match=""):
        bs.to_value()

    with pytest.raises(NotImplementedError, match=""):
        bs.to_vectors()

    with pytest.raises(NotImplementedError, match=""):
        bs.to_classical()

    with pytest.raises(NotImplementedError, match=""):
        bs.to_equinoctial()

    assert_quantity_allclose(_d, mes.p)
    assert_quantity_allclose(_n, mes.f)
    assert_quantity_allclose(_a, mes.g)
    assert_quantity_allclose(_a, mes.h)
    assert_quantity_allclose(_a, mes.k)
    assert_quantity_allclose(_a, mes.L)

    expected_res = (
        149597870.7,
        0.5,
        0.017453292519943295,
        0.017453292519943295,
        0.017453292519943295,
        0.017453292519943295,
    )
    expected_res_from_classical = (
        1.495979e08,
        5.003045e-01,
        4.935534e-02,
        7.853982e-01,
        5.532680e00,
        6.265746e00,
    )
    expected_res_from_vectors = [
        [9.964189e07, 1.799942e06, -3.417410e06],
        [-1.011823e00, 4.464467e01, 1.594684e00],
    ]
    res = mes.to_value()
    assert_quantity_allclose(res, expected_res)

    res_from_classical = mes.to_classical()
    value_res_from_classical = res_from_classical.to_value()
    assert_quantity_allclose(
        value_res_from_classical, expected_res_from_classical, rtol=1e-6
    )

    res_from_equinoctial = res_from_classical.to_equinoctial()
    res_from_equinoctial.to_value()
    assert_quantity_allclose(
        value_res_from_classical, expected_res_from_classical, rtol=1e-6
    )

    res_from_vectors = mes.to_vectors()
    value_res_from_vectors = res_from_vectors.to_value()
    assert_quantity_allclose(
        value_res_from_vectors, expected_res_from_vectors, rtol=1e-6
    )
