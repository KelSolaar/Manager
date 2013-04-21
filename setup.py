#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**setup.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	`https://pypi.python.org/pypi/Manager <https://pypi.python.org/pypi/Manager>`_ package setup file.

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***	Encoding manipulations.
#**********************************************************************************************************************
import sys

def _setEncoding():
	"""
	This definition sets the Application encoding.
	"""

	reload(sys)
	sys.setdefaultencoding("utf-8")

_setEncoding()

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import re
from setuptools import setup
from setuptools import find_packages

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import manager.globals.constants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2013 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["getLongDescription"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
def getLongDescription():
	"""
	This definition returns the Package long description.

	:return: Package long description. ( String )
	"""

	description = []
	with open("README.rst") as file:
		for line in file:
			if ".. code:: python" in line and len(description) >= 2:
				blockLine = description[-2]
				if re.search(r":$", blockLine) and not re.search(r"::$", blockLine):
					description[-2] = "::".join(blockLine.rsplit(":", 1))
				continue

			description.append(line)
	return "".join(description)

setup(name=manager.globals.constants.Constants.applicationName,
	version=manager.globals.constants.Constants.releaseVersion,
	author=manager.globals.constants.__author__,
	author_email=manager.globals.constants.__email__,
	include_package_data=True,
	packages=find_packages(),
	scripts=[],
	url="https://github.com/KelSolaar/Manager",
	license="GPLv3",
	description="Manager is the Components Manager package of Umbra, sIBL_GUI and sIBL_Reporter.",
	long_description=getLongDescription(),
	install_requires=["Foundations>=2.0.8"],
	classifiers=["Development Status :: 5 - Production/Stable",
				"Environment :: Console",
				"Intended Audience :: Developers",
				"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
				"Natural Language :: English",
				"Operating System :: OS Independent",
				"Programming Language :: Python :: 2.7",
				"Topic :: Utilities"])
