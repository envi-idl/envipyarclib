"""
"""

import unittest
import arcpy

class TestDatatypeLong(unittest.TestCase):
    """Tests the long task datatype"""

    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_long',
                                 'test_datatype_long')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_long_max(self):
        """Tests the long datatype maximum value."""
        input = 2147483647
        result = arcpy.QA_IDLTaskEngine_DataType_Long_TEST(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_long_min(self):
        """Tests the long datatype minimum value."""
        input = -2147483648
        result = arcpy.QA_IDLTaskEngine_DataType_Long_TEST(input)

        self.assertEqual(int(result.getOutput(0)), int(input))