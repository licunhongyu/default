import sys
import datetime

message = sys.stdin.read()
if message.strip() == 'error':
    raise ValueError()

sys.stderr.write("ERROR: " + message)

#sys.stdout.write("OUTPUT: " + message)

# sys.stdout
# sys.stderr

"""
now = datetime.datetime.today()

if now.hour > 17 and now.hour < 24:
    print "Good evening!"
if now.hour > 12 and now.hour <= 17:
    print "Good afternoon!"
if now.hour <= 12:
    print "Good morning!"

print "Hello World!"
"""