import manager.globals.constants

from setuptools import setup
from setuptools import find_packages

def getLongDescription():
	"""
	This definition returns the Package long description.

	:return: Package long description. ( String )
	"""

	description = str()
	with open("README.rst") as file:
		for line in file:
			if ".. code:: python" in line:
				continue

			description += line
	return description

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
	install_requires=["Foundations>=2.0.2"],
	classifiers=["Development Status :: 5 - Production/Stable",
				"Environment :: Console",
				"Intended Audience :: Developers",
				"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
				"Natural Language :: English",
				"Operating System :: OS Independent",
				"Programming Language :: Python :: 2.7",
				"Topic :: Utilities"])
