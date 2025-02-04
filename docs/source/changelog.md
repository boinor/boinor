# What's new

## boinor 0.17.0 - 2022-07-10

### Highlights

- **boinor at SciPy US 2022**:
  [Juan Luis](https://github.com/astrojuanlu/) and [Jorge](https://github.com/jorgepiloto/)
  have co-authored [a scientific paper about boinor] that will appear in the proceedings of
  the 21st annual Scientific Computing with Python conference (SciPy US 2022).
  In addition, Juan Luis will deliver a talk titled
  "Per Python ad astra: interactive Astrodynamics with boinor" at the conference.
  After almost a decade of work, it will be the first time that
  boinor is presented at the most important conference about Scientific Python.
- **Refactored propagators**:
  Propagation methods are no longer plain functions and have become classes instead.
  This allows them to share a common interface and perform more efficient calculations.
  For most users of {{ Orbit }} objects this should be invisible, unless you were using
  a custom propoagator: for example, to propagate using Cowell's method, you now have to write

```python
from boinor.twobody.propagation import CowellPropagator

new_orbit = orbit.propagate(1 << u.day, method=CowellPropagator())
```

- **New {py:meth}`~boinor.twobody.orbit.scalar.Orbit.to_ephem` to retrieve propagation time histories**:
  The {py:meth}`~boinor.twobody.orbit.scalar.Orbit.propagate` method that allows users to
  return a propagated {{ Orbit }} at a new epoch has been available in boinor for a very long time.
  However, many users were interested in retrieving the full time history of the propagation
  in the intermediate time steps, and historically boinor has struggled to provide a consistent API for it.
  The new {py:meth}`~boinor.twobody.orbit.scalar.Orbit.to_ephem` aims to replace the old
  `boinor.twobody.propagation.propagate` function, which was difficult to discover and too low-level.

[a scientific paper about boinor]: https://github.com/scipy-conference/scipy_proceedings/blob/2022/papers/juanluis_cano_boinor/juanluis_cano_boinor.rst

### New features

- New {py:meth}`~boinor.twobody.orbit.scalar.Orbit.to_ephem` method
  that generates an {{ Ephem }} instances from {{ Orbit }} objects using a variety of strategies
  available in {py:mod}`boinor.twobody.sampling`:
  minimum and maximum anomalies with {py:class}`~boinor.twobody.sampling.TrueAnomalyBounds`,
  minimum and maximum epochs with {py:class}`~boinor.twobody.sampling.EpochsBounds`,
  or explicit array of epochs with {py:class}`~boinor.twobody.sampling.EpochsArray`.
- The Lambert problem algorithms in {py:mod}`boinor.iod` now accept `prograde` and `lowpath`
  parameters to disambiguate solutions.
- New {py:class}`boinor.plotting.gabbard.GabbardPlotter` to plot
  [Gabbard diagrams](https://en.wiktionary.org/wiki/Gabbard_diagram):

```{image} _static/gabbard.png
---
align: center
---
```

- New recursive series Kepler solver for elliptical orbits
  {py:class}`boinor.twobody.propagation.RecseriesPropagator` based on Charls
  "Recursive solution to Kepler’s problem for elliptical orbits -
  application in robust Newton-Raphson and co-planar closest approach estimation".
- New {py:meth}`~boinor.twobody.orbit.scalar.Orbit.elevation` of {{ Orbit }} objects
  to determine the elevation of the object over a specific observation point on the attractor
  defined by latitude `lat` and longitude `theta`.
- New {py:meth}`boinor.earth.util.get_local_sidereal_time`.

In addition, we have new community-contributed scripts:

- [Circular restricted three-body problem](https://github.com/boinor/boinor/blob/main/contrib/CR3BP/CR3BP.py)

### Performance improvements

- Propagation now performs fewer unnecessary element conversions,
  and therefore should be slightly faster.

### Bugs fixed

- Compatibility with newer versions of astroquery ({github}`Issue #1405 <#1405>`)
- {py:class}`boinor.maneuver.Maneuver.lambert` sometimes generated negative times of flight
  and crashed ({github}`Issue #1397 <#1397>`)
- Attractor singletons now behave correctly upon pickling and unpickling
  ({github}`Issue #1395 <#1395>`)
- {py:meth}`boinor.earth.atmosphere.jacchia.Jacchia77.density()` returned value
  in incorrect units ({github}`Issue #1509 <#1509>`)
- `atmospheric_drag` had incorrect units in its docstring ({github}`Issue #1513 <#1513>`)
- `radiation_pressure` had incorrect units in its docstring ({github}`Issue #1515 <#1515>`)
- Typo in `coesa76` table ({github}`Issue #1518 <#1518>`)
- {py:class}`boinor.maneuver.Maneuver.lambert` had lousy time comparisons.
- {py:meth}`build_ephem_interpolant`

### Backwards incompatible changes

- The propagators in {py:mod}`boinor.twobody.propagation` are no longer functions, but classes:
  hence `cowell` becomes {py:class}`boinor.twobody.propagation.CowellPropagator`,
  `farnocchia` becomes {py:class}`boinor.twobody.propagation.FarnocchiaPropagator`, and so forth.
- The state classes in {py:mod}`boinor.twobody.states` no longer accept elements as keyword arguments,
  but instead they take 6-tuples.
- Interpolation methods in {py:mod}`boinor.ephem` are no longer enumeration values, but classes:
  hence `ephem.sample(method=InterpolationMethods.SPLINES)` becomes `ephem.sample(interpolator=SplineInterpolator())`.
- The Lambert problem methods in {py:mod}`boinor.iod` do not yield pairs of velocities anymore,
  and instead they always return departure and arrival velocity.
- Module `boinor.earth.sensors` was moved to {py:mod}`boinor.sensors`.

### Contributors

This is the complete list of the people that contributed to this
release, with a + sign indicating first contribution.

- Abhishek K. M.
- Andrew Mackie+
- Anish+
- Arnaud Muller+
- Carlosbogo
- Jero Bado
- John Reinert+
- Jorge Martínez Garrido
- Juan Luis Cano Rodríguez
- Kevin Charls+
- Luis Grau
- Ole Streicher
- Sebastian M. Ernst
- Tom Johnson+
- Tommaso Pino+
- TreshUp+
- Varenyam Bhardwaj+
- Yash Gondhalekar
