from __future__ import with_statement
import sys
try:
    import queue
except ImportError:
    import Queue as queue
import random
import Pyro4.core
from workitem import Workitem

Pyro4.config.SERIALIZER = 'pickle'
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

def readNumbers(path):
    print("\nReading numbers")
    with open(path) as f:
        lines = f.read().splitlines()
    numbers = [int(e) for e in lines]
    return numbers

def placeWork(master, numbers):
    print("\nPlacing work items into master queue")
    for i in range(len(numbers)):
        item = Workitem(i+1, numbers[i])
        master.putWork(item)

def collectResults(master, item_count):
    print("\nGetting results from master queue")
    results = {}
    while len(results) < item_count:
        try:
            item = master.getResult()
            print("Got result: %s (from %s)" % (item, item.processedBy))
            results[item.data] = item.result
        except queue.Empty:
            print("Not all results available yet (got %d out of %d). Work queue size: %d" %  \
                    (len(results), item_count, master.workQueueSize()))
    return results

def writeResults(results, path):
    print("\nWriting results")
    with open(path, 'w') as f:
        for (number, factorials) in results.items():
            f.write(str(number) + ': ' + ', '.join(map(str,factorials)) + '\n')

def main():
    disp_address = str(sys.argv[1])
    numbers_path = str(sys.argv[2])
    results_path = str(sys.argv[3])

    numbers = readNumbers(numbers_path)

    with Pyro4.core.Proxy("PYRO:master@" + disp_address) as master:        
        placeWork(master, numbers)
        results = collectResults(master, len(numbers))

    writeResults(results, results_path)

if __name__=="__main__":
    main()
