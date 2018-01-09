from weathertrip import util
import unittest


class UtilTest(unittest.TestCase):
    def test_get_key(self):
        value = util.get_key("test_file.txt")
        self.assertEqual('This_is_a_key', value)

    def test_get_key_negative(self):
        self.assertFalse(util.get_key("does_not_exist.file"))

    def test_get_coordinates(self):
        good_dict =[{'overview_polyline': {'points': '_c`|@_y|u@?~hbE'}}]
        coordinate_set = util.get_coordinates_from_encoded_polyline(good_dict)
        self.assertEqual([{'lat': 10.0, 'lng': 9.0}, {'lat': 10.0, 'lng': 8.0}], coordinate_set)

    def test_get_coordinates_no_polyline(self):
        bad_dict = [{'apple':'test'}]
        self.assertFalse(util.get_coordinates_from_encoded_polyline(bad_dict))

    def test_get_distances(self):
        value = util.get_distances([{'lat': 95.6, 'lng': -26.5}, {'lat': 95.6, 'lng': -26.408245}])
        self.assertEqual('1.0', str(round(value, 1)))

    def test_get_distances_negative(self):
        self.assertFalse(util.get_distances([0]))


if __name__ == '__main__':
    unittest.main()