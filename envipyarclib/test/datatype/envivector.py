"""
"""
import os
import filecmp
import unittest
import arcpy

class TestDataTypeENVIVector(unittest.TestCase):
    """Tests the server GPToolbox class"""

    config = None

    @classmethod
    def setUpClass(cls):
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_envivector',
                                 'test_datatype_envivector')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_envivector_basic(self):
        """Tests envivector datatype."""

        input_vector = os.path.join(self.config.test_data_dir, 'checkerboard_vectors.shp')
        result = arcpy.qa_envitaskengine_datatype_ENVIVector_TEST(input_vector)

        # Verify result exists.
        self.assertTrue(result.getOutput(0), 'Output Raster URI not set')

        output_shp = result.getOutput(0)
        output_filename = os.path.splitext(os.path.basename(output_shp))[0]
        output_dir = os.path.dirname(output_shp)
        input_dir = os.path.dirname(input_vector)
        input_filename = os.path.splitext(os.path.basename(input_vector))[0]

        # Verify files
        exp_extensions = ['.shp', '.shx', '.prj', '.shp.qtr']
        for ext in exp_extensions:

            output_file = os.path.join(output_dir, output_filename + ext)
            input_file = os.path.join(input_dir, input_filename + ext)

            # Verify file exists.
            self.assertTrue(os.path.isfile(output_file), 'Output file does not exist: ' + output_file)

            # Compare output to input.
            self.assertTrue(filecmp.cmp(output_file, input_file),
                        'Output does not match expected: ' + output_file)