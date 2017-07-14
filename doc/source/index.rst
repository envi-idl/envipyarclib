.. _envipyarclib:

**************************
ENVI Py for ArcGIS Library
**************************

.. include:: <isonum.txt>

ENVI Py for ArcGIS Library provides tools for generating ArcGIS python toolboxes.

See http://www.harrisgeospatial.com/ for more details on product offerings.

Usage
=====

Create GPToolbox
----------------

To generate an empty toolbox from python, use the GPToolbox class and initialize with an empty list of task objects::

    from envipyarclib import GPToolbox
    toolbox = GPToolbox([], 'DEMO')
    toolbox.create_toolbox('C:\\TEMP\\demo.pyt')

To create a toolbox with empty GPTools you must first create a Task class defining the properties the GPToolbox supports::

    class Task(object):

        def __init__(self, name, display_name, description):
            self.name = name
            self.display_name = display_name
            self.description = description
            self.uri = name

        @property
        def parameters(self):
            return dict()
        
Once the Task class is defined you can pass in task objects to the GPToolbox and generate empty GPtools::

    toolbox = GPToolbox([Task('firstTask', 'First Task', 'Does nothing'),
                         Task('secondTask', 'Second Task', 'Still Does nothing')],
                         'DEMO')
    toolbox.create_toolbox('C:\\TEMP\\demo.pyt')

To import python modules or any global functionality to the toolbox, you can use the imports_template keyword when initializing the GPToolbox.  The template string must be formatted with zero indentation.  For example to inlcude arcpy and os::

    from string import Template
    from envipyarclib import GPToolbox

    imports_template = Template('''
    import os
    import arcpy
    ''')

    toolbox = GPToolbox([Task('firstTask', 'First Task', 'Does nothing')], 'DEMO',
                        imports_template=imports_template)
    toolbox.create_toolbox('C:\\TEMP\\demo.pyt')

To add code to the execute method of all GPTools, you can use the execute_template keyword when initializing the GPToolbox. The template string must be formatted with 2 indentations.  From our previous exmample, to add the system path to the messages when running the GPTool::

    from string import Template
    from envipyarclib import GPToolbox

    imports_template = Template('''
    import os
    import arcpy
    ''')

    execute_template = Template('''
            messages.AddMessage('System Path: ' + str(os.sys.path))
    ''')

    toolbox = GPToolbox([Task('firstTask', 'First Task', 'Does nothing')], 'DEMO',
                        imports_template=imports_template,
                        execute_template=execute_template)
    toolbox.create_toolbox('C:\\TEMP\\demo.pyt')


Test GPToolbox Data Types
-------------------------

This library provides test cases and test tasks for testing ENVI and IDL data types available in the envipyarclib.test package.  To test a data type, you must implement the test config abstract base class for generating a toolbox and importing it into arcpy before running a test::

    import arcpy
    from envipyarclib.test.config import Config

    class MyConfig(Config):

        def __init__
        def setup_toolbox(self, engine_name, task_name, toolbox_name):
            # Create python toolbox here
            arcpy.ImportToolbox(toolbox_file)

Once the Config class is created you can import a data type test in your module for testing.  Once imported, the unittest module will be able to find and run the test cases::

    from envipyarclib.test.datatype.bool import TestDataTypeBool

    config = MyConfig()

    # Attach the config to the test case
    TestDataTypeBool.config = config
    
API Documentation
=================

.. toctree::
   :maxdepth: 2

   api
