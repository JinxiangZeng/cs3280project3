#!/usr/bin/env python3

"""
THis class used to implement the scan function and
display the port status after scan.
"""
from multiprocessing import Process, Pipe
import sys
import utils

__author__ = "Jinxiang Zeng"
__versiton__ = "Fall cs3280"

def get_port_status(conn):
    """
    This method used to use arguments to implement scan
    funciton and send the dictionary to relative partner.
    """
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Please check your ip address, start_port or' \
             'end_port is inputted correcttly or not')
        sys.exit()
    ip_address = sys.argv[1]
    start_port = sys.argv[2]
    end_port = ''
    if len(sys.argv) == 3:
        end_port = sys.argv[2]
    else:
        end_port = sys.argv[3]
    conn.send(utils.scan(ip_address, start_port, end_port))
    conn.close()

def main():
    """
    The main funciton to recvive the specific dictionary
    and display the information to user.
    """
    try:
        parent_conn, child_conn = Pipe()
        scan_process = Process(target=get_port_status, args=(child_conn,))
        scan_process.start()
        result = parent_conn.recv()
        for key, value in result.items():
            print("Port ", key, " : ", value)
        scan_process.join()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Exitting Program !!!!")
        sys.exit()

if __name__ == '__main__':
    main()
