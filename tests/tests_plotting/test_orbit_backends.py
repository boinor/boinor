"""tests related to module orbit_backends in sub-package plotting"""
import plotly.graph_objects as go
import pytest

from boinor.plotting.orbit.backends._base import OrbitPlotterBackend
from boinor.plotting.orbit.backends.plotly import (
    BasePlotly,
    Plotly2D,
    Plotly3D,
)

# even internal stuff needs to be tested
# pylint: disable=protected-access


class Dummy2D(BasePlotly):
    """dummy class to help with 2D plotting"""

    def __init__(self, figure, width=None, height=None):
        theme = "plotly_dark"

        # Declare the layout and attach it to the figure
        layout = go.Layout(
            autosize=True,
            width=width,
            height=height,
            xaxis={"constrain": "domain"},
            yaxis={"scaleanchor": "x"},
            template=theme,
        )
        super().__init__(figure, layout)


def test_orbit_backends_plotly():
    bp = Dummy2D(None)

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = bp.draw_impulse(1, color=2, label=3, size=4)  # just dummy parameter and not needed in this function

    x = (10.0, 11.1, 12.2)
    y = (20.1, 21.2, 22.3)
    z = (30.1, 31.2, 32.3)
    p2d = Plotly2D()
    v = p2d.draw_marker([x, y], color=2, label=None, marker_symbol="x", size=5)
    assert v.x == x
    assert v.y == y

    p3d = Plotly3D()
    v = p3d.draw_marker([x, y, z], color=2, label=None, marker_symbol="x", size=5)
    assert v.x == x
    assert v.y == y
    assert v.z == z

    # at the moment this does not give any exception
    _ = Dummy2D(None, width=234, height=345)
    with pytest.raises(
        ValueError,
        match="Invalid value of type 'builtins.str' received for the 'height' property of layout",
    ):
        _ = Dummy2D(None, width=234, height="nix da")


def test_orbit_backends_base():
    dummyScene = 1
    wrongName = "nothing"
    with pytest.raises(ValueError, match="Backend name must end with '2D' or '3D'."):
        opb = OrbitPlotterBackend(dummyScene, wrongName)

    goodName = "Matplotlib2D"
    opb = OrbitPlotterBackend(dummyScene, goodName)
    assert opb.is_3D is False

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb._get_colors("0x000000", False)  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_marker(
            1, color=2, label=3, marker_symbol=4, size=5
        )  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_position(1, color=2, label=3, size=4)  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_impulse(1, color=2, label=3, size=4)  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.draw_sphere(1, color=2, label=3, radius=4)  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a plotting backend class.",
    ):
        _ = opb.undraw_attractor()

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.draw_coordinates(1, colors=2, dashed=3, label=4)  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.draw_axes_labels_with_length_scale_units(1)  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.update_legend()

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.resize_limits()

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.generate_labels(1, 2, 3)  # just dummy parameter and not needed in this function

    with pytest.raises(
        NotImplementedError,
        match="This method is expected to be overridden by a specific plotting backend.",
    ):
        _ = opb.show()
