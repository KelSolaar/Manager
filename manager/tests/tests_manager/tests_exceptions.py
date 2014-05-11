#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_exceptions.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines units tests for :mod:`manager.exceptions` module.

**Others:**

"""

from __future__ import unicode_literals

import inspect
import sys
if sys.version_info[:2] <= (2, 6):
	import unittest2 as unittest
else:
	import unittest

import manager.exceptions

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["EXCEPTIONS", "TestExceptions"]

EXCEPTIONS = []

def _gather_exceptions():
	"""
	Gathers the exceptions.
	"""

	for attribute in dir(manager.exceptions):
		object = getattr(manager.exceptions, attribute)
		if not inspect.isclass(object):
			continue
		if issubclass(object, Exception):
			EXCEPTIONS.append(object)

_gather_exceptions()

class TestExceptions(unittest.TestCase):
	"""
	Defines :mod:`manager.exceptions` module exceptions classes units tests methods.
	"""

	def test_required_attributes(self):
		"""
		Tests presence of required attributes.
		"""

		required_attributes = ("value",)
		for exception in EXCEPTIONS:
			exception_instance = exception(None)
			for attribute in required_attributes:
				self.assertIn(attribute, dir(exception_instance))

	def test__str__(self):
		"""
		Tests exceptions classes **__str__** method.
		"""

		for exception in EXCEPTIONS:
			exception_instance = exception("{0} Exception raised!".format(exception.__class__))
			self.assertIsInstance(exception_instance.__str__(), str)
			exception_instance = exception([exception.__class__, "Exception raised!"])
			self.assertIsInstance(exception_instance.__str__(), str)
			exception_instance = exception(0)
			self.assertIsInstance(exception_instance.__str__(), str)

if __name__ == "__main__":
	unittest.main()
