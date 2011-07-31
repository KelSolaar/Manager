#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**manager.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Manager Module.

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

LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class Profile(object):
	"""
	This class is the Profile class.
	"""

	@core.executionTrace
	def __init__(self, name=None, path=None):
		"""
		This method initializes the class.

		:param name: Name of the Component. ( String )
		:param path: Path of the Component. ( String )
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
		This method is the property for the __name attribute.

		:return: self.__name. ( String )
		"""

		return self.__name

	@name.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def name(self, value):
		"""
		This method is the setter method for the __name attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("name", value)
		self.__name = value

	@name.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def name(self):
		"""
		This method is the deleter method for the __name attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("name"))

	@property
	def path(self):
		"""
		This method is the property for the __path attribute.

		:return: self.__path. ( String )
		"""

		return self.__path

	@path.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def path(self, value):
		"""
		This method is the setter method for the __path attribute.

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
		This method is the deleter method for the __path attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("path"))

	@property
	def object_(self):
		"""
		This method is the property for the __object_ attribute.

		:return: self.__object_. ( String )
		"""

		return self.__object_

	@object_.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def object_(self, value):
		"""
		This method is the setter method for the __object_ attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("object_", value)
		self.__object_ = value

	@object_.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def object_(self):
		"""
		This method is the deleter method for the __object_ attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("object_"))

	@property
	def rank(self):
		"""
		This method is the property for the __rank attribute.

		:return: self.__rank. ( String )
		"""

		return self.__rank

	@rank.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def rank(self, value):
		"""
		This method is the setter method for the __rank attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("rank", value)
		self.__rank = value

	@rank.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def rank(self):
		"""
		This method is the deleter method for the __rank attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("rank"))

	@property
	def import_(self):
		"""
		This method is the property for the __import_ attribute.

		:return: self.__import. ( Module )
		"""

		return self.__import

	@import_.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def import_(self, value):
		"""
		This method is the setter method for the __import_ attribute.

		:param value: Attribute value. ( Module )
		"""

		if value:
			assert type(value) is type(sys), "'{0}' attribute: '{1}' type is not 'module'!".format("import", value)
		self.__import = value

	@import_.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def import_(self):
		"""
		This method is the deleter method for the __import_ attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("import"))

	@property
	def interface(self):
		"""
		This method is the property for the __interface attribute.

		:return: self.__interface. ( Object )
		"""

		return self.__interface

	@interface.setter
	def interface(self, value):
		"""
		This method is the setter method for the __interface attribute.

		:param value: Attribute value. ( Object )
		"""

		self.__interface = value

	@interface.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def interface(self):
		"""
		This method is the deleter method for the __interface attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("interface"))

	@property
	def categorie(self):
		"""
		This method is the property for the __categorie attribute.

		:return: self.__categorie. ( String )
		"""

		return self.__categorie

	@categorie.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def categorie(self, value):
		"""
		This method is the setter method for the __categorie attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("categorie", value)
		self.__categorie = value

	@categorie.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def categorie(self):
		"""
		This method is the deleter method for the __categorie attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("categorie"))

	@property
	def module(self):
		"""
		This method is the property for the __module attribute.

		:return: self.__module. ( String )
		"""

		return self.__module

	@module.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def module(self, value):
		"""
		This method is the setter method for the __module attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("module", value)
		self.__module = value

	@module.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def module(self):
		"""
		This method is the deleter method for the __module attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("module"))

	@property
	def version(self):
		"""
		This method is the property for the __version attribute.

		:return: self.__version. ( String )
		"""

		return self.__version

	@version.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def version(self, value):
		"""
		This method is the setter method for the __version attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("version", value)
		self.__version = value

	@version.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def version(self):
		"""
		This method is the deleter method for the __version attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("version"))

	@property
	def author(self):
		"""
		This method is the property for the __author attribute.

		:return: self.__author. ( String )
		"""

		return self.__author

	@author.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def author(self, value):
		"""
		This method is the setter method for the __author attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("author", value)
		self.__author = value

	@author.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def author(self):
		"""
		This method is the deleter method for the __author attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("author"))

	@property
	def email(self):
		"""
		This method is the property for the __email attribute.

		:return: self.__email. ( String )
		"""

		return self.__email

	@email.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def email(self, value):
		"""
		This method is the setter method for the __email attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("email", value)
		self.__email = value

	@email.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def email(self):
		"""
		This method is the deleter method for the __email attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("email"))

	@property
	def url(self):
		"""
		This method is the property for the __url attribute.

		:return: self.__url. ( String )
		"""

		return self.__url

	@url.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def url(self, value):
		"""
		This method is the setter method for the __url attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("url", value)
		self.__url = value

	@url.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def url(self):
		"""
		This method is the deleter method for the __url attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("url"))

	@property
	def description(self):
		"""
		This method is the property for the __description attribute.

		:return: self.__description. ( String )
		"""

		return self.__description

	@description.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def description(self, value):
		"""
		This method is the setter method for the __description attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("description", value)
		self.__description = value

	@description.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def description(self):
		"""
		This method is the deleter method for the __description attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("description"))

class Manager(object):
	"""
	This class is the Manager class.
	"""

	@core.executionTrace
	def __init__(self, paths=None, extension="rc", categories={ "default" : Component, "ui" : UiComponent }):
		"""
		This method initializes the class.
		:param paths: Paths to walk. ( Dictionary )
		:param extension: Extension to look after. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		# --- Setting class attributes. ---
		self.__paths = None
		self.paths = paths
		self.__extension = None
		self.extension = extension
		self.__categories = None
		self.categories = categories
		self.__components = None

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def paths(self):
		"""
		This method is the property for the __paths attribute.

		:return: self.__paths. ( Dictionary )
		"""

		return self.__paths

	@paths.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def paths(self, value):
		"""
		This method is the setter method for the __paths attribute.

		:param value: Attribute value. ( Dictionary )
		"""

		if value:
			assert type(value) is dict, "'{0}' attribute: '{1}' type is not 'dict'!".format("paths", value)
			for path in value.values(): assert os.path.exists(path), "'{0}' attribute: '{1}' directory doesn't exists!".format("paths", path)
		self.__paths = value

	@paths.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def paths(self):
		"""
		This method is the deleter method for the __paths attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("paths"))

	@property
	def extension(self):
		"""
		This method is the property for the __extension attribute.

		:return: self.__extension. ( String )
		"""

		return self.__extension

	@extension.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def extension(self, value):
		"""
		This method is the setter method for the __extension attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("extension", value)
		self.__extension = value

	@extension.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def extension(self):
		"""
		This method is the deleter method for the __extension attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("extension"))

	@property
	def categories(self):
		"""
		This method is the property for the __categories attribute.

		:return: self.__categories. ( Dictionary )
		"""

		return self.__categories

	@categories.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def categories(self, value):
		"""
		This method is the setter method for the __categories attribute.

		:param value: Attribute value. ( Dictionary )
		"""

		if value:
			assert type(value) is dict, "'{0}' attribute: '{1}' type is not 'dict'!".format("categories", value)
		self.__categories = value

	@categories.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def categories(self):
		"""
		This method is the deleter method for the __categories attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("categories"))

	@property
	def components(self):
		"""
		This method is the property for the __components attribute.

		:return: self.__components. ( Dictionary )
		"""

		return self.__components

	@components.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def components(self, value):
		"""
		This method is the setter method for the __components attribute.

		:param value: Attribute value. ( Object )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("components"))

	@components.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def components(self):
		"""
		This method is the deleter method for the __components attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("components"))

	#***********************************************************************************************
	#***	Class methods.
	#***********************************************************************************************
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.FileStructureError)
	def getProfile(self, file):
		"""
		This method gets provided Component Profile.

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
				raise foundations.exceptions.FileStructureError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Name"))
			profile.path = os.path.dirname(file)
			profile.module = parser.attributeExists("Module", "Component") and parser.getValue("Module", "Component") or None
			if not profile.module:
				raise foundations.exceptions.FileStructureError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Module"))
			profile.object_ = parser.attributeExists("Object", "Component") and parser.getValue("Object", "Component") or None
			if not profile.object_:
				raise foundations.exceptions.FileStructureError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Object"))
			profile.rank = parser.attributeExists("Rank", "Component") and parser.getValue("Rank", "Component") or None
			if not profile.rank:
				raise foundations.exceptions.FileStructureError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Rank"))
			profile.version = parser.attributeExists("Version", "Component") and parser.getValue("Version", "Component") or None
			if not profile.version:
				raise foundations.exceptions.FileStructureError("'{0}' no '{1}' attribute found, file structure seems invalid!".format(file, "Version"))
			profile.author = parser.attributeExists("Author", "Informations") and parser.getValue("Author", "Informations") or None
			profile.email = parser.attributeExists("Email", "Informations") and parser.getValue("Email", "Informations") or None
			profile.url = parser.attributeExists("Url", "Informations") and parser.getValue("Url", "Informations") or None
			profile.description = parser.attributeExists("Description", "Informations") and parser.getValue("Description", "Informations") or None

			return profile
		else:
			raise foundations.exceptions.FileStructureError("'{0}' no sections found, file structure seems invalid!".format(file))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def gatherComponents(self):
		"""
		This method gather the Components.
		"""

		if self.paths:
			self.__components = {}
			walker = Walker()
			for path in self.paths.keys():
				walker.root = self.paths[path]
				walker.walk(("\.{0}$".format(self.__extension),), ("\._",))
				for component in walker.files.keys():
					LOGGER.debug("> Current Component: '{0}'.".format(component))
					profile = self.getProfile(walker.files[component])
					if profile:
						if os.path.isfile(os.path.join(profile.path, profile.module) + ".py"):
							self.__components[profile.name] = profile
						else:
							LOGGER.warning("!> {0} | '{1}' has no associated Module and has been rejected!".format(self.__class__.__name__, component))
							continue
					else:
						LOGGER.warning("!> {0} | '{1}' is not a valid Component and has been rejected!".format(self.__class__.__name__, component))
		else:
			raise foundations.exceptions.ProgrammingError("'{0}' has no Components paths defined!".format(self))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError, ImportError)
	def instantiateComponents(self, callback=None):
		"""
		This method instantiates the Components.

		:param callback: Callback object. ( Object )
		"""

		assert self.__components, "'{0}' Manager has no Components!".format(self)

		for component in self.getComponents():
			profile = self.__components[component]
			callback and callback(profile)

			LOGGER.debug("> Current Component: '{0}'.".format(component))

			sys.path.append(profile.path)
			profile.import_ = __import__(profile.module)
			object_ = profile.object_ in profile.import_.__dict__ and getattr(profile.import_, profile.object_) or None
			if object_ and inspect.isclass(object_):
				for categorie, type in self.__categories.items():
					profile.categorie = categorie
					profile.interface = issubclass(object_, type) and object_ is not type and object_(name=profile.name) or None
					if profile.interface:
						LOGGER.info("{0} | '{1}' Component has been instantiated!".format(self.__class__.__name__, profile.name))
						break
			else:
				LOGGER.error("{0} | '{1}' Component has no Interface and has been rejected!".format(self.__class__.__name__, profile.name))
				del(self.__components[component])

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def deleteComponent(self, component):
		"""
		This method removes the Provided Component.

		:param component: Component to remove. ( List )
		:return: Deletion success. ( Boolean )
		"""

		del(self.__components[component])
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def clearComponents(self):
		"""
		This method clears the Components.

		:return: Clearing success. ( Boolean )
		"""

		self.__components.clear()
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, ImportError)
	def reloadComponent(self, component):
		"""
		This method reload the Provided Component.

		:param callback: Callback object. ( Object )
		:return: Reload success. ( Boolean )
		"""

		profile = self.__components[component]
		import_ = __import__(profile.module)
		reload(import_)
		object_ = profile.object_ in dir(import_) and getattr(import_, profile.object_) or None
		if object_ and inspect.isclass(object_):
			interface = issubclass(object_, self.__categories[profile.categorie]) and object_ is not self.__categories[profile.categorie] and object_(name=profile.name) or None
			if interface:
				LOGGER.info("{0} | '{1}' Component has been reloaded!".format(self.__class__.__name__, profile.name))
				profile.import_ = import_
				profile.interface = interface

				return True

	@core.executionTrace
	def getComponents(self):
		"""
		This method gets the Components by ranking.
		"""

		return [component[0] for component in sorted(((component, profile.rank) for component, profile in self.__components.items()), key=lambda x:(int(x[1])))]

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def filterComponents(self, pattern, categorie=None):
		"""
		This method filters the Components using the provided pattern.

		:param pattern: Regex filtering pattern. ( String )
		:param categorie: Categorie filter. ( String )
		:return: Matching items. ( List )
		"""

		assert self.__components is not None, "'{0}' Manager has no Components!".format(self)
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
		This method gets the Component interface.

		:param component: Component to get the interface.
		:return: Component interface. ( Object )
		"""

		components = self.filterComponents("^" + component + "$")
		if components != []:
			return self.__components[components[0]].interface

