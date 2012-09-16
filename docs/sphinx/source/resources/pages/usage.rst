_`Usage`
========

Please refer to `Manager - Api <http://thomasmansencal.com/Sharing/Manager/Support/Documentation/Api/index.html>`_ for precise usage examples.

A Component package contains at least a resource **.rc** description file and a main module::

	testsComponentA
	├── __init__.py
	├── testsComponentA.py
	└── testsComponentA.rc

The description file is a configuration style file with a structure similar to what you would find in Microsoft Windows INI files::

	[Component]
	Name = core.testsComponentA
	Title = Tests Component A
	Module = testsComponentA
	Object = TestsComponentA
	Rank = 10
	Version = 1.0

	[Informations]
	Author = Thomas Mansencal
	Email = thomas.mansencal@gmail.com
	Url = http://www.hdrlabs.com/
	Description = Core tests Component A.

Given the following directories structure::

	core
	├── __init__.py
	├── testsComponentA
	│   ├── __init__.py
	│   ├── testsComponentA.py
	│   └── testsComponentA.rc
	└── testsComponentB
		├── __init__.py
		├── testsComponentB.py
		└── testsComponentB.rc

Instantiating the Components Manager is done the following way:

.. code:: python

	>>> manager = Manager(("./manager/tests/testsManager/../components/core",))
	>>> manager.registerComponents()
	True
	>>> manager.listComponents()
	['core.testsComponentA', 'core.testsComponentB']
	>>> manager.instantiateComponents()
	True
	>>> manager.getInterface("core.testsComponentA")
	<testsComponentA.TestsComponentA object at 0x11dd990>

**manager.componentsManager.Manager.getInterface(name)** method returns the interface of given Component, in the previous example it's the object declared in the description file by this statement: **Object = TestsComponentA**.

Three base Components are provided by default:

-  **manager.component.Component**
-  **manager.qobjectComponent.QObjectComponent**
-  **manager.qwidgetComponent.QWidgetComponent**

When inheriting from those Components, one have to reimplement the following methods for all the Components types:

-  **activate**
-  **deactivate**

**activated** attribute has to be set accordingly in the methods implementation.

When implementing a **manager.qwidgetComponent.Component** or **manager.qobjectComponent.QObjectComponent**, the following methods are also needed:

-  **initialize**
-  **uninitialize**

**initialized** attribute has to be set accordingly in the methods implementation.

Or alternatively, those methods when implementing a **manager.qwidgetComponent.QWidgetComponent**:

-  **initializeUi**
-  **uninitializeUi**

**initializedUi** attribute has to be set accordingly in the methods implementation.

Reference Component implementation example class:

.. code:: python

	class TestsComponentA(Component):

		def __init__(self, name=None):
			Component.__init__(self, name=name)
			
			self.deactivatable = True

		def activate(self):
			print("> Activating '{0}' Component.".format(self.__class__.__name__))

			self.activated = True
			return True

		def deactivate(self):
			print("> Deactivating '{0}' Component.".format(self.__class__.__name__))

			self.activated = False
			return True

		def initialize(self):
			print("> Initializing '{0}' Component.".format(self.__class__.__name__))

			self.initialized = True
			return True

		def uninitialize(self):
			print("> Uninitializing '{0}' Component.".format(self.__class__.__name__))

			self.initialized = False
			return True

.. raw:: html

    <br/>

