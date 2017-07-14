"""
"""

import unittest
import arcpy

class TestDataTypeStringArray(unittest.TestCase):
    """Tests the string array task datatype"""

    config = None

    @classmethod
    def setUpClass(cls):
        cls.config.setup_toolbox('IDL', 'qa_idltaskengine_datatype_stringarray',
                                 'test_datatype_stringarray')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_stringarray_one_dimension(self):
        """Verify a one dimensional array of strings returns a semicolon separated string list."""
        input = ['foo', 'bar', 'baz']
        expect_dims = [len(input)]
        result = arcpy.QA_IDLTaskEngine_DataType_StringArray_TEST(input, expect_dims)

        self.assertEqual(result[0], ';'.join(str(i) for i in input))