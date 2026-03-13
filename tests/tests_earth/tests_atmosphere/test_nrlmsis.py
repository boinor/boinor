"""tests related to module nrlmsis in sub-package atmosphere of earth"""
from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose
import numpy as np
import pytest

from boinor.earth.atmosphere.nrlmsis import Nrlmsis

# even internal stuff needs to be tested
# pylint: disable=protected-access

def test_values():
    print("XXX this is just a dummy test")
