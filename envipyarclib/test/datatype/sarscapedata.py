"""
"""

import unittest
import os
import arcpy


class TestDataTypeSARSCAPEDATA(unittest.TestCase):
    """Tests the SARSCAPEDATA task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_sarscapedata',
                                 'test_datatype_sarscapedata')

    @classmethod
    def tearDownClass(cls):
        pass

    def DISABLEDtest_datatype_sarscapedata_uri(self):
        pass
        """Tests the sarscapedata datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'checkerboard.dat')
        result = arcpy.qa_envitaskengine_datatype_sarscapedata_TEST(input)
        self.assertEqual(input, result[0])

    def DISABLEDtest_datatype_sarscapedata_string(self):
        """Tests the sarscapedata datatype with file uri."""
        input = 'foo'
        result = arcpy.qa_envitaskengine_datatype_sarscapedata_TEST(input)
        self.assertEqual(input, result[0])
