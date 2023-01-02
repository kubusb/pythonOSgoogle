#!/usr/bin/env python3
from test_to_csv import write_int_speed_to_csv
import unittest
import os

class TestInternet(unittest.TestCase):
    def test_something(self):
        path = os.path.exists('./speedtest.csv')
        assert path is True

unittest.main()