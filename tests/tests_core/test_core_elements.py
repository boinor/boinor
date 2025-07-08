from astropy import units as u
import numpy as np
from numpy.testing import assert_allclose

from boinor.bodies import Earth

# lots of functions are already checked somewhere else
# unfortunately mee2rv is missing
from boinor.core.elements import coe2mee, coe2rv, mee2coe, mee2rv, rv2coe


def test_conversions():
    # taken from the rv2coe() example
    # this is a bad example as it results in 90 < i <180, which is a retrograde orbit
    # and coe2mee() can not handle this
    # k = Earth.k.to_value(u.km**3 / u.s**2)
    # r = np.array([-6045.0, -3490.0, 2500.0])
    # v = np.array([-3.457, 6.618, 2.533])

    # this values are better
    k = Earth.k.to_value(u.km**3 / u.s**2)
    r = np.array([-6045.0, -3490.0, 2500.0])
    v = np.array([-3.457, -6.618, -2.533])

    p_coe, ecc_coe, inc_coe, raan_coe, argp_coe, nu_coe = rv2coe(k, r, v)

    p_mee, f_mee, g_mee, h_mee, k_mee, L_mee = coe2mee(
        p_coe, ecc_coe, inc_coe, raan_coe, argp_coe, nu_coe
    )
    p_coe2, ecc_coe2, inc_coe2, raan_coe2, argp_coe2, nu_coe2 = mee2coe(
        p_mee, f_mee, g_mee, h_mee, k_mee, L_mee
    )
    assert_allclose(p_coe, p_coe2)
    assert_allclose(ecc_coe, ecc_coe2)
    assert_allclose(inc_coe, inc_coe2)
    assert_allclose(raan_coe, raan_coe2)
    assert_allclose(argp_coe, argp_coe2)
    assert_allclose(nu_coe, nu_coe2)

    r_rv, v_rv = mee2rv(k, p_mee, f_mee, g_mee, h_mee, k_mee, L_mee)
    # print("r:", r, " <-> ", r_rv)
    # print("v:", v, " <-> ", v_rv)

    assert_allclose(r, r_rv)
    assert_allclose(v, v_rv)

    r_new, v_new = coe2rv(
        k, p_coe, ecc_coe, inc_coe, raan_coe, argp_coe, nu_coe
    )
    assert_allclose(r, r_new)
    assert_allclose(v, v_new)
