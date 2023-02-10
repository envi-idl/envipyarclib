"""
"""

import unittest
import os
import arcpy
import filecmp
import tempfile


class TestDataTypeENVIRasterSeriesArray(unittest.TestCase):
    """Tests the ENVIRASTERSERIESARRAY task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_envirasterseriesarray',
                                 'test_datatype_envirasterseriesarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_envirasterseriesarray_file(self):
        """Tests the envirasterseriesarray datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'checkerboard.series')

        result = arcpy.qa_envitaskengine_datatype_envirasterseriesarray_TEST([input, input], 2)

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output ENVIRasterSeries URI not set')
        path = result.getOutput(0)

        output_filename = os.path.splitext(os.path.basename(path))[0]
        output_dir = os.path.dirname(path)

        input_dir = os.path.dirname(input)
        input_filename = os.path.splitext(os.path.basename(input))[0]

        # Verify file(s)
        output_file = os.path.join(output_dir, output_filename + '.series')
        input_file = os.path.join(input_dir, input_filename + '.series')

        self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)
        self.assertTrue(filecmp.cmp(output_file, input_file), 'Output does not match expected: ' + output_file)