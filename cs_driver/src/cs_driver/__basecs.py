import rospy
import cmd
from logging import NullHandler
from pickle import TRUE
from turtle import goto
import socket
import json
import time
import copy
import os

class BaseCS():
    def connectETController(self, ip, port=30001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, port))
            return (True, sock)
        except Exception as e:
            sock.close()
            return (False,)

    def disconnectETController(self, sock):
        if (sock):
            sock.close()
            sock = None
        else:
            sock = None

    def sendCMD(self, sock, cmd, params=None, id=1):
        try:
            sock.sendall(cmd.encode("utf8"))

        except Exception as e:
            return (False, None, None)