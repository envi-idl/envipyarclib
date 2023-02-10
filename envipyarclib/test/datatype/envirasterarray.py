"""
"""

import unittest
import os
import arcpy
import filecmp
import tempfile


class TestDataTypeENVIRasterArray(unittest.TestCase):
    """Tests the ENVIRasterArray task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_envirasterarray',
                                 'test_datatype_envirasterarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_envirasterarray_singlefile(self):
        """Tests the envirasterarray datatype with file uri."""
        input = [ os.path.join(self.config.test_data_dir, 'checkerboard.dat') ]

        result = arcpy.qa_envitaskengine_datatype_envirasterarray_TEST(input, len(input))

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output not set')
        path = result.getOutput(0)
        input = input[0]

        output_filename = os.path.splitext(os.path.basename(path))[0]
        output_dir = os.path.dirname(path)

        input_dir = os.path.dirname(input)
        input_filename = os.path.splitext(os.path.basename(input))[0]

        # Verify file(s)
        output_file = os.path.join(output_dir, output_filename + '.dat')
        input_file = os.path.join(input_dir, input_filename + '.dat')

        self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)
        self.assertTrue(filecmp.cmp(output_file, input_file), 'Output does not match expected: ' + output_file)

    def test_datatype_envirasterarray_multifile(self):
        """Tests the envirasterarray datatype with file uri."""
        input =  [ os.path.join(self.config.test_data_dir, 'checkerboard.dat'), os.path.join(self.config.test_data_dir, 'rose.gif') ]
        postfix = [ '.dat', '.gif' ]
        result = arcpy.qa_envitaskengine_datatype_envirasterarray_TEST(input, len(input))

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output not set')
        paths = result.getOutput(0).split(';')
        self.assertTrue(len(paths) == len(input), 'Output is an unexpected size')

        for i in range(len(input)):
            output_filename = os.path.splitext(os.path.basename(paths[i]))[0]
            output_dir = os.path.dirname(paths[i])

            input_dir = os.path.dirname(input[i])
            input_filename = os.path.splitext(os.path.basename(input[i]))[0]

            # Verify file(s)
            output_file = os.path.join(output_dir, output_filename + postfix[i])
            input_file = os.path.join(input_dir, input_filename + postfix[i])

            self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)
            self.assertTrue(filecmp.cmp(output_file, input_file), 'Output does not match expected: ' + output_file)
