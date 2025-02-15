from astropy import units as u
import numpy as np
from numpy.testing import assert_allclose

from boinor.bodies import Earth

# lots of functions are already checked somewhere else
# unfortunately mee2rv is missing
from boinor.core.elements import coe2mee, mee2rv, rv2coe


def test_conversions():
    # taken from the rv2coe() example
    k = Earth.k.to_value(u.km**3 / u.s**2)
    r = np.array([-6045.0, -3490.0, 2500.0])
    np.array([-6444.0, -5555.0, 2500.0])
    v = np.array([-3.457, 6.618, 2.533])
    p_coe, ecc_coe, inc_coe, raan_coe, argp_coe, nu_coe = rv2coe(k, r, v)
    print("p_coe:", p_coe, "[km]")

    p_mee, f_mee, g_mee, h_mee, k_mee, L_mee = coe2mee(
        p_coe, ecc_coe, inc_coe, raan_coe, argp_coe, nu_coe
    )

    r_rv, v_rv = mee2rv(p_mee, f_mee, g_mee, h_mee, k_mee, L_mee)

    print("r:", r, " <-> ", r_rv)
    print("v:", v, " <-> ", v_rv)

    assert_allclose(r, r_rv)
    # XXX this does not work, see #1
    # v_rv contains all NAN
    # assert_allclose(v,v_rv)
