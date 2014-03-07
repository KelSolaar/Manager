#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**exceptions.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines **Manager** package exceptions. 

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.exceptions

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["AbstractComponentsManagerError",
			"ComponentProfileError",
			"ComponentModuleError",
			"ComponentRegistrationError",
			"ComponentInterfaceError",
			"ComponentInstantiationError",
			"ComponentActivationError",
			"ComponentDeactivationError",
			"ComponentReloadError",
			"ComponentExistsError"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class AbstractComponentsManagerError(foundations.exceptions.AbstractError):
	"""
	Defines the abstract base class for :class:`manager.componentsManager.Manager` related exceptions.
	"""

	pass

class ComponentProfileError(AbstractComponentsManagerError):
	"""
	Defines Component profile exceptions.
	"""

	pass

class ComponentModuleError(AbstractComponentsManagerError):
	"""
	Defines Component associated module exceptions.
	"""

	pass

class ComponentRegistrationError(AbstractComponentsManagerError):
	"""
	Defines Component registration exceptions.
	"""

	pass

class ComponentInterfaceError(AbstractComponentsManagerError):
	"""
	Defines Component Interface exceptions.
	"""

	pass

class ComponentInstantiationError(AbstractComponentsManagerError):
	"""
	Defines Component instantiation exceptions.
	"""

	pass

class ComponentActivationError(AbstractComponentsManagerError):
	"""
	Defines Component activation exceptions.
	"""

	pass

class ComponentDeactivationError(AbstractComponentsManagerError):
	"""
	Defines Component deactivation exceptions.
	"""

	pass

class ComponentReloadError(AbstractComponentsManagerError):
	"""
	Defines Component reload exceptions.
	"""

	pass

class ComponentExistsError(AbstractComponentsManagerError):
	"""
	Defines non existing Component exceptions.
	"""

	pass
