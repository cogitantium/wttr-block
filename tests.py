import json
import unittest

import wttr


class GettingWeather(unittest.TestCase):
    def test_success(self):
        response = wttr.get_weather_data("https://www.wttr.in?format=j1")
        data = dict(json.loads(response))
        self.assertTrue(type(data) == dict)

    def test_fail(self):
        response = wttr.get_weather_data("http://www.wack.dk")
        self.assertEqual(response, "Error getting weather")


if __name__ == '__main__':
    unittest.main()
