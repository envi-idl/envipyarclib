"""
"""

import unittest
import os
import arcpy
import filecmp
import tempfile


class TestDataTypeENVIROIArray(unittest.TestCase):
    """Tests the ENVIROIArray task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_enviroiarray',
                                 'test_datatype_enviroiarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_enviroiarray_singlefile_singleroi(self):
        """Tests the enviroiarray datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'checkerboard_1roi.xml')
        roisInFile = 1

        result = arcpy.qa_envitaskengine_datatype_enviroiarray_TEST(input, roisInFile)

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output ROI URI not set')
        path = result.getOutput(0)

        output_filename = os.path.splitext(os.path.basename(path))[0]
        output_dir = os.path.dirname(path)

        input_dir = os.path.dirname(input)
        input_filename = os.path.splitext(os.path.basename(input))[0]

        # Verify file(s)
        output_file = os.path.join(output_dir, output_filename + '.xml')
        input_file = os.path.join(input_dir, input_filename + '.xml')

        self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)
        self.assertTrue(filecmp.cmp(output_file, input_file), 'Output does not match expected: ' + output_file)

    def test_datatype_enviroiarray_singlefile_multiplerois(self):
        """Tests the enviroiarray datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'checkerboard_3roi.xml')
        roisInFile = 3

        result = arcpy.qa_envitaskengine_datatype_enviroiarray_TEST(input, roisInFile)

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output ROI URI not set')
        path = result.getOutput(0)

        output_filename = os.path.splitext(os.path.basename(path))[0]
        output_dir = os.path.dirname(path)

        input_dir = os.path.dirname(input)
        input_filename = os.path.splitext(os.path.basename(input))[0]

        # Verify file(s)
        output_file = os.path.join(output_dir, output_filename + '.xml')
        input_file = os.path.join(input_dir, input_filename + '.xml')

        self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)
        self.assertTrue(filecmp.cmp(output_file, input_file), 'Output does not match expected: ' + output_file)

    def test_datatype_enviroiarray_multiplefiles_multiplerois(self):
        """Tests the enviroiarray datatype with file uri."""
        input = [ os.path.join(self.config.test_data_dir, 'checkerboard_1roi.xml'), os.path.join(self.config.test_data_dir, 'checkerboard_3roi.xml') ]
        roisInFile = [ 1, 3 ]

        result = arcpy.qa_envitaskengine_datatype_enviroiarray_TEST(input, 4)

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output ROI URI not set')
        paths = result.getOutput(0).split(';')

        # verify we ge the same files out as in
        self.assertEqual(len(input), len(paths))

        index = 0
        for path in paths:
            output_filename = os.path.splitext(os.path.basename(path))[0]
            output_dir = os.path.dirname(path)

            input_dir = os.path.dirname(input[index])
            input_filename = os.path.splitext(os.path.basename(input[index]))[0]

            # Verify file(s)
            output_file = os.path.join(output_dir, output_filename + '.xml')
            input_file = os.path.join(input_dir, input_filename + '.xml')

            self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)
            self.assertTrue(filecmp.cmp(output_file, input_file), 'Output does not match expected: ' + output_file)
            index+=1
