[![boinor Logo](https://raw.githubusercontent.com/boinor/boinor/main/docs/source/_static/logo_readme.png)](https://docs.boinor.space/en/stable/)

| **Name**  |                        **Website**                         |                                                         **Authors**                                                       |                                      **Maintainers**                                      |                     **Version**                      |
|:---------:|:----------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|:----------------------------------------------------:|
| boinor | [https://www.boinor.space](https://www.boinor.space) | [Thorsten Alteholz](https://orcid.org/0000-0002-9570-7046) | [boinor development team](https://github.com/boinor/boinor/blob/main/AUTHORS.md) | [0.19XXX](https://github.com/boinor/boinor/) |

[![boinor_badge]](https://github.com/boinor/boinor)
[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/9wE8FEEBmTs6KrznLADUmx/EX84xKHFPudDeazG3q2XVw/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/9wE8FEEBmTs6KrznLADUmx/EX84xKHFPudDeazG3q2XVw/tree/main)
[![license_badge]](https://opensource.org/licenses/MIT)
[![python_badge]](https://pypi.org/project/boinor) 
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/boinor/boinor/main.svg)](https://results.pre-commit.ci/latest/github/boinor/boinor/main)
[![code_badge]]()
[![pypi_badge]](https://pypi.org/project/boinor) 
[![mailing_badge]](https://groups.io/g/boinor-dev) 
[![docs_badge]](https://readthedocs.org/projects/boinor/badge/?version=latest)
[![coverage_badge]](https://codecov.io/github/boinor/boinor?branch=main) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12809725.svg)](https://doi.org/10.5281/zenodo.12809725)

<!--
[![backers_badge]](https://opencollective.com/boinor/) 
[![sponsors_badge]](https://opencollective.com/boinor/) 
[![astropy_badge]](https://zenodo.org/badge/latestdoi/11178845) 
[![chat_badge]](http://chat.boinor.space/) 
[![binder_badge]](https://mybinder.org/v2/gh/boinor/boinor/main?labpath=index.ipynb) 
-->


boinor is an open source ([MIT](#License)) pure Python library for interactive
Astrodynamics and Orbital Mechanics, with a focus on ease of use, speed, and
quick visualization. It provides a simple and intuitive API, and handles
physical quantities with units.

Some features include orbit propagation, solution of the Lambert\'s problem,
conversion between position and velocity vectors and classical orbital elements
and orbit plotting, among others.  It focuses on interplanetary applications,
but can also be used to analyze artificial satellites in Low-Earth Orbit (LEO).

If you use boinor on your project, please [let us know]. Use the DOI to cite
boinor in your publications:

    Juan Luis Cano Rodríguez, Jorge Martinez, et al.. (2023). boinor: boinor 0.17.0. Zenodo. 10.5281/zenodo.6817189

![Multiple examples image](https://github.com/boinor/boinor/raw/main/docs/source/_static/examples.png)
-->

## Requirements

boinor requires the following Python packages:

- [numpy](https://numpy.org/) for basic numerical routines
- [astropy](https://www.astropy.org/) for physical units and time handling
- [numba](https://numba.pydata.org/) for accelerating the code
- [jplephem](https://github.com/brandon-rhodes/python-jplephem) for the planetary ephemerides using SPICE kernels
- [matplotlib](https://matplotlib.org/) for orbit plotting
- [plotly](https://plotly.com/) for 2D and 3D interactive orbit plotting
- [scipy](https://scipy.org/) for root finding and numerical propagation

boinor is supported on Linux, macOS and Windows on Python 3.9 to 3.12.

## Installation

Multiple installation methods are supported by boinor, including:

|                             **Logo**                              | **Platform** |                                    **Command**                                    |
|:-----------------------------------------------------------------:|:------------:|:---------------------------------------------------------------------------------:|
|       ![PyPI logo](https://simpleicons.org/icons/pypi.svg)        |     PyPI     |                        ``python -m pip install boinor``                        |
| ![Conda Forge logo](https://simpleicons.org/icons/condaforge.svg) | Conda Forge  |                 ``conda install boinor --channel conda-forge``                 |
|     ![GitHub logo](https://simpleicons.org/icons/github.svg)      |    GitHub    | ``python -m pip install https://github.com/boinor/boinor/archive/main.zip`` |

For other installation methods, see the [alternative installation methods].


## Documentation

Complete documentation, including a [quickstart guide] and an [API reference], can
be read on the wonderful [Read the Docs]. Multi-version documentation includes:

* [Development documentation](https://docs.boinor.space/en/latest/)
* [Stable documentation](https://docs.boinor.space/en/stable/)


## Examples, background and talks

There is a great variety of examples demostrating the capabilities of
boinor. Examples can be accessed in various ways:

* Examples source code collected in the [examples directory]
* Rendered [gallery of examples] presented in the documentation
<!--
* Interactive examples powered by [binder] so users can try boinor without installing it
-->

<!--
boinor is also promoted through conferences and talks. These are the latest
talks in some of the most popular conferences about scientific software:

| **Conference**  |                                                                                                  **Talk**                                                                                                   |
|:---------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|   SciPy 2022    |                                                [Per Python ad astra: Interactive Astrodynamics with boinor](https://www.youtube.com/watch?v=0GqdIRdDe9c)                                                 |
|   OSCW  2019    |                                                        [Interplanetary mission analysis with boinor](https://www.youtube.com/watch?v=0GqdIRdDe9c)                                                        |
| EuroSciPy 2019  | [Can we make Python fast without sacrificing readability? numba for Astrodynamics](https://pyvideo.org/euroscipy-2019/can-we-make-python-fast-without-sacrificing-readability-numba-for-astrodynamics.html) |
| EuroPython 2016 |                                                             [Per Python ad Astra](https://pyvideo.org/europython-2016/per-python-ad-astra.html)                                                             |
-->

## License

boinor is released under the MIT license, hence allowing commercial use of
the library. Please refer to the [COPYING] file.

    The MIT License (MIT)
    
    Copyright (c) 2012-2023 Juan Luis Cano Rodríguez, Jorge Martínez Garrido, and the poliastro development team
    Copyright (c) 2024-2025 Thorsten Alteholz, and the boinor development team
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

If you are planning to use boinor with commercial purposes consider
[sponsoring the project](#Backers-and-sponsors).


## Problems and suggestions

If for any reason you get an unexpected error message or an incorrect result,
or you want to let the developers know about your use case, please open a new
issue in the [issue tracker] and we will try to answer promptly.

## Contributing and community support

This project exists thanks to all the people who contribute! boinor is a
community project, hence all contributions are more than welcome! For more
information, head to the [CONTRIBUTING.md] file.

Release announcements and general discussion take place on our [mailing list].

<!--
For further clarifications and discussions, feel free to join boinor's [chat
room].
-->


## Backers and sponsors

boinor requires finnacial support to mantain its high quality standars. The
money is used to renew the web domain and updating the documentation hosting
subscription among others.

<!--
If you would like to support boinor, consider [becoming a backer] or
[becoming a sponsor]. 

**Thanks to all our backers!**

[![Backers](https://opencollective.com/boinor/backers.svg?width=890)](https://opencollective.com/boinor#backer)


**Thanks to all our sponsors!**
-->


## Frequently asked questions

* **What's up with the name?**

  boinor comes from BOdies IN ORbit.

* **Is boinor validated?**

  Yes! boinor is a community project that strives to be easy to use, while at
  the same time producing correct results [that are validated] against other
  [commonly used Astrodynamics software] such as GMAT and Orekit.

* **Can I suggest new features for boinor?**

  Sure, we encourage you to [open an issue] so we can discuss future feature
  additions!

* **What's the future of the project?**

  boinor is actively maintained and receiving an influx of new contributors
  thanks to the generous sponsorship of Google, the European Space Agency, and
  NumFOCUS. The best way to get an idea of the roadmap is to see the
  [milestones] of the project.

<!-- LINKS AND REFERENCES -->

[quickstart guide]: https://docs.boinor.space/en/stable/quickstart.html
[API reference]: https://docs.boinor.space/en/latest/api.html
[Read the docs]: https://readthedocs.org
[binder]: https://mybinder.org/
[alternative installation methods]: https://docs.boinor.space/en/stable/installation.html#alternative-installation-methods
[issue tracker]: https://github.com/boinor/boinor/issues 
[CONTRIBUTING.md]: https://github.com/boinor/boinor/blob/main/CONTRIBUTING.md
[COPYING]: https://github.com/boinor/boinor/blob/main/COPYING
[mailing list]: https://groups.io/g/boinor-dev
[chat room]: http://chat.boinor.space/
[let us know]: mailto:hello@juanlu.space
[examples directory]: https://github.com/boinor/boinor/tree/main/docs/source/examples
[become a sponsor]: https://opencollective.com/boinor/sponsor/0/website
[docs_stable]: https://docs.boinor.space/en/stable/
[docs_latest]: https://docs.boinor.space/en/latest/
[that are validated]: https://github.com/boinor/validation/
[commonly used Astrodynamics software]: https://docs.boinor.space/en/stable/related.html
[open an issue]: https://github.com/boinor/validation/issues/new
[milestones]: https://github.com/boinor/boinor/milestones
[Want to be a backer]: https://opencollective.com/boinor#backer
[gallery of examples]: https://docs.boinor.space/en/latest/gallery.html
[becoming a backer]: https://opencollective.com/boinor#backer
[becoming a sponsor]: https://opencollective.com/boinor#sponsor
[acknowledgement from the original author]: https://docs.boinor.space/en/stable/history.html#acknowledgement-from-the-original-author


<!-- Badges -->

<!--
[CircleCI_badge]: https://dl.circleci.com/status-badge/img/circleci/9wE8FEEBmTs6KrznLADUmx/EX84xKHFPudDeazG3q2XVw/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/9wE8FEEBmTs6KrznLADUmx/EX84xKHFPudDeazG3q2XVw/tree/main "CircleCI badge"
[orcid_badge]: https://img.shields.io/badge/id-0000--0002--2187--161X-a6ce39.svg "orcid badge"
-->

[python_badge]: https://img.shields.io/pypi/pyversions/boinor?logo=pypi&logoColor=white "python badge"
[license_badge]: https://img.shields.io/badge/license-MIT-blue.svg?logo=open%20source%20initiative&logoColor=white "license badge"

[boinor_badge]: https://img.shields.io/badge/boinor-gray.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAbxJREFUOE+Vk79LAmEYx7/njzulHKLQQIKwiyLuohykxqJBaHMNwvorcmltbG6LhnBqrMiWlmYl0SydaoqgwbLz9DS/B++heUI98A73vs/zfZ7n8zwndXsGF6tUKojFYvD7/W7Pzp00SiCXyyGTySCZTCKVSiEej7sKjRSgdzqdRq1WQzabRTQa/b8Ag8vlMsLhMBKJxN8F2u02LMtyAur1OqqFe+jaEsYi6oDQUAuGYcDn89nHsR7nq+N9zKxsQdvcGS3QbDYhyzJYQafTGSzZMvBQeoau61AUZXgKLJkTZaDX64XH40Gr1bIdKWqaJorFIjRNs995aE4LIjsdOXsGK9YT0HqHoawjEAggf3OJ2eUVBCcmnSoGBEQ2BsteA6juAY08unNn+HgN4fboEItqDAsHR6MF2B+rkMnwcRtov6E7fwGzM42781PEdQ2h1TV3AZInB6nX/8l1AbsbixhXJBgmUCqV7GWKRCJguwKk0wLhESQnEAwGcVd8wZTnE9+NLxuoqqo2B0mSHMgDEPnB0kmXDPp3gfesjHCZgFMRNrRIdKYxq9hGESgg9y+I68/EdsQOCGeKUPS3/QDL/fnRmszmsAAAAABJRU5ErkJggg== "boinor"
[ci_badge]: https://img.shields.io/circleci/build/gh/boinor/boinor/main?logo=CircleCi "ci badge"
[docs_badge]: https://img.shields.io/readthedocs/boinor/stable.svg?logo=read%20the%20docs&logoColor=white&label=docs&version=stable "docs badge"
[coverage_badge]:  https://img.shields.io/codecov/c/github/boinor/boinor.svg?logo=Codecov&logoColor=white "coverage badge"
[pre_commit_badge]: https://results.pre-commit.ci/badge/github/boinor/boinor/main.svg "pre-commit badge"
[doi_badge]: https://zenodo.org/badge/11178845.svg "doi badge" 
[astropy_badge]: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg "astropy badge"
[mailing_badge]: https://img.shields.io/badge/mailing%20list-groups.io-8cbcd1.svg 
[chat_badge]: https://img.shields.io/matrix/boinor:matrix.org.svg?logo=Matrix&logoColor=white "chat badge"
[backers_badge]: https://img.shields.io/opencollective/backers/boinor?logo=open%20collective&logoColor=white  "backers badge"
[sponsors_badge]: https://img.shields.io/opencollective/sponsors/boinor?logo=open%20collective&logoColor=white "sponsors badge"
[pypi_badge]: https://img.shields.io/pypi/v/boinor.svg?logo=Python&logoColor=white?labelColor=blue "pypi badge"
[code_badge]: https://img.shields.io/badge/Code%20style-black%20isort%20flake8-black "code badge"
[binder_badge]: https://img.shields.io/badge/Binder-examples-green.svg?logo=data:image/png;base64,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 "binder badge"
