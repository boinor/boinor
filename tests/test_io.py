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
                "epoch": 2460800.5 * u.d,
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
                "epoch": 2460800.5 * u.d,
            }
        }
    if name == "test3":
        rc = {
            "object": {"shortname": "test3", "neo": True, "moid": 0.334},
            "orbit": {
                "elements": {
                    "ma": 90.28032584,
                    "a": 1.0 * u.AU,
                    "e": 0.2,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 2460800.5 * u.d,
            },
        }

    if name == "test4":
        rc = {
            "object": {"shortname": "test4", "neo": True, "moid": 0.334},
            "orbit": {
                "elements": {
                    "ma": 90.28032584 * u.deg,
                    "a": 1.0 * u.AU,
                    "e": 1.0,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 2460800.5 * u.d,
            },
        }
    if name == "test5":
        rc = {
            "object": {"shortname": "test5", "neo": True, "moid": 0.334},
            "orbit": {
                "elements": {
                    "ma": 90.28032584 * u.deg,
                    "a": -1.0 * u.AU,
                    "e": 1.1,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 2460800.5 * u.d,
            },
        }
    if name == "test6":
        rc = {
            "object": {"shortname": "test6", "neo": True, "moid": 0.334},
            "orbit": {
                "elements": {
                    "ma": 90.28032584 * u.deg,
                    "a": 1.0 * u.AU,
                    "e": 0.0,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 2460800.5 * u.d,
            },
        }
    if name == "test7":
        rc = {
            "count": {"blub": "2"},
            "list": {"name": {"a": "v", "b": "v", "c": "v"}},
            "object": {"shortname": "test7", "neo": True, "moid": 0.334},
            "orbit": {
                "elements": {
                    "ma": 90.28032584 * u.deg,
                    "a": 1.0 * u.AU,
                    "e": 0.0,
                    "i": 3.0 * u.deg,
                    "om": 4.0 * u.deg,
                    "w": 5.0 * u.deg,
                },
                "epoch": 2460800.5 * u.d,
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

    # e=1; no body in SBDB should have e=1, so this should raise an exception somewhere
    with pytest.raises(
        ValueError, match="For parabolic orbits use Orbit.parabolic instead"
    ):
        orbit_from_sbdb("test4", **test_kwargs)

    # e=1.1; no body in SBDB should have e>1, but it seems to work
    orbit_from_sbdb("test5", **test_kwargs)

    # e=0; no body in SBDB should have e==0, but it seems to work
    orbit_from_sbdb("test6", **test_kwargs)

    # count=2
    with pytest.raises(ValueError, match="different objects found"):
        orbit_from_sbdb("test7", **test_kwargs)
