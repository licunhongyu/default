import sys
import time
import datetime

x=sys.stdin.read().strip().split('\n')
print len(x) 

count = 100000

start = datetime.datetime.today()
for j in range(0, count):
    if j % 10 == 0:
        sys.stdout.write('\r%10d %%' % j)
        sys.stdout.flush()
sys.stdout.write('\n')
end = datetime.datetime.today()
print (end - start) / count