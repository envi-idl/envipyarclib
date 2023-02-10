"""
Defines the parameter template for the specified data type.
"""
from __future__ import absolute_import
from string import Template
from ..template import Template as ParamTemplate



class ENVIURIARRAY(ParamTemplate):
    """
    Defines the parameter template for the specified data type.
    """
    def get_parameter(self, task_param):
        # Input uses a composite data type of both defile and gpstring.
        # This allows for url strings while also providing file selection in the UI.
        if task_param['direction'].upper() == 'INPUT':
            if task_param['is_directory']:
                return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype=["DEFolder", "GPString"],
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')
            else:
                return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype=["DEFile","GPString"],
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
''')
        # Return the output template
        else:
            return Template('''
        $name = arcpy.Parameter(
            displayName="$displayName",
            name="$name",
            datatype="GPString",
            parameterType="$paramType",
            direction="$direction",
            multiValue=$multiValue
        )
    ''')

    def parameter_names(self, task_param):
        return [Template('${name}')]

    def default_value(self):
        return Template('''
        ${name}.values = "$defaultValue"
''')

    def pre_execute(self):
        return Template('''
        # valuesAsText will put quotes around values with spaces in them
        # this is erronious in ENVI, and thus we need to follow this pattern.

        paths = parameters[self.i${name}].values
        uris = []
        for uri in paths:
            try:
                uris.append(uri.value)
            except AttributeError as error:
                uris.append(uri)
        input_params['${name}'] = uris
''')

    def post_execute(self):
        return Template('''
        if '${name}' in task_results:
            parameters[self.i${name}].values = task_results['${name}']
''')

def template():
    """Factory method for this parameter template class"""
    return ENVIURIARRAY('DEFile')
