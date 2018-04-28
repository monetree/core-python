'''
# when a thread wants to lock an object which has been
# already by another thread and the second thread wants to lock the first
# object which is already locked by the first thread, then both the threads will go
# into waiting state forever. This is called thread deadlock.
# if dead lock happens entire will halt
# Solution of thread deadlock: no
# the programmer should design the program in order not to get into deadlock situation.
'''