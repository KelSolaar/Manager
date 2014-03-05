#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsConstants.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines units tests for :mod:`manager.globals.constants` module.

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import sys
if sys.version_info[:2] <= (2, 6):
	import unittest2 as unittest
else:
	import unittest

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
from manager.globals.constants import Constants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["ConstantsTestCase"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class ConstantsTestCase(unittest.TestCase):
	"""
	Defines :class:`manager.globals.constants.Constants` class units tests methods.
	"""

	def testRequiredAttributes(self):
		"""
		Tests presence of required attributes.
		"""

		requiredAttributes = ("applicationName",
								"majorVersion",
								"minorVersion",
								"changeVersion",
								"releaseVersion",
								"logger",
								"verbosityLevel",
								"verbosityLabels",
								"loggingDefaultFormatter",
								"loggingSeparators",
								"defaultCodec",
								"codecError",
								"applicationDirectory",
								"providerDirectory",
								"nullObject")

		for attribute in requiredAttributes:
			self.assertIn(attribute, Constants.__dict__)

	def testApplicationNameAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.applicationName` attribute.
		"""

		self.assertRegexpMatches(Constants.applicationName, "\w+")

	def testMajorVersionAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.majorVersion` attribute.
		"""

		self.assertRegexpMatches(Constants.releaseVersion, "\d")

	def testMinorVersionAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.minorVersion` attribute.
		"""

		self.assertRegexpMatches(Constants.releaseVersion, "\d")

	def testChangeVersionAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.changeVersion` attribute.
		"""

		self.assertRegexpMatches(Constants.releaseVersion, "\d")

	def testReleaseVersionAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.releaseVersion` attribute.
		"""

		self.assertRegexpMatches(Constants.releaseVersion, "\d\.\d\.\d")

	def testLoggerAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.logger` attribute.
		"""

		self.assertRegexpMatches(Constants.logger, "\w+")

	def testVerbosityLevelAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.verbosityLevel` attribute.
		"""

		self.assertIsInstance(Constants.verbosityLevel, int)
		self.assertGreaterEqual(Constants.verbosityLevel, 0)
		self.assertLessEqual(Constants.verbosityLevel, 4)

	def testVerbosityLabelsAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.verbosityLabels` attribute.
		"""

		self.assertIsInstance(Constants.verbosityLabels, tuple)
		for label in Constants.verbosityLabels:
			self.assertIsInstance(label, unicode)

	def testLoggingDefaultFormatterAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.loggingDefaultFormatter` attribute.
		"""

		self.assertIsInstance(Constants.loggingDefaultFormatter, unicode)

	def testLoggingSeparatorsAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.loggingSeparators` attribute.
		"""

		self.assertIsInstance(Constants.loggingSeparators, unicode)

	def testDefaultCodecAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.defaultCodec` attribute.
		"""

		validEncodings = ("utf-8",
						"cp1252")

		self.assertIn(Constants.defaultCodec, validEncodings)

	def testEncodingErrorAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.codecError` attribute.
		"""

		validEncodingsErrors = ("strict",
							"ignore",
							"replace",
							"xmlcharrefreplace")

		self.assertIn(Constants.codecError, validEncodingsErrors)

	def testApplicationDirectoryAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.applicationDirectory` attribute.
		"""

		self.assertRegexpMatches(Constants.applicationDirectory, "\w+")

	def testProviderDirectoryAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.providerDirectory` attribute.
		"""

		self.assertRegexpMatches(Constants.providerDirectory, "\.*\w")

	def testNullObjectAttribute(self):
		"""
		Tests :attr:`manager.globals.constants.Constants.nullObject` attribute.
		"""

		self.assertRegexpMatches(Constants.nullObject, "\w+")

if __name__ == "__main__":
	unittest.main()
