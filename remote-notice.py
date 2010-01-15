#!/usr/bin/env python
from optparse import OptionParser

import pynotify
import re
import simplejson as json
import socket

def run(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('',port))
        s.listen(10)
        while 1:
            client, address = s.accept()
            data = recv(client)
            handleResp(data)
            client.close() 
    except KeyboardInterrupt:
        s.close()

def recv(client):
    data = []
    while True:
        d = client.recv(1024)
        data.append(d)
        if len(d) < 1024: break
    return ''.join(data)

def handleResp(data):
    try:
        d = json.loads(data)
        msg(d['title'], d['msg'])
    except Exception as e:
        print data
        print e

def escape(s):
    return re.sub('''(['"])''', '', s)

def msg(title, msg, appname='remote-notice'):
    if pynotify.init(appname):
        n = pynotify.Notification(escape(title), escape(msg), "dialog-warning")
        n.show()
    else:
        print "Unable to send notification"

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port', help='server port', \
                                      type='int', default=33333)
    (opts, args) = parser.parse_args()
    run(opts.port)

