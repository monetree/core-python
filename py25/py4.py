#Unpickle - deserialization
import pickle
f = open('emp.dat', 'rb')
while True:
    try:
        e = pickle.load(f)
        e.display()
    except EOFError:
        print('end of file reached...')
        break
f.close()