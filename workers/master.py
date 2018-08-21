from __future__ import print_function
import sys
try:
    import queue
except ImportError:
    import Queue as queue
import Pyro4.core

Pyro4.config.SERIALIZER = 'pickle'
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

class Master(object):
    def __init__(self):
        self.workqueue = queue.Queue()
        self.resultqueue = queue.Queue()

    @Pyro4.expose
    def putWork(self, item):
        self.workqueue.put(item)

    @Pyro4.expose
    def getWork(self, timeout=5):
        return self.workqueue.get(timeout=timeout)

    @Pyro4.expose
    def putResult(self, item):
        self.resultqueue.put(item)

    @Pyro4.expose
    def getResult(self, timeout=5):
        return self.resultqueue.get(timeout=timeout)

    @Pyro4.expose
    def workQueueSize(self):
        return self.workqueue.qsize()

def main():
    # HOST:PORT
    address = str(sys.argv[1]).split(':')
    host = address[0]
    port = int(address[1])

    daemon = Pyro4.core.Daemon(host, port)
    master = Master()
    uri = daemon.register(master, "master")

    print("Master is running: " + str(uri))
    daemon.requestLoop()

if __name__=="__main__":
    main()
