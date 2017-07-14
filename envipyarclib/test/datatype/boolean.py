"""
"""
import unittest

import arcpy


class TestDataTypeBoolean(unittest.TestCase):
    """Tests the server GPToolbox class"""
    config = None
    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'QA_IDLTaskEngine_DataType_Boolean', 
                                 'test_datatype_boolean')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_boolean_true(self):
        """Tests the bool datatype with a value of true."""
        inputBool = True
        result = arcpy.QA_IDLTaskEngine_DataType_Boolean_TEST(inputBool)
        self.assertEqual(result.getOutput(0), 'true')

    def test_datatype_boolean_default(self):
        """Tests the bool datatype with a default value."""
        result = arcpy.QA_IDLTaskEngine_DataType_Boolean_TEST()
        self.assertEqual(result.getOutput(0), 'false')

    def test_datatype_boolean_false(self):
        """Tests the bool datatype with a value of false."""
        inputBool = False
        result = arcpy.QA_IDLTaskEngine_DataType_Boolean_TEST(inputBool)
        self.assertEqual(result.getOutput(0), 'false')