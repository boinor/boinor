from astropy import time, units as u
import pytest

from boinor.bodies import Earth, Mars
from boinor.earth import EarthSatellite
from boinor.earth.plotting import GroundtrackPlotter
from boinor.twobody import Orbit
from boinor.util import time_range


class TestEarthSatellite(EarthSatellite):
    """Position and velocity of a body with respect to Earth
    at a given time.
    derived from EarthSatellite to do some testing with orbits here
    """

    def __init__(self, orbit, spacecraft):
        """Constructor.

        Parameters
        ----------
        orbit : Orbit
            Position and velocity of a body with respect to an attractor
            at a given time (epoch).
        spacecraft : Spacecraft

        Raises
        ------
        ValueError
            If the orbit's attractor is not Earth

        """
        #        if orbit.attractor is not Earth:
        #            raise ValueError("The attractor must be Earth")

        self._orbit = orbit  # type: Orbit
        self._spacecraft = spacecraft


def test_groundtrack_general():
    # at the moment just a general test to check whether there is no assert

    # Generate an instance of the plotter, add title and show latlon grid
    gp = GroundtrackPlotter()
    gp.update_layout(title="Test groundtrack")

    # create some objects in orbits
    iss = Orbit.from_vectors(  # from boinor.examples
        Earth,
        [8.59072560e2, -4.13720368e3, 5.29556871e3] * u.km,
        [7.37289205, 2.08223573, 4.39999794e-1] * u.km / u.s,
        time.Time("2013-03-18 12:00", scale="utc"),
    )
    iss_spacecraft = EarthSatellite(iss, None)

    testBody1 = Orbit.from_vectors(
        Mars,
        [8.59072560e2, -4.13720368e3, 5.29556871e3] * u.km,
        [7.37289205, 2.08223573, 4.39999794e-1] * u.km / u.s,
        time.Time("2013-03-18 12:00", scale="utc"),
    )
    testOrbit1 = TestEarthSatellite(testBody1, None)

    t_span = time_range(
        iss.epoch - 1.5 * u.h, num_values=150, end=iss.epoch + 1.5 * u.h
    )

    # Plot previously defined EarthSatellite object, no error should occur
    gp.plot(
        iss_spacecraft,
        t_span,
        label="ISS",
        color="red",
        marker={
            "size": 10,
            "symbol": "triangle-right",
            "line": {"width": 1, "color": "black"},
        },
    )

    # plot orbit around Mars, should raise an execption as it is not Earth
    with pytest.raises(ValueError) as excinfo:
        gp.plot(
            testOrbit1,
            t_span,
            label="Test1",
            color="orange",
            marker={
                "size": 10,
                "symbol": "triangle-right",
                "line": {"width": 1, "color": "black"},
            },
        )
    assert "Satellite should be orbiting Earth" in excinfo.exconly()
