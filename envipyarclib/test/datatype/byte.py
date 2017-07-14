"""
"""
import os
import unittest
import arcpy


class TestDataTypeByte(unittest.TestCase):
    """Tests the byte task datatype"""

    config = None
    
    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL','qa_idltaskengine_datatype_byte', 
                                 'test_datatype_byte')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_byte_min(self):
        """Tests the byte datatype minimum value."""
        input = 0
        result = arcpy.QA_IDLTaskEngine_DataType_Byte_TEST(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_byte_max(self):
        """Tests the byte datatype maximum value."""
        input = 255
        result = arcpy.QA_IDLTaskEngine_DataType_Byte_TEST(input)

        self.assertEqual(int(result.getOutput(0)), input)

    def test_datatype_byte_outofrange(self):
        """Tests error message when value is out of datatype range."""
        input = 256

        try:
            result = arcpy.QA_IDLTaskEngine_DataType_Byte_TEST(input)
            self.fail('Exception not thrown.')
        except arcpy.ExecuteError:
            isError = str(arcpy.GetMessages(2))
            expError = 'Task failed to execute'

            self.assertIn(expError, isError)