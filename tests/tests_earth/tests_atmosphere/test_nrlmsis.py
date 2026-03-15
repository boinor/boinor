"""tests related to module nrlmsis in sub-package atmosphere of earth"""
from astropy.tests.helper import assert_quantity_allclose
import pytest

import boinor.core.earth_atmosphere.nrlmsis as cnrlmsis

# even internal stuff needs to be tested
# pylint: disable=protected-access


def test_t_of_zeta():
    temperature_profile = cnrlmsis.Bates_temperature_profile(0, 0, 0)

    # XXX this case is still missing
    with pytest.raises(NotImplementedError, match="case zeta < zetab not yet implemented"):
        t_of_zeta = cnrlmsis.t_of_zeta(50, temperature_profile)

    T_ex = 12.0
    temperature_profile_t1 = cnrlmsis.Bates_temperature_profile(T_ex, 0, 0)
    t_of_zeta = cnrlmsis.t_of_zeta(cnrlmsis.core_zetaB + 120, temperature_profile_t1)
    assert_quantity_allclose(t_of_zeta, 0.0, rtol=1e-16)

    T_ex = 1000.0
    temperature_profile_t1 = cnrlmsis.Bates_temperature_profile(T_ex, 0, 0)
    t_of_zeta = cnrlmsis.t_of_zeta(cnrlmsis.core_zetaB + 120, temperature_profile_t1)
    assert_quantity_allclose(t_of_zeta, 0.0, rtol=1e-16)
