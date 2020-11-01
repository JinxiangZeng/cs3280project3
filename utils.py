"""
Create scanner class to scan ports if is opened or closed
"""
import socket

__author__ = "Jinxiang Zeng"
__versiton__ = "Fall cs3280"

def scan(ip_address, start_port, end_port):
    """
    This method used to check the ports betweent start port and
    end port on give ip address, and return a dictionay of status
    that represent each post.
    """
    port_dictionary = {}
    int_start_port = int(start_port)
    int_end_port = int(end_port)
    for port in range(int_start_port, int_end_port + 1):
        listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = listen.connect_ex((ip_address, port))
        if result == 0:
            key = port
            value = True
            port_dictionary[key] = value
        else:
            key = port
            value = False
            port_dictionary[key] = value
        listen.close()
    return port_dictionary
