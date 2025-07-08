# What's new

## boinor 0.19.0 (xx.xx.xxxx)

### Highlights

- Deprecating Python 3.9
- Version requires numpy 2.0.2

### Coverage

New tests have been added or improved all over the code.
The code coverage increased from 95.94% to XX.XX%.

### Bugs fixed

- Fix mee2rv(), which needs another parameter to correctly calculate equation 3b from the mentioned paper, see ({github}`boinor issue #1 <boinor/boinor#1>`)

### Pull requests

### Contributors

This is the complete list of the people that contributed to this
release, with a + sign indicating first contribution.

- Thorsten Alteholz



## boinor 0.18.7 (29.06.2025)

### Highlights

- Deprecating Python 3.8
- As numpy 2.0 does not work with Python 3.9, deprecation of Python 3.9 started.
- Taking care of most pylint issues (except some of too-many-* or *docstring).
- github funding body was added, don't hesitate to use it :-).
- Introduce vulture to get information about dead code.
- Introduce interrogate to get information about docstring usage.
- Fixing latex/pdf creation of documentation (Thorsten Alteholz and @MLopez-Ibanez).
- All jupyter notebooks can be built again.
- Modernize ruff setup by @MLopez-Ibanez.

### Coverage

New tests have been added or improved all over the code.
The code coverage increased from 91.45% to 95.94%.

### Bugs fixed

- Obtain FAIR badge ({github}`poliastro issue #1320 <poliastro/poliastro#1320>`).
- Unable to install poliastro through spyder ({github}`poliastro issue #1604 <poliastro/poliastro#1604>`).
- Jacchia77 (U.S Standard Atmosphere 1962) very likely broken (and untested) ({github}`poliastro issue #1562 <poliastro/poliastro#1562>`)
  This bug is not yet completely fixed, see ({github}`boinor issue #7 <boinor/boinor#7>`)
- Update matplotlib.py to use .get_next_color ({github}`hapsira issue #15 <pleiszenburg/hapsira#15>`).
- Fix units of return value of ClassicalState.to_equinoctial() and ModifiedEquinoctialState.to_value().
- Fix some typos detected by tests.

### Pull requests

- add cartesion_to_spherical ({github}`poliastro pull request #1365 <poliastro/poliastro#1365>`)
- no more pylint warning for super init not called on mixin class ({github}`poliastro pull request #1554 <poliastro/poliastro#1554>`)
- add argument to PorkchopPlotter.porkchop() to not draw plot ({github}`poliastro pull request #1589 <poliastro/poliastro#1589>`)
  the bug was not solved but the suggestion to unify the user experience with the PorkcopPlotter() has been implemented
- adding libration point calculation using newton raphson method ({github}`poliastro issue #1573 <poliastro/poliastro#1573>`)
- enable faster parallel testing ({github}`poliastro issue #1556 <poliastro/poliastro#1556>`)
- all PRs from poliastro are either merged, are not finished or are to old to cleanly apply
- Use correct spelling of Deimos ({github}`boinor issue #14 <boinor/boinor#14>`) created by @MLopez-Ibanez.
- Show Numpy 2.0 VisibleDecprecationWarnings ({github}`boinor issue #16 <boinor/boinor#16>`) supplied by @MLopez-Ibanez.

### Contributors

This is the complete list of the people that contributed to this
release, with a + sign indicating first contribution.

- Thorsten Alteholz
- @MLopez-Ibanez
- @s-m-e
- @mtryan83
- @DhruvJ22



## boinor 0.18.6

### Highlights

- **boinor**
  After poliastro has been archived, a fork has been created that is called **boinor*
  BOdies IN Orbit.
  Thanks a lot to [Juan Luis](https://github.com/astrojuanlu/), [Jorge Martinez](https://github.com/jorgepiloto/)
  and the poliastro development team for creating such a great software.
  Hopefully I can maintain their high standards so that this software keeps alive.

### Coverage

New tests have been added or improved:
 - tests/tests_core/test_core_elements.py

The code coverage increased from 91.1% to 91.45%.

### Bugs fixed

- add docstrings for constants ({github}`poliastro issue #1568 <poliastro/poliastro#1405>`)
- fix usage of time_range() in quickstart.md ({github}`poliastro issue #1639 <poliastro/poliastro#1639>`)
- fix errors of mee2rv() ({github}`poliastro issue #1638 <poliastro/poliastro#1638>`)
  This is only a partial fix for two of three mentioned bugs.
  Bug number 3 will be handled in {github}`boinor issue #1 <boinor/boinor#1>`.
- different order of parameter in documentation ({github}`poliastro issue #1634 <poliastro/poliastro#1634>`)
- add .pylintrc file ({github}`poliastro issue #1387 <poliastro/poliastro#1387>`)


### Contributors

This is the complete list of the people that contributed to this
release, with a + sign indicating first contribution.

- Thorsten Alteholz
- gaowutong
- Elle

## versions before

Earlier versions are released from poliastro and can be found
at https://github.com/poliastro/poliastro
