"""

"""

import unittest
import arcpy

class TestDatatypeString(unittest.TestCase):
    """Tests the string datatype."""

    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_string',
                                 'test_datatype_string')
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_string',
                                 'test_datatype_string_choicelist')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_string_basic(self):
        """Tests the string datatype with a basic string."""
        inputString = 'th1sIsaTESTString!'
        result = arcpy.QA_IDLTaskEngine_DataType_String_TEST(inputString)

        self.assertEqual(result.getOutput(0), inputString)

    def test_datatype_string_default(self):
        """Tests the string datatype with a default value."""
        result = arcpy.QA_IDLTaskEngine_DataType_String_TEST()

        self.assertEqual(result.getOutput(0), "cat")

    def test_datatype_string_choicelist(self):
        """Tests the string datatype with a choicelist."""
        input = "fish"
        result = arcpy.QA_ENVITaskEngine_DataType_String_TEST(input)

        self.assertEqual(result.getOutput(0), input)