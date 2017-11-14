"""
"""

import unittest
import os
import arcpy


class TestDataTypeENVIURI(unittest.TestCase):
    """Tests the ENVIURI task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'QA_ENVITaskEngine_DataType_ENVIURI',
                                 'test_datatype_enviuri')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_enviuri_file_uri(self):
        """Tests the enviuri datatype with file uri."""
        input = os.path.join(self.config.test_data_dir, 'checkerboard.dat')
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIURI_TEST(input)
        self.assertEqual(result[0], input)

    def test_datatype_enviuri_url(self):
        """Tests the enviuri datatype with http url."""
        input = 'http://localhost/ese/data/qb_boulder_msi.dat'
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIURI_TEST(input)
        self.assertEqual(result[0], input)

    def test_datatype_enviuri_string(self):
        """Tests the enviuri datatype with arbitrary string."""
        inputENVIURI = 'foo'
        result = arcpy.QA_ENVITaskEngine_DataType_ENVIURI_TEST(inputENVIURI)
        self.assertEqual(result[0], inputENVIURI)