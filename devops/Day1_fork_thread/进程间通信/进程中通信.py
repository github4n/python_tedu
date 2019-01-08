# -*-coding:utf-8-*-
import os
import time
from multiprocessing import Process, Queue


def write(q):
    print('启动写子进程%s' % os.getpid())
    for chr in ['A', 'B', 'C', 'D']:
        q.put(chr)
        time.sleep(1)
    print('结束写进程%s' % os.getpid())


def read(q):
    print('启动读子进程%s' % os.getpid())
    while True:
        value = q.get(True)
        print("value=" + value)
    print('结束读子进程%s' % os.getpid())


if __name__ == '__main__':
    # 父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()      # 读子进程为死循环，不能自行结束,强制结束
    print('父进程结束')


