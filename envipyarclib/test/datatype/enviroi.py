"""
"""

import unittest
import os
import arcpy
import filecmp
import tempfile


class TestDataTypeENVIROI(unittest.TestCase):
    """Tests the ENVIROI task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_enviroi',
                                 'test_datatype_enviroi')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_enviroi_singlefile_singleroi(self):
        """Tests the enviroi datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'checkerboard_1roi.xml')

        result = arcpy.qa_envitaskengine_datatype_enviroi_TEST(input)

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

    def test_datatype_enviroi_singlefile_multiplerois(self):
        """Tests the enviroi datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'checkerboard_3roi.xml')
        try:
            result = arcpy.qa_envitaskengine_datatype_enviroi_TEST(input)
            self.assertTrue(False, 'Test should have crashed - enviroi must be a scalar')
        except:
            pass
