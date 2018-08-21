# Pyro-python
This is the solution of problem:
Formulation of the problem

Improve the disassembled in the classroom implementation of the scheme "master-workers" (see the code below for the assignment):

    Implement in the wizard support for simultaneous maintenance (processing tasks) of several clients in the order in which they receive jobs;
    Implement in the wizard the detection and processing of failures related to work processes ("fall" or temporary "freezing" of the process, failure of the network between the master and the worker);
    Implement in the working processing of network failures between the master and the worker (the worker must try to reconnect with the master);
    Implement in the client the processing of network failures between the master and the client (the client should try to reconnect with the master).

Thus, the advanced implementation should function correctly (all tasks sent by clients are eventually executed and delivered to clients) in the conditions of network and worker failures.

In addition to correctness, the implementation should be effective, minimizing the times of detection of failures and the expectation of results by customers. At the same time, a reasonable balance should be maintained between efficiency and overhead (network load).

Finally, the implementation should work well not only on tests, but also under arbitrary conditions, thus making no a priori assumptions about the times of receipt and processing of tasks.
