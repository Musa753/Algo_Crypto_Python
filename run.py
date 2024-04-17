import multiprocessing

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=exec(open("sender_I.py").read()))
    p2 = multiprocessing.Process(target=exec(open("receiver_I.py").read()))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
