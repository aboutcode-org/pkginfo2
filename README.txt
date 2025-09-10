``pkginfo2`` README
=====================

Homepage URL: https://github.com/aboutcode-org/pkginfo2
SPDX-License-Identifier: MIT

This package provides an API for querying the distutils metadata written in
the ``PKG-INFO`` file inside a source distriubtion (an ``sdist``) or a
binary distribution or a wheel (e.g., created by running ``bdist_egg``).  It can
also query the ``EGG-INFO`` directory of an installed distribution, and
the ``*.egg-info`` stored in a "development checkout"
(e.g, created by running ``setup.py develop``), or the ``*.dist-info`` from
an as-installed package.

This is a fork of http://bazaar.launchpad.net/~tseaver/pkginfo removing the
ability to import and eval arbitrary code and work with modules known to the
current interpreter. Use importlib_metadata for this if you need it.


Please see the `pkginfo2 repo at <https://github.com/aboutcode-org/pkginfo2>`_
for more documentation.
