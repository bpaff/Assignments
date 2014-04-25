from network import Listener, Handler, poll

 
handlers = {} # map client handler to user name
event_queue = []
messages = []
class Client:
    
    def __init__(self):
        pass
class MyHandler(Handler):
     
    def on_open(self):
        event_queue.append(('join', self))
         
    def on_close(self):
        event_queue.append(('quit', self))
     
    def on_msg(self, msg):
        i=0
        temp = list()
        lie = 0
        for s in msg.values():
            temp.append(s)
        message = temp[0]
        messages.append(message)
        for m in messages:
            print m
 
 
port = 8888
server = Listener(port, MyHandler)
while 1:
    poll(timeout=0.05) # in seconds
    for event, handler in event_queue:
        if event == 'quit':
            del handlers[handler]
        elif event == 'join':
            handlers[handler] = Client()
            
    event_queue = []
    for h in handlers:
        for m in messages:
            h.do_send(m)
            print "sent msg"
