"""

"""

import unittest
import arcpy

class TestDataTypeULong(unittest.TestCase):
    """Tests the ulong task datatype"""

    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_ulong',
                                 'test_datatype_ulong')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_ulong_max(self):
        """Tests the ulong datatype maximum value."""
        # Since we have to use gplong, we are limited to the 32 bit signed long integer range.
        input = 2147483647

        result = arcpy.QA_IDLTaskEngine_DataType_ULong_TEST(input)
        # int and long were consolidated to int only in Python 3
        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_ulong_min(self):
        """Tests the ulong datatype minimum value."""
        input = 0
        result = arcpy.QA_IDLTaskEngine_DataType_ULong_TEST(input)
        print(result.getOutput(0))
        # int and long were consolidated to int only in Python 3
        self.assertEqual(int(result.getOutput(0)), int(input))