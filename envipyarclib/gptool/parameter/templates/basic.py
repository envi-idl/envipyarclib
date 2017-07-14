"""
Maps a simple task parameter to a GP Tool parameter.  Meant to be used as a base class.
"""
from __future__ import absolute_import
from string import Template

from ..template import Template as ParamTemplate


class BASIC(ParamTemplate):
    """
    Maps a simple task parameter to a GP Tool parameter.  Meant to be used as a base class.
    """
    def get_parameter(self, task_param):
        return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="$dataType",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')

    def parameter_names(self, task_param):
        return [Template('${name}')]

    def default_value(self):
        return Template('''
        ${name}.value = $defaultValue
''')

    def pre_execute(self):
        return Template('''
        input_params['${name}'] = parameters[self.i${name}].value
''')

    def post_execute(self):
        return Template('''
        parameters[self.i${name}].value = task_results['${name}']
''')


def template():
    """Factory method for this parameter template class"""
    return BASIC('GPType')
