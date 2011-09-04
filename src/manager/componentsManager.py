#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**manager.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines the :class:`Manager` class and others helper objects.

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import inspect
import logging
import os
import sys
import re

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
import foundations.core as core
import foundations.exceptions
import foundations.strings
import manager.exceptions
from foundations.parser import Parser
from foundations.walker import Walker
from manager.component import Component
from manager.globals.constants import Constants
from manager.uiComponent import UiComponent

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "Components", "Profile", "Manager"]

LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class Components(core.Structure):
	"""
	This class represents a storage object for :class:`Manager` class Components.
	"""

	@core.executionTrace
	def __init__(self, **kwargs):
		"""
		This method initializes the class.

		:param \*\*kwargs: Arguments. ( Key / Value pairs )
		"""

		core.Structure.__init__(self, **kwargs)

class Profile(object):
	"""
	This class is used by the :class:`Manager` class to store Components informations and objects.
	"""

	@core.executionTrace
	def __init__(self, name=None, path=None):
		"""
		This method initializes the class.
		
		:param name: Name of the Component. ( String )
		:param path: Path of the Component. ( String )
		
		:Note: :class:`Profile` class attributes ( Except :meth:`Profile.name` and for :meth:`Profile.path` ) are initialized by the :meth:`Manager.getProfile` method.
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		# --- Setting class attributes. ---
		self.__name = None
		self.name = name
		self.path = None
		self.__path = path

		self.__object_ = None
		self.__rank = None
		self.__import = None
		self.__interface = None
		self.__categorie = None

		self.__module = None
		self.__version = None
		self.__author = None
		self.__email = None
		self.__url = None
		self.__description = None

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def name(self):
		"""
		This method is the property for **self.__name** attribute.

		:return: self.__name. ( String )
		"""

		return self.__name

	@name.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def name(self, value):
		"""
		This method is the setter method for **self.__name** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("name", value)
		self.__name = value

	@name.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def name(self):
		"""
		This method is the deleter method for **self.__name** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("name"))

	@property
	def path(self):
		"""
		This method is the property for **self.__path** attribute.

		:return: self.__path. ( String )
		"""

		return self.__path

	@path.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def path(self, value):
		"""
		This method is the setter method for **self.__path** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("path", value)
			assert os.path.exists(value), "'{0}' attribute: '{1}' directory doesn't exists!".format("path", value)
		self.__path = value

	@path.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def path(self):
		"""
		This method is the deleter method for **self.__path** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("path"))

	@property
	def object_(self):
		"""
		This method is the property for **self.__object_** attribute.

		:return: self.__object_. ( String )
		"""

		return self.__object_

	@object_.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def object_(self, value):
		"""
		This method is the setter method for **self.__object_** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("object_", value)
		self.__object_ = value

	@object_.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def object_(self):
		"""
		This method is the deleter method for **self.__object_** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("object_"))

	@property
	def rank(self):
		"""
		This method is the property for **self.__rank** attribute.

		:return: self.__rank. ( String )
		"""

		return self.__rank

	@rank.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def rank(self, value):
		"""
		This method is the setter method for **self.__rank** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("rank", value)
		self.__rank = value

	@rank.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def rank(self):
		"""
		This method is the deleter method for **self.__rank** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("rank"))

	@property
	def import_(self):
		"""
		This method is the property for **self.__import_** attribute.

		:return: self.__import. ( Module )
		"""

		return self.__import

	@import_.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def import_(self, value):
		"""
		This method is the setter method for **self.__import_** attribute.

		:param value: Attribute value. ( Module )
		"""

		if value:
			assert type(value) is type(sys), "'{0}' attribute: '{1}' type is not 'module'!".format("import", value)
		self.__import = value

	@import_.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def import_(self):
		"""
		This method is the deleter method for **self.__import_** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("import"))

	@property
	def interface(self):
		"""
		This method is the property for **self.__interface** attribute.

		:return: self.__interface. ( Object )
		"""

		return self.__interface

	@interface.setter
	def interface(self, value):
		"""
		This method is the setter method for **self.__interface** attribute.

		:param value: Attribute value. ( Object )
		"""

		self.__interface = value

	@interface.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def interface(self):
		"""
		This method is the deleter method for **self.__interface** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("interface"))

	@property
	def categorie(self):
		"""
		This method is the property for **self.__categorie** attribute.

		:return: self.__categorie. ( String )
		"""

		return self.__categorie

	@categorie.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def categorie(self, value):
		"""
		This method is the setter method for **self.__categorie** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("categorie", value)
		self.__categorie = value

	@categorie.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def categorie(self):
		"""
		This method is the deleter method for **self.__categorie** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("categorie"))

	@property
	def module(self):
		"""
		This method is the property for **self.__module** attribute.

		:return: self.__module. ( String )
		"""

		return self.__module

	@module.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def module(self, value):
		"""
		This method is the setter method for **self.__module** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("module", value)
		self.__module = value

	@module.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def module(self):
		"""
		This method is the deleter method for **self.__module** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("module"))

	@property
	def version(self):
		"""
		This method is the property for **self.__version** attribute.

		:return: self.__version. ( String )
		"""

		return self.__version

	@version.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def version(self, value):
		"""
		This method is the setter method for **self.__version** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("version", value)
		self.__version = value

	@version.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def version(self):
		"""
		This method is the deleter method for **self.__version** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("version"))

	@property
	def author(self):
		"""
		This method is the property for **self.__author** attribute.

		:return: self.__author. ( String )
		"""

		return self.__author

	@author.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def author(self, value):
		"""
		This method is the setter method for **self.__author** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("author", value)
		self.__author = value

	@author.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def author(self):
		"""
		This method is the deleter method for **self.__author** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("author"))

	@property
	def email(self):
		"""
		This method is the property for **self.__email** attribute.

		:return: self.__email. ( String )
		"""

		return self.__email

	@email.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def email(self, value):
		"""
		This method is the setter method for **self.__email** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("email", value)
		self.__email = value

	@email.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def email(self):
		"""
		This method is the deleter method for **self.__email** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("email"))

	@property
	def url(self):
		"""
		This method is the property for **self.__url** attribute.

		:return: self.__url. ( String )
		"""

		return self.__url

	@url.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def url(self, value):
		"""
		This method is the setter method for **self.__url** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("url", value)
		self.__url = value

	@url.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def url(self):
		"""
		This method is the deleter method for **self.__url** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("url"))

	@property
	def description(self):
		"""
		This method is the property for **self.__description** attribute.

		:return: self.__description. ( String )
		"""

		return self.__description

	@description.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def description(self, value):
		"""
		This method is the setter method for **self.__description** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("description", value)
		self.__description = value

	@description.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def description(self):
		"""
		This method is the deleter method for **self.__description** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("description"))

class Manager(object):
	"""
	| This class defines methods to manage Components, allowing Components registration / unregistration, instantiation and reloading.
	| The Components can be registered in mass by providing paths that are recursively walk for candidates or simply by calling the registration method on a provided Component file.
	| When a Component is registered, a Profile ( Stored using the :class:`Profile` class ) is built and associated to it, this Profile object contains the Component Interface and various description attributes. 
	"""

	@core.executionTrace
	def __init__(self, paths=None, extension="rc", categories={ "default" : Component, "ui" : UiComponent }):
		"""
		This method initializes the class.

		Usage::

			>>> manager = Manager(("./Manager/src/tests/testsManager/resources/components/core",))
			>>> manager.registerComponents()
			True
			>>> manager.getComponents()
			['core.testsComponentA', 'core.testsComponentB']
			>>> manager.instantiateComponents()
			True
			>>> manager.getInterface("core.testsComponentA")
			<testsComponentA.TestsComponentA object at 0x11dd990>

		:param paths: Paths to walk. ( Tuple / List )
		:param extension: Components file extension. ( String )
		:param categories: Components categories. ( Dictionary )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		# --- Setting class attributes. ---
		self.__paths = None
		self.paths = paths
		self.__extension = None
		self.extension = extension
		self.__categories = None
		self.categories = categories
		self.__components = Components()

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def paths(self):
		"""
		This method is the property for **self.__paths** attribute.

		:return: self.__paths. ( Tuple / List )
		"""

		return self.__paths

	@paths.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def paths(self, value):
		"""
		This method is the setter method for **self.__paths** attribute.

		:param value: Attribute value. ( Tuple / List )
		"""

		if value:
			assert type(value) in (tuple, list), "'{0}' attribute: '{1}' type is not 'tuple' or 'list'!".format("paths", value)
			for path in value: assert os.path.exists(path), "'{0}' attribute: '{1}' directory doesn't exists!".format("paths", path)
		self.__paths = value

	@paths.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def paths(self):
		"""
		This method is the deleter method for **self.__paths** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("paths"))

	@property
	def extension(self):
		"""
		This method is the property for **self.__extension** attribute.

		:return: self.__extension. ( String )
		"""

		return self.__extension

	@extension.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def extension(self, value):
		"""
		This method is the setter method for **self.__extension** attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("extension", value)
		self.__extension = value

	@extension.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def extension(self):
		"""
		This method is the deleter method for **self.__extension** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("extension"))

	@property
	def categories(self):
		"""
		This method is the property for **self.__categories** attribute.

		:return: self.__categories. ( Dictionary )
		"""

		return self.__categories

	@categories.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def categories(self, value):
		"""
		This method is the setter method for **self.__categories** attribute.

		:param value: Attribute value. ( Dictionary )
		"""

		if value:
			assert type(value) is dict, "'{0}' attribute: '{1}' type is not 'dict'!".format("categories", value)
		self.__categories = value

	@categories.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def categories(self):
		"""
		This method is the deleter method for **self.__categories** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("categories"))

	@property
	def components(self):
		"""
		This method is the property for **self.__components** attribute.

		:return: self.__components. ( Dictionary )
		"""

		return self.__components

	@components.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def components(self, value):
		"""
		This method is the setter method for **self.__components** attribute.

		:param value: Attribute value. ( Dictionary )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("components"))

	@components.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def components(self):
		"""
		This method is the deleter method for **self.__components** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("components"))

	#***********************************************************************************************
	#***	Class methods.
	#***********************************************************************************************
	@staticmethod
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.FileStructureParsingError)
	def getProfile(file):
		"""
		This method gets provided Component Profile.
		
		Usage::

			>>> profile = Manager.getProfile("./Manager/src/tests/testsManager/resources/components/core/testsComponentA/testsComponentA.rc")
			>>> profile.description
			Core tests Component A.

		:param file: File path. ( String )
		:return: Profile. ( Profile )
		"""

		LOGGER.debug("> Building '{0}' profile.".format(file))

		parser = Parser(file)
		parser.read() and parser.parse()

		if parser.sections:
			profile = Profile()
			profile.path = os.path.dirname(file)
			profile.name = parser.attributeExists("Name", "Component") and parser.getValue("Name", "Component") or None
			if not profile.name:
				raise foundations.exceptions.FileStructureParsingError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Name"))
			profile.path = os.path.dirname(file)
			profile.module = parser.attributeExists("Module", "Component") and parser.getValue("Module", "Component") or None
			if not profile.module:
				raise foundations.exceptions.FileStructureParsingError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Module"))
			profile.object_ = parser.attributeExists("Object", "Component") and parser.getValue("Object", "Component") or None
			if not profile.object_:
				raise foundations.exceptions.FileStructureParsingError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Object"))
			profile.rank = parser.attributeExists("Rank", "Component") and parser.getValue("Rank", "Component") or None
			if not profile.rank:
				raise foundations.exceptions.FileStructureParsingError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Rank"))
			profile.version = parser.attributeExists("Version", "Component") and parser.getValue("Version", "Component") or None
			if not profile.version:
				raise foundations.exceptions.FileStructureParsingError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Version"))
			profile.author = parser.attributeExists("Author", "Informations") and parser.getValue("Author", "Informations") or None
			profile.email = parser.attributeExists("Email", "Informations") and parser.getValue("Email", "Informations") or None
			profile.url = parser.attributeExists("Url", "Informations") and parser.getValue("Url", "Informations") or None
			profile.description = parser.attributeExists("Description", "Informations") and parser.getValue("Description", "Informations") or None

			return profile
		else:
			raise foundations.exceptions.FileStructureParsingError("'{0}' no sections found, file structure seems invalid!".format(file))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, manager.exceptions.ComponentModuleError, manager.exceptions.ComponentProfileError)
	def registerComponent(self, path):
		"""
		This method registers provided component.

		Usage::

			>>> manager = Manager()
			>>> manager.registerComponent("./Manager/src/tests/testsManager/resources/components/core/testsComponentA/testsComponentA.rc")
			True
			>>> manager.components
			{'core.testsComponentA': <manager.componentsManager.Profile object at 0x11c9eb0>}

		:param path: Component path. ( String )
		:return: Method success. ( Boolean )
		"""

		component = foundations.strings.getSplitextBasename(path)
		LOGGER.debug("> Current Component: '{0}'.".format(component))
		profile = self.getProfile(path)
		if profile:
			if os.path.isfile(os.path.join(profile.path, profile.module) + ".py") or os.path.isdir(os.path.join(profile.path, profile.module)) or os.path.basename(profile.path) == profile.module:
				self.__components[profile.name] = profile
				return True
			else:
				raise manager.exceptions.ComponentModuleError("'{0}' has no associated module and has been rejected!".format(component))
		else:
			raise manager.exceptions.ComponentProfileError("'{0}' is not a valid Component and has been rejected!".format(component))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def unregisterComponent(self, component):
		"""
		This method unregisters provided Component.

		.. warning::

			The :class:`Manager` class is not responsible of any deactivation / cleanup actions and will not trigger anything while unregistering a Component.
	
		Usage::

			>>> manager = Manager()
			>>> manager.registerComponent("./Manager/src/tests/testsManager/resources/components/core/testsComponentA/testsComponentA.rc")
			True
			>>> manager.unregisterComponent("core.testsComponentA")
			True
			>>> manager.components
			{}

		:param component: Component to remove. ( String )
		:return: Method success. ( Boolean )
		"""

		del(self.__components[component])
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, manager.exceptions.ComponentRegistrationError)
	def registerComponents(self):
		"""
		This method registers the Components.

		Usage::

			>>> manager = Manager(("./Manager/src/tests/testsManager/resources/components/core",))
			>>> manager.registerComponents()
			True
			>>> manager.components.keys()
			['core.testsComponentA', 'core.testsComponentB']
		
		:return: Method success. ( Boolean )
		"""

		walker = Walker()
		unregisteredComponents = []
		for path in self.paths:
			walker.root = path
			walker.walk(("\.{0}$".format(self.__extension),), ("\._",))
			for file in walker.files.values():
				if not self.registerComponent(file):
					unregisteredComponents.append(file)

		if not unregisteredComponents:
			return True
		else:
			raise manager.exceptions.ComponentRegistrationError("'{0}' Components failed to register!".format(", ".join(unregisteredComponents)))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def unregisterComponents(self):
		"""
		This method unregisters the Components.

		.. warning::

			The :class:`Manager` class is not responsible of any deactivation / cleanup actions and will not trigger anything while unregistering a Component.
	
		Usage::

			>>> manager = Manager(("./Manager/src/tests/testsManager/resources/components/core",))
			>>> manager.registerComponents()
			True
			>>> manager.unregisterComponents()
			True
			>>> manager.components
			{}

		:return: Method success. ( Boolean )
		"""

		self.__components.clear()
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, ImportError, manager.exceptions.ComponentInterfaceError)
	def instantiateComponent(self, component, callback=None):
		"""
		This method instantiates provided Component.

		Usage::

			>>> manager = Manager()
			>>> manager.registerComponent("./Manager/src/tests/testsManager/resources/components/core/testsComponentA/testsComponentA.rc")
			True
			>>> manager.instantiateComponent("core.testsComponentA")
			True
			>>> manager.getInterface("core.testsComponentA")
			<testsComponentA.TestsComponentA object at 0x17a5b90>

		:param component: Component to instantiate. ( String )
		:param callback: Callback object. ( Object )
		"""

		profile = self.__components[component]
		callback and callback(profile)

		LOGGER.debug("> Current Component: '{0}'.".format(component))

		if os.path.isfile(os.path.join(profile.path, profile.module) + ".py") or os.path.isdir(os.path.join(profile.path, profile.module)):
			path = profile.path
		elif os.path.basename(profile.path) == profile.module:
			path = os.path.join(profile.path, "..")
		not path in sys.path and sys.path.append(path)

		profile.import_ = __import__(profile.module)
		object_ = profile.object_ in profile.import_.__dict__ and getattr(profile.import_, profile.object_) or None
		if object_ and inspect.isclass(object_):
			for categorie, type in self.__categories.items():
				profile.categorie = categorie
				profile.interface = issubclass(object_, type) and object_ is not type and object_(name=profile.name) or None
				if profile.interface:
					LOGGER.info("{0} | '{1}' Component has been instantiated!".format(self.__class__.__name__, profile.name))
					return True
		else:
			del(self.__components[component])
			raise manager.exceptions.ComponentInterfaceError("'{0}' Component has no Interface and has been rejected!".format(profile.name))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False)
	def instantiateComponents(self, callback=None):
		"""
		This method instantiates the Components.

		Usage::

			>>> manager = Manager(("./Manager/src/tests/testsManager/resources/components/core",))
			>>> manager.registerComponents()
			True
			>>> manager.instantiateComponents()
			True
			>>> manager.getInterface("core.testsComponentA")
			<testsComponentA.TestsComponentA object at 0x17a5bb0>

		:param callback: Callback object. ( Object )
		"""

		uninstantiatedComponents = [component for component in self.getComponents() if not self.instantiateComponent(component, callback)]
		if not uninstantiatedComponents:
			return True
		else:
			raise manager.exceptions.ComponentInstantiationError("'{0}' Components failed to instantiate!".format(", ".join(uninstantiatedComponents)))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, ImportError)
	def reloadComponent(self, component):
		"""
		This method reload provided Component module.

		Usage::

			>>> manager = Manager()
			>>> manager.registerComponent("./Manager/src/tests/testsManager/resources/components/core/testsComponentA/testsComponentA.rc")
			True
			>>> manager.instantiateComponent("core.testsComponentA")
			True
			>>> manager.getInterface("core.testsComponentA")
			<testsComponentA.TestsComponentA object at 0x17b4890>
			>>> manager.reloadComponent("core.testsComponentA")
			True
			>>> manager.getInterface("core.testsComponentA")
			<testsComponentA.TestsComponentA object at 0x17b0d70>

		:return: Reload success. ( Boolean )
		"""

		profile = self.__components[component]
		import_ = __import__(profile.module)
		reload(import_)
		object_ = profile.object_ in dir(import_) and getattr(import_, profile.object_) or None
		if object_ and inspect.isclass(object_):
			interface = issubclass(object_, self.__categories[profile.categorie]) and object_ is not self.__categories[profile.categorie] and object_(name=profile.name) or None
			if not interface:
				return

			LOGGER.info("{0} | '{1}' Component has been reloaded!".format(self.__class__.__name__, profile.name))
			profile.import_ = import_
			profile.interface = interface
			return True

	@core.executionTrace
	def getComponents(self):
		"""
		This method gets the Components by ranking.

		Usage::

			>>> manager = Manager(("./Manager/src/tests/testsManager/resources/components/core",))
			>>> manager.registerComponents()
			True
			>>> manager.components["core.testsComponentA"].rank
			'10'
			>>> manager.components["core.testsComponentB"].rank
			'20'
			>>> manager.getComponents()
			['core.testsComponentA', 'core.testsComponentB']

		"""

		return [component[0] for component in sorted(((component, profile.rank) for component, profile in self.__components.items()), key=lambda x:(int(x[1])))]

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def filterComponents(self, pattern, categorie=None):
		"""
		This method filters the Components using provided regex pattern.

		Usage::

			>>> manager = Manager(("./Manager/src/tests/testsManager/resources/components/core",))
			>>> manager.registerComponents()
			True
			>>> manager.filterComponents("\w+A$")
			['core.testsComponentA']

		:param pattern: Regex filtering pattern. ( String )
		:param categorie: Categorie filter. ( String )
		:return: Matching items. ( List )
		"""

		matchingItems = []
		for component, profile in self.__components.items():
			if categorie:
				if profile.categorie != categorie:
					continue

			if re.search(pattern, component):
				matchingItems.append(component)
		return matchingItems

	@core.executionTrace
	def getInterface(self, component):
		"""
		This method gets provided Component interface.

		Usage::

			>>> manager = Manager()
			>>> manager.registerComponent("./Manager/src/tests/testsManager/resources/components/core/testsComponentA/testsComponentA.rc")
			True
			>>> manager.getInterface("core.testsComponentA")
			<testsComponentA.TestsComponentA object at 0x17b0d70>

		:param component: Component to get the interface. ( Component / UiComponent )
		:return: Component interface. ( Object )
		"""

		components = self.filterComponents(r"^{0}$".format(component))
		if components != []:
			return self.__components[components[0]].interface

	@staticmethod
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def getComponentAttributeName(component):
		"""
		This method gets provided Component attribute name.

		Usage::

			>>> Manager.getComponentAttributeName("factory.componentsManagerUi")
			'coreComponentsManagerUi'

		:param component: Component to get the attribute name. ( String )
		:return: Component attribute name. ( Object )
		"""

		search = re.search("(?P<categorie>\w+)\.(?P<name>\w+)", component)
		if search:
			name = "{0}{1}{2}".format(search.group("categorie"), search.group("name")[0].upper(), search.group("name")[1:])
			LOGGER.debug("> Component name: '{0}' to attribute name Active_QLabel: '{1}'.".format(component, name))
		else:
			name = component
		return name
