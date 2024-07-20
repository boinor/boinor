"""The following script holds the different high level functions for the
different propagators available at boinor:

+-------------+------------+-----------------+-----------------+
|  Propagator | Elliptical |    Parabolic    |    Hyperbolic   |
+-------------+------------+-----------------+-----------------+
|  farnocchia |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|   vallado   |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|   mikkola   |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|   markley   |      ✓     |        x        |        x        |
+-------------+------------+-----------------+-----------------+
|   pimienta  |      ✓     |        ✓        |        x        |
+-------------+------------+-----------------+-----------------+
|   gooding   |      ✓     |        x        |        x        |
+-------------+------------+-----------------+-----------------+
|    danby    |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|    cowell   |      ✓     |        ✓        |        ✓        |
+-------------+------------+-----------------+-----------------+
|  recseries  |      ✓     |        x        |        x        |
+-------------+------------+-----------------+-----------------+

"""
from boinor.twobody.propagation.cowell import CowellPropagator
from boinor.twobody.propagation.danby import DanbyPropagator
from boinor.twobody.propagation.enums import PropagatorKind
from boinor.twobody.propagation.farnocchia import FarnocchiaPropagator
from boinor.twobody.propagation.gooding import GoodingPropagator
from boinor.twobody.propagation.markley import MarkleyPropagator
from boinor.twobody.propagation.mikkola import MikkolaPropagator
from boinor.twobody.propagation.pimienta import PimientaPropagator
from boinor.twobody.propagation.recseries import RecseriesPropagator
from boinor.twobody.propagation.vallado import ValladoPropagator

from ._compat import propagate

ALL_PROPAGATORS = [
    CowellPropagator,
    DanbyPropagator,
    FarnocchiaPropagator,
    GoodingPropagator,
    MarkleyPropagator,
    MikkolaPropagator,
    PimientaPropagator,
    RecseriesPropagator,
    ValladoPropagator,
]
ELLIPTIC_PROPAGATORS = [
    propagator
    for propagator in ALL_PROPAGATORS
    if propagator.kind & PropagatorKind.ELLIPTIC
]
PARABOLIC_PROPAGATORS = [
    propagator
    for propagator in ALL_PROPAGATORS
    if propagator.kind & PropagatorKind.PARABOLIC
]
HYPERBOLIC_PROPAGATORS = [
    propagator
    for propagator in ALL_PROPAGATORS
    if propagator.kind & PropagatorKind.HYPERBOLIC
]


__all__ = [item.__name__ for item in ALL_PROPAGATORS] + ["propagate"]
