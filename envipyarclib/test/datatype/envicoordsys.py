"""
"""

import unittest
import os
import arcpy


class TestDataTypeENVICoordSys(unittest.TestCase):
    """Tests the ENVICOORDSYS task datatype"""
    config = None

    @classmethod
    def setUpClass(cls):
        """Class setup creates a toolbox file wrapper"""
        cls.config.setup_toolbox('ENVI', 'qa_envitaskengine_datatype_envicoordsys', 'test_datatype_envicoordsys')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_datatype_envicoordsys_css(self):
        """Tests the envicoordsys datatype with a valid code"""
        css = 'PROJCS["WGS_1984_UTM_Zone_13N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-105.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'
        result = arcpy.qa_envitaskengine_datatype_envicoordsys_TEST(css)
        # even though envi returns the EPSG code, it's converted back to css just fine
        self.assertEqual(result[0].replace("'", '"'), css)