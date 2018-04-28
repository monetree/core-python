#notify() and wait() methods are useful in efficient thread communication
#when the consumer should wait till all the data is completed and then use
#the data, we should go for notify() and wait() methods.
#notify() -> sends message to a waiting thread
#notify_all() -> sends message to all waiting threads at once
