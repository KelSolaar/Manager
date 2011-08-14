#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**exceptions.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines **Manager** package exceptions. 

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import logging

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
import foundations.core as core
import foundations.exceptions
from manager.globals.constants import Constants

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************

class AbstractComponentError(foundations.exceptions.AbstractError):
	"""
	This class is the abstract base class for Components related exceptions.
	"""

	pass

class ComponentProfileError(AbstractComponentError):
	"""
	This class is used for Component profile exceptions.
	"""

	pass

class ComponentModuleError(AbstractComponentError):
	"""
	This class is used for Component associated module exceptions.
	"""

	pass

class ComponentRegistrationError(AbstractComponentError):
	"""
	This class is used for Component registration exceptions.
	"""

	pass

class ComponentInterfaceError(AbstractComponentError):
	"""
	This class is used for Component interface exceptions.
	"""

	pass

class ComponentInstantiationError(AbstractComponentError):
	"""
	This class is used for Component instantiation exceptions.
	"""

	pass

class ComponentActivationError(AbstractComponentError):
	"""
	This class is used for Component activation exceptions.
	"""

	pass

class ComponentDeactivationError(AbstractComponentError):
	"""
	This class is used for Component deactivation exceptions.
	"""

	pass

class ComponentReloadError(AbstractComponentError):
	"""
	This class is used for Component reload exceptions.
	"""

	pass
