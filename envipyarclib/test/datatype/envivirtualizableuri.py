"""
"""

import unittest
import os
import arcpy


class TestDataTypeENVIVirtualizableURI(unittest.TestCase):
    """Tests the ENVIVIRTUALIZABLEURI task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_envivirtualizableuri',
                                 'test_datatype_envivirtualizableuri')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_envivirtualizableuri_file_uri(self):
        """Tests the envivirtualizableuri datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'qb_boulder_msi.dat')
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIVIRTUALIZABLEURI_TEST(input)
        self.assertEqual(result[0], input)

    def test_datatype_envivirtualizableuri_url(self):
        """Tests the envivirtualizableuri datatype with http url."""
        input = 'http://localhost/ese/data/qb_boulder_msi.dat'
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIVIRTUALIZABLEURI_TEST(input)
        self.assertEqual(result[0], input)

    def test_datatype_envivirtualizableuri_string(self):
        """Tests the envivirtualizableuri datatype with arbitrary string."""
        inputENVIVIRTUALIZABLEURI = 'foo'
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIVIRTUALIZABLEURI_TEST(inputENVIVIRTUALIZABLEURI)
        self.assertEqual(result[0], inputENVIVIRTUALIZABLEURI)