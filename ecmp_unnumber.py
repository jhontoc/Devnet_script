
import time
import argparse
import re
import os
import sys
import syslog
import logging

from time import sleep
import datetime
import cisco
from cli import *


class scrubber():
    FLAT = 0
    PER_LINE = 1
    FIRST_MATCH = 2

    def __init__(self):
        self.success = False
        self.data = []

    def scrub(self, output, rex, mode = 0, debug = 0):
        matches = []
        if type(output) == str:
            output = [output]
        for line in output:
            line_matches = []
            for match in re.findall(rex, line):
                if debug:
                    print 'scrub_line:', line
                    print 'scrub_match:', match
                if type(match) == tuple:
                    line_matches += list(match)
                else:
                    line_matches += [match]
                if mode == self.FIRST_MATCH:
                    self.data = match
                    self.success = True
                    return 1

            if line_matches:
                if mode == scrubber.FLAT:
                    matches += line_matches
                elif mode == scrubber.PER_LINE:
                    matches += [line_matches]

        if debug:
            print 'scrub_total:', len(matches)
        self.data = matches
        self.success = bool(matches)
        return len(matches)


class qncli():

    def __init__(self, username=None, password=None, device=None):
        self.username = username
        self.password = password
        self.device = device
        self.proxies = {
            "http": None,
            "https": None,
        }


    def onboard(self, cmd):
        #
        # local run
        #
        try:
            try:
                tmp = cli(cmd).split('\n')
                return tmp
            except Exception as tmp:
                tmp = ' '.join(tmp)
                tmp = tmp.split('\n')
                return tmp
        except:
            return ['']

    def vsh(self, cmd, vdc=1):

        cmd = 'vsh -i ' + str(vdc) + " -c '" + cmd + "'"
        tmp = os.popen(cmd).read().split('\n')
        return tmp


def debug(msg):

    if DEBUG:
        print("--- DEBUG:")
        print(str(msg))
        print("---")


def oprint(msg):
    if VERBOSE:
        qcli.onboard("logit " + str(msg))
    debug(msg)





##################################################################
##################################################################
# Main stuff
##################################################################
##################################################################


if __name__ == "__main__":


    #
    # EVIRON VARS
    #
    #
    # set Date format
    DATE_FORMAT = "%a %b %d %H:%M:%S %Y"
    #
    # internal debug on/off
    DEBUG = False
    VERBOSE = True



    qcli = qncli()
    sc = scrubber()
    #
    # just to see arguments due to crappy EEM
    oprint('RUNNING - EEM arguments:')
    oprint(str(sys.argv))

    #
    ### ARGS ###
    parser = argparse.ArgumentParser(description='unnumbered ecmp ping workaround')
    parser.add_argument('msg', action='store', help='device name/IP')
    parser.add_argument('-v', '--verbose', help="increase output verbosity", action = 'store_true')
    parser.add_argument('-d', '--debug', help="increase output verbosity", action='store_true')
    arguments = parser.parse_args()
    #reload = arguments.reload
    #
    # get timestamp - second resolution
    timestamp = datetime.datetime.now()
    timestamp = timestamp.replace(microsecond=0)

    sleep(2)

    msg = arguments.msg
    oprint(msg)

    if arguments.debug:
        DEBUG = True

    if arguments.verbose:
        VERBOSE = True
    else:
        VERBOSE = False

    if msg != "ARP":

    sc.scrub(msg, r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', mode=sc.FIRST_MATCH)
    oprint('ip address: ' + sc.data)
    addr = str(sc.data)

    out = qcli.onboard('ping ' + addr + ' count 2 timeout 0')
    oprint(out)
