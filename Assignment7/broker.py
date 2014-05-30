from network import Listener, Handler, poll


handlers = {}  # map client handler to user name
names = {} # map name to handler
subs = {} # map tag to handlers

def broadcast(msg):
    for h in handlers.keys():
        h.do_send(msg)


class MyHandler(Handler):
    
    def on_open(self):
        handlers[self] = None
        
    def on_close(self):
        name = handlers[self]
        del handlers[self]
        broadcast({'leave': name, 'users': handlers.values()})
        
    def on_msg(self, msg):
        if 'join' in msg:
            name = msg['join']
            handlers[self] = name
            names[name] = self
            broadcast({'join': name, 'users': handlers.values()})
        elif 'speak' in msg:
            message = list()
            sendees = list()
            name, txt = msg['speak'], msg['txt']
            string = txt
            string2 = string.split()
            for words in string2:
                #print "c = ", c
                character = words[0]
                #print "d = ", d
                if character == '+':
                    subscribe_value = words[1:]
                    subs[subscribe_value] = list()
                    subs[subscribe_value].append(name)
                elif character == '#':
                    publish_value = words[1:]
                    if publish_value in subs:
                        if subs.values():
                            for sub in subs.values():
                                person_already_sent_to = 0
                                if sendees:
                                    for s in sendees:
                                        if sub == s:
                                            person_already_sent_to = 1
                                if person_already_sent_to == 0:
                                    if sub != '0':
                                        x = sub
                                        y = x[0]
                                        sendees.append(y)
                elif character == '-':
                    desub_value = words[1:]
                    if desub_value in subs:
                        if name in subs[desub_value]:
                            for s in subs[desub_value]:
                                if name == s:
                                    s = '0'
                elif character == '@':
                    send_to_client = words[1:]
                    print send_to_client
                    if send_to_client in names:
                        sent_to = 0
                        for s in sendees:
                            if send_to_client == s:
                                sent_to = 1
                        if sent_to == 0:
                            sendees.append(send_to_client)
                else:
                    message.append(words)
            mess = ' '.join(message)
            if mess != '':
                if sendees:
                    for s in sendees:
                        send_to = names[s]
                        send_to.do_send({'speak': name, 'txt': mess})
                else:
                    broadcast({'speak': name, 'txt': mess})


Listener(8888, MyHandler)
while 1:
    poll(0.05)