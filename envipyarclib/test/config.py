"""

"""
import os
import difflib
import glob
from abc import ABCMeta, abstractmethod
import arcpy
from ..metaclass import with_metaclass

class Config(with_metaclass(ABCMeta, object)):
    """
    Defines the configuration for running the datatype tests.
    """

    @property
    def test_data_dir(self):
        """
        Returns the full path to the test data directory
        """
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

    @property
    def test_task_dir(self):
        """
        Returns the full paath to the test task directory
        """
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks')

    @abstractmethod
    def setup_toolbox(self, engine_name, task_name, toolbox_name):
        """
        Abstract method for generating python toolboxes from test tasks.
        :param engine_name:  The name of the engine the test case runs against
        :param task_name:  The name of the task the test case runs against
        :param toolbox_name: The name of the toolbox to be generated.
        """
        pass

    def remove_toolbox(self, toolbox_file):
        """
        Removes the toolbox file from disk
        """
        toolbox_file = os.path.splitext(toolbox_file)[0]
        for tb_file in glob.glob(toolbox_file + '.*'):
            os.remove(tb_file)

    def compare_text_files(self, file1, file2):
        """
        Compares two text files.
        Removes whitespace, empty lines, and newline chars
        Empty string as a return value mean file are the same
        Open, read lines to string list, remove any newline chars, and
        filter out empty strings/lines.

        """
        text1 = list(filter(None, map(str.rstrip, open(file1, 'U').readlines())))
        text2 = list(filter(None, map(str.rstrip, open(file2, 'U').readlines())))

        return ''.join(difflib.unified_diff(text1, text2))

    def setup_workspace(self, workspace_dir):
        """
        Override the default arcpy workspace and scratch workspace

        """
        if not os.path.isdir(workspace_dir):
            os.mkdir(workspace_dir)
        arcpy.env.workspace = workspace_dir

        scratch_workspace = os.path.join(workspace_dir, 'scratch')
        if not os.path.isdir(scratch_workspace):
            os.mkdir(scratch_workspace)
        arcpy.env.scratchWorkspace = scratch_workspace

