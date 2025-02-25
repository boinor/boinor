from unittest.mock import patch

from astropy import units as u
import pytest

from boinor.io import orbit_from_sbdb


def patch_sbdb_getData(name, **kwargs):
    if name == "test1":
        rc = {
            "object": {"shortname": "test1", "neo": True, "moid": 0.334},
            "orbit": {
                "elements": {
                    "ma": 90.28032584 * u.deg,
                    "a": 1.0 * u.AU,
                    "e": 0.2,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 1 * u.d,
            },
        }
    if name == "test2":
        rc = {
            "orbit": {
                "elements": {
                    "ma": 90.28032584 * u.deg,
                    "a": 1.0 * u.AU,
                    "e": 0.2,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 1 * u.d,
            }
        }
    if name == "test3":
        rc = {
            "object": {"shortname": "test1", "neo": True, "moid": 0.334},
            "orbit": {
                "elements": {
                    "ma": 90.28032584,
                    "a": 1.0 * u.AU,
                    "e": 0.2,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 1 * u.d,
            },
        }

    return rc


@patch("astroquery.jplsbdb.SBDB.query", new=patch_sbdb_getData)
def test_orbit_from_sbdb():
    test_kwargs = {"phys": False}

    # should not raise an exception
    orbit_from_sbdb("test1", **test_kwargs)

    # no "object" available
    with pytest.raises(ValueError) as exc2:
        orbit_from_sbdb("test2", **test_kwargs)
    assert "ValueError" in exc2.exconly()

    # attribute missing
    with pytest.raises(AttributeError) as exc3:
        orbit_from_sbdb("test3", **test_kwargs)
    assert "AttributeError" in exc3.exconly()
