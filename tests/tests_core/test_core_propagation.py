from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose
import pytest

from boinor.core.elements import coe2rv
from boinor.core.propagation import (
    danby,
    danby_coe,
    farnocchia,
    gooding,
    gooding_coe,
    markley,
    markley_coe,
    mikkola,
    mikkola_coe,
    pimienta,
    pimienta_coe,
    recseries,
    vallado,
)
from boinor.core.propagation.farnocchia import (
    M_to_D_near_parabolic,
    _kepler_equation_near_parabolic,
    _kepler_equation_prime_near_parabolic,
    d2S_x_alt,
    dS_x_alt,
    farnocchia_coe,
    nu_from_delta_t,
)
from boinor.examples import iss


@pytest.mark.parametrize(
    "propagator_coe",
    [
        danby_coe,
        markley_coe,
        pimienta_coe,
        mikkola_coe,
        farnocchia_coe,
        gooding_coe,
    ],
)
def test_propagate_with_coe(propagator_coe):
    period = iss.period
    a, ecc, inc, raan, argp, nu = iss.classical()
    p = a * (1 - ecc**2)

    # Delete the units
    p = p.to_value(u.km)
    ecc = ecc.value
    period = period.to_value(u.s)
    inc = inc.to_value(u.rad)
    raan = raan.to_value(u.rad)
    argp = argp.to_value(u.rad)
    nu = nu.to_value(u.rad)
    k = iss.attractor.k.to_value(u.km**3 / u.s**2)

    nu_final = propagator_coe(k, p, ecc, inc, raan, argp, nu, period)

    assert_quantity_allclose(nu_final, nu)


def test_farnocchia_stuff():
    D = 1.1
    M = 1.3
    ecc = 0.999

    expected_value = 0.24328683542064818
    value = _kepler_equation_near_parabolic(D, M, ecc)
    assert_quantity_allclose(expected_value, value)

    expected_value = 2.2078790282669667
    value = _kepler_equation_prime_near_parabolic(D, M, ecc)
    assert_quantity_allclose(expected_value, value)

    x = 1.0
    with pytest.raises(AssertionError, match=""):
        value = dS_x_alt(ecc, x)

    x = 0.5
    expected_value = 7.99
    value = dS_x_alt(ecc, x)
    assert_quantity_allclose(expected_value, value)

    x = 1.0
    with pytest.raises(AssertionError, match=""):
        value = d2S_x_alt(ecc, x)

    x = 0.5
    expected_value = 47.944
    value = d2S_x_alt(ecc, x)
    assert_quantity_allclose(expected_value, value)

    expected_value = 0.9832822210139998
    value = M_to_D_near_parabolic(M, ecc)
    assert_quantity_allclose(expected_value, value)

    expected_value = 0.5381960297002113
    value = nu_from_delta_t(0.4, ecc)
    assert_quantity_allclose(expected_value, value)

    ecc = 1.00001  # needs to be hyperbolic
    expected_value = 0.5383066383929812
    value = nu_from_delta_t(0.4, ecc)
    assert_quantity_allclose(expected_value, value)


def test_kepler_algorithm():
    # own invented values might not be that good, better use data from ISS
    #    k = Earth.k
    #    r0 = [5000.0, 10000.0, 2100.0] * u.km
    #    v0 = [15.0, 110.0, 12.0] * u.km / u.s
    #    expected_r = [2532.06252977, 5067.56395212, 1063.7112836]
    #    expected_v = [-114809.18251688, -229616.31786688, -48219.71079645]

    tof = 1.0 * u.h
    tof = tof.to_value(u.h)
    numiter = 100
    expected_r = [866.444902, -4135.118792, 5296.005316]
    expected_v = [7.371786, 2.087538, 0.433211]

    a, ecc, inc, raan, argp, nu = iss.classical()
    period = iss.period

    p = a * (1 - ecc**2)

    # Delete the units
    p = p.to_value(u.km)
    ecc = ecc.value
    period = period.to_value(u.s)
    inc = inc.to_value(u.rad)
    raan = raan.to_value(u.rad)
    argp = argp.to_value(u.rad)
    nu = nu.to_value(u.rad)
    k = iss.attractor.k.to_value(u.km**3 / u.s**2)

    r0, v0 = coe2rv(k, p, ecc, inc, raan, argp, nu)

    #    print("null: ", r0, v0)
    #    print("expected: ", expected_r, expected_v)

    value_recseries = recseries(k, r0, v0, tof)
    #    print("recseries: ", value_recseries)
    assert_quantity_allclose(expected_r, value_recseries[0])
    assert_quantity_allclose(expected_v, value_recseries[1], rtol=1e-06)

    value = pimienta(k, r0, v0, tof)
    #    print("pimienta: ", value)
    assert_quantity_allclose(expected_r, value[0])
    assert_quantity_allclose(expected_v, value[1], rtol=1e-06)

    # XXX what does that mean?
    f, g, fdot, gdot = vallado(k, r0, v0, tof, numiter)
    print("vallado: ", f, g, fdot, gdot)
    #    assert_quantity_allclose(expected_r, value[0])
    #    assert_quantity_allclose(expected_v, value[1])

    value_danby = danby(k, r0, v0, tof)
    #    print("danby: ", value_danby)
    assert_quantity_allclose(expected_r, value_danby[0])
    assert_quantity_allclose(expected_v, value_danby[1], rtol=1e-06)

    value_gooding = gooding(k, r0, v0, tof)
    #    print("gooding: ", value_gooding)
    assert_quantity_allclose(expected_r, value_gooding[0])
    assert_quantity_allclose(expected_v, value_gooding[1], rtol=1e-06)

    value_markley = markley(k, r0, v0, tof)
    #    print("markley: ", value_markley)
    assert_quantity_allclose(expected_r, value_markley[0])
    assert_quantity_allclose(expected_v, value_markley[1], rtol=1e-06)

    value = mikkola(k, r0, v0, tof)
    #    print("mikkola: ", value)
    assert_quantity_allclose(expected_r, value[0])
    assert_quantity_allclose(expected_v, value[1], rtol=1e-06)

    value_farnocchia = farnocchia(k, r0, v0, tof)
    #    print("farnocchia: ", value_farnocchia)
    assert_quantity_allclose(expected_r, value_farnocchia[0])
    assert_quantity_allclose(expected_v, value_farnocchia[1], rtol=1e-06)


# todo: does not work
#    value_cowell_r, value_cowell_v=cowell(k, r0, v0, tof)
#    print("cowell: ", value_cowell_r, value_cowell_v)
#    assert_quantity_allclose(expected_r, value_cowell_r)
#    assert_quantity_allclose(expected_v, value_cowell_v)
