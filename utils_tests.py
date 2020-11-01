#!/usr/bin/env python3

"""
Create test test class to test scan port if crrectly.
"""

__author__ = "Jinxiang Zeng"
__version__ = "Fall cs3280"

import unittest
import socket
import utils

class TestUtilsMethods(unittest.TestCase):

    """
    This class used to test methods in scanner
    """
    def test_one_port_open(self):

        """Test start port is 50000 and the port is open"""
        dictionary = {}
        listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen.bind(('127.0.0.1', 50000))
        listen.listen(1)
        socket.setdefaulttimeout(1)
        result = listen.connect_ex(('127.0.0.1', 50000))
        if result == 0:
            key = 50000
            value = True
            dictionary[key] = value
        else:
            key = 50000
            value = False
            dictionary[key] = value
        listen.close()
        self.assertEqual(dictionary, utils.scan('127.0.0.1', 50000, 50000))

    def test_one_port_close(self):

        """Test start port is 50000 and the port is close"""
        dictionary = {}
        listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = listen.connect_ex(('127.0.0.1', 50000))
        if result == 0:
            key = 50000
            value = True
            dictionary[key] = value
        else:
            key = 50000
            value = False
            dictionary[key] = value
        listen.close()
        self.assertEqual(dictionary, utils.scan('127.0.0.1', 50000, 50000))

    def test_all_port_open(self):

        """Test start port is 50010 and end port is 50013, and all ports open"""
        dictionary = {}
        for port in range(50000, 50013 + 1):
            listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listen.bind(('127.0.0.1', 50010))
            listen.listen(1)
            socket.setdefaulttimeout(1)
            result = listen.connect_ex(('127.0.0.1', port))
            if result == 0:
                key = port
                value = True
                dictionary[key] = value
            else:
                key = port
                value = False
                dictionary[key] = value
            listen.close()
        self.assertEqual(dictionary, utils.scan('127.0.0.1', 50000, 50013))

    def test_all_port_close(self):

        """Test start port is 50010 and end port is 50020, and all ports close"""
        dictionary = {}
        for port in range(50000, 50020 + 1):
            listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = listen.connect_ex(('127.0.0.1', port))
            if result == 0:
                key = port
                value = True
                dictionary[key] = value
            else:
                key = port
                value = False
                dictionary[key] = value
            listen.close()
        self.assertEqual(dictionary, utils.scan('127.0.0.1', 50000, 50020))

    def test_port_open_and_close(self):

        """Test start port is 50000 and end port is 50020"""
        dictionary = {}
        for port in range(50000, 50020 + 1):
            listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listen.bind(('127.0.0.1', 50018))
            listen.listen(1)
            socket.setdefaulttimeout(1)
            result = listen.connect_ex(('127.0.0.1', port))
            if result == 0:
                key = port
                value = True
                dictionary[key] = value
            else:
                key = port
                value = False
                dictionary[key] = value
            listen.close()
        self.assertEqual(dictionary, utils.scan('127.0.0.1', 50000, 50020))


if __name__ == '__main__':
    unittest.main()
