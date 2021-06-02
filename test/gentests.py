#
# BQ Enq 1
#
import os

TEST_PATH = os.path.dirname(__file__)

BQENQ1 = os.path.join(TEST_PATH,"bqenq_1.dat")
BQENQ2 = os.path.join(TEST_PATH,"bqenq_2.dat")
BQENQ3 = os.path.join(TEST_PATH,"bqenq_3.dat")
BQENQ4 = os.path.join(TEST_PATH,"bqenq_4.dat")
BQENQ5 = os.path.join(TEST_PATH,"bqenq_5.dat")
BQENQ6 = os.path.join(TEST_PATH,"bqenq_6.dat")

BQDEQ1 = os.path.join(TEST_PATH,"bqdeq_1.dat")
BQDEQ2 = os.path.join(TEST_PATH,"bqdeq_2.dat")
BQDEQ3 = os.path.join(TEST_PATH,"bqdeq_3.dat")
BQDEQ4 = os.path.join(TEST_PATH,"bqdeq_4.dat")
BQDEQ5 = os.path.join(TEST_PATH,"bqdeq_5.dat")
BQDEQ6 = os.path.join(TEST_PATH,"bqdeq_6.dat")

BSTENQ1 = os.path.join(TEST_PATH,"bstenq_1.dat")
BSTENQ2 = os.path.join(TEST_PATH,"bstenq_2.dat")
BSTENQ3 = os.path.join(TEST_PATH,"bstenq_3.dat")
BSTENQ4 = os.path.join(TEST_PATH,"bstenq_4.dat")
BSTENQ5 = os.path.join(TEST_PATH,"bstenq_5.dat")
BSTENQ6 = os.path.join(TEST_PATH,"bstenq_6.dat")

BSTDEQ1 = os.path.join(TEST_PATH,"bstdeq_1.dat")
BSTDEQ2 = os.path.join(TEST_PATH,"bstdeq_2.dat")
BSTDEQ3 = os.path.join(TEST_PATH,"bstdeq_3.dat")
BSTDEQ4 = os.path.join(TEST_PATH,"bstdeq_4.dat")
BSTDEQ5 = os.path.join(TEST_PATH,"bstdeq_5.dat")
BSTDEQ6 = os.path.join(TEST_PATH,"bstdeq_6.dat")

print("Eliminando los test generados anteriormente")

os.system("rm *.dat")

print("Generando los tests")

with open(BQENQ1,'a') as t:
    for i in reversed(range(1,1001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")

with open(BQENQ2,'a') as t:
    for i in reversed(range(1,2001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    
with open(BQENQ3,'a') as t:
    for i in reversed(range(1,3001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")

with open(BQENQ4,'a') as t:
    for i in reversed(range(1,4001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")

with open(BQENQ5,'a') as t:
    for i in reversed(range(1,5001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    
with open(BQENQ6,'a') as t:
    for i in reversed(range(1,6001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")


with open(BQDEQ1,'a') as t:
    for i in reversed(range(1,1001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")

with open(BQDEQ2,'a') as t:
    for i in reversed(range(1,2001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")
    
with open(BQDEQ3,'a') as t:
    for i in reversed(range(1,3001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")

with open(BQDEQ4,'a') as t:
    for i in reversed(range(1,4001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")

with open(BQDEQ5,'a') as t:
    for i in reversed(range(1,5001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")
    
with open(BQDEQ6,'a') as t:
    for i in reversed(range(1,6001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")

with open(BSTENQ1,'a') as t:
    for i in reversed(range(1,1001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")

with open(BSTENQ2,'a') as t:
    for i in reversed(range(1,2001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    
with open(BSTENQ3,'a') as t:
    for i in reversed(range(1,3001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")

with open(BSTENQ4,'a') as t:
    for i in reversed(range(1,4001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")

with open(BSTENQ5,'a') as t:
    for i in reversed(range(1,5001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    
with open(BSTENQ6,'a') as t:
    for i in reversed(range(1,6001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")

with open(BSTDEQ1,'a') as t:
    for i in reversed(range(1,1001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")

with open(BSTDEQ2,'a') as t:
    for i in reversed(range(1,2001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")
    
with open(BSTDEQ3,'a') as t:
    for i in reversed(range(1,3001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")

with open(BSTDEQ4,'a') as t:
    for i in reversed(range(1,4001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")

with open(BSTDEQ5,'a') as t:
    for i in reversed(range(1,5001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")
    
with open(BSTDEQ6,'a') as t:
    for i in reversed(range(1,6001)):
        t.write("enqueue p"+str(i)+"-"+str(i)+" "+str(i)+"\n")
    t.write("dequeue\n")