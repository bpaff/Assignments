from network import Handler, poll
import sys
from threading import Thread
from time import sleep


myname = raw_input('What is your name? ')

class Client(Handler):
        
    def on_close(self):
        done = True
    
    def on_msg(self, msg):
        temp = []
        print msg
        for m in msg.values():
            temp.append(m)
            print m
        print "the first index is", temp[0]
        if temp[0] == 'join':
            name = temp[1]
            print name, " has joined the room."
        elif temp[0] == 'quit':
            name = temp[1]
            print name, " has left the room."
        else:
            name = temp[1]
            print name, ":", temp[0]
            
        
        
host, port = 'localhost', 8888
client = Client(host, port)
message = {'join': myname}
client.do_send(message)

def periodic_poll():
    while 1:
        poll()
        sleep(0.05) # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True # die when the main thread dies
thread.start()
done = False
while done == False:
    mytxt = sys.stdin.readline().rstrip()
    client.do_send({'speak': myname, 'txt': mytxt})