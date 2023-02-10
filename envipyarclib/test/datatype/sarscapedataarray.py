"""
"""

import unittest
import os
import arcpy


class TestDataTypeSARSCAPEDATAArray(unittest.TestCase):
    """Tests the SARSCAPEDATAArray task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_sarscapedataarray',
                                 'test_datatype_sarscapedataarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def DISABLEDtest_datatype_sarscapedataarray_uri(self):
        """Tests the sarscapedataarray datatype with file uri."""
        input = [ os.path.join(self.config.test_data_dir, 'checkerboard_1roi.xml'),
                  os.path.join(self.config.test_data_dir, 'checkerboard.hdr'),
                  os.path.join(self.config.test_data_dir, 'checkerboard.dat') ]

        result = arcpy.qa_envitaskengine_datatype_sarscapedataarray_TEST(input)
        self.assertEqual(';'.join(input).lower(), result[0].lower())

    def DISABLEDtest_datatype_sarscapedataarray_string(self):
        """Tests the sarscapedataarray datatype with file uri."""
        input = [ 'foo.bar', 'tea.leaves', 'sar' ]

        result = arcpy.qa_envitaskengine_datatype_sarscapedataarray_TEST(input)
        self.assertEqual(input, result[0].split(';'))
