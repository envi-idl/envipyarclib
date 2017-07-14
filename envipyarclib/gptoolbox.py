"""
GPToolbox is used as a base class to create GPTool wrappers for \
ENVI, IDL, and GSF Analytics.
"""

import os.path
from string import Template
import pkgutil

import envipyarclib.gptool.parameter.builder as param_builder
from envipyarclib.gptool.parameter.builder import ParameterMap
import envipyarclib.gptool.help as help_builder


class GPToolbox(object):
    """
    GPToolbox is used as a base class to create GPTool wrappers for \
ENVI, IDL, and GSF Analytics.

    :param tasks: a list of tasks to map to GPTools where each task name is a \
    GPTool in the toolbox.
    :param alias: The alias of the generated toolbox
    :param imports_template: The template string code for defining imports
    :param execute_template: The template string code for GPTool execution
    :param parameter_templates: The python package containing parameter templates.  \
    Templates must implement the envipyarclib.gptool.parameter.Template class.
    """

    _toolbox_class_template = Template('''
class Toolbox(object):
    def __init__(self):
        self.label = "$label"
        self.alias = "$alias"

        # List of tool classes associated with this toolbox
        self.tools = $toolList
''')

    _tool_template = Template('''
class $taskName(object):
    def __init__(self):
        self.label = "$taskDisplayName"
        self.description = "$taskDescription"
        self.canRunInBackground = $canRunInBackground

    def getParameterInfo(self):

        $parameterInfo

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        $updateParameter
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        $preExecute
        $execute
        $postExecute
        return

''')

    def __init__(self,
                 tasks=None,
                 alias=None,
                 imports_template=Template(''),
                 execute_template=Template(''),
                 parameter_templates=None):
        self.tasks = tasks
        self.toolbox_file = None
        self.parameter_map = ParameterMap()
        self.alias = alias
        self._imports_template = imports_template
        self._execute_template = execute_template

        if parameter_templates:
            for importer, modname, is_pkg in pkgutil.iter_modules(parameter_templates.__path__):
                self.parameter_map.register_template('.'.join((parameter_templates.__name__,
                                                               modname)))

    def create_toolbox(self, filename):
        """
        Creates a new Python toolbox where each task name is a GPTool in the toolbox.

        :param filename: the filename of the generated toolbox
        :param service_name: The name of the ESE service containing the tasks.  Only tasks from
                             one service may be used.
        :param tasks: The list of tasks from the service to build as GPTools.
        """
        filename = os.path.splitext(filename)[0]
        label = os.path.basename(filename)

        # Get task information first so we can build the tool list
        tool_list = []
        for task in self.tasks:
            tool_list.append(task.name)

        file_descriptor = os.open(filename + '.pyt',
                                  os.O_WRONLY | os.O_CREAT | os.O_EXCL)
        with os.fdopen(file_descriptor, 'w') as self.toolbox_file:
            self.toolbox_file.write(self._imports_template.substitute({}))
            toolbox_class = self._toolbox_class_template.substitute(
                {'label': label,
                 'alias': self.alias,
                 'toolList': param_builder.convert_list(tool_list)
                }
            )
            self.toolbox_file.write(toolbox_class)

            for task in self.tasks:
                gp_tool = self.create_tool(task)
                self.toolbox_file.write(gp_tool)
                toolbox_help_filename = '.'.join((filename, task.name, 'pyt', 'xml'))
                help_builder.create(toolbox_help_filename, task, self.alias)

        return filename

    def create_tool(self, task):
        """
        Creates a new GPTool for the toolbox.


        """
        gp_tool = dict(taskName=task.name,
                       taskDisplayName=task.display_name,
                       taskDescription=task.description,
                       canRunInBackground=True,
                       taskUri=task.uri)

        gp_tool['execute'] = self._execute_template.substitute(gp_tool)
        gp_tool['parameterInfo'] = param_builder.create_param_info(task.parameters,
                                                                   self.parameter_map)
        gp_tool['updateParameter'] = param_builder.create_update_parameter(task.parameters,
                                                                           self.parameter_map)
        gp_tool['preExecute'] = param_builder.create_pre_execute(task.parameters,
                                                                 self.parameter_map)
        gp_tool['postExecute'] = param_builder.create_post_execute(task.parameters,
                                                                   self.parameter_map)
        return self._tool_template.substitute(gp_tool)

    def import_script(self, script_name):
        """Finds the script file and copies it into the toolbox"""
        filename = os.path.abspath(script_name)
        with open(filename, 'r') as script_file:
            self.toolbox_file.write(script_file.read())
