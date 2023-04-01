import pika, sys, os
import xml.etree.ElementTree as ET
import socket
import time



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='Test')
    CARBON_SERVER = '127.0.0.1'
    CARBON_PORT = 2003

    def callback(ch, method, properties, body):
        # print(" [x] Received %r" % body)    
        root = ET.fromstring(body)
        # print(body)
        attributes = root.attrib
        x = int(attributes.get ('x'))
        y = int(attributes.get ('y'))
        print(y) 
        # print("y")   
        message = 'sdaia.ibm.t %d %d\n'%(y, x)
        byt=message.encode()
        print(byt)
        # print("byt")
        sock = socket.socket()
        sock.connect((CARBON_SERVER, CARBON_PORT))
        sock.sendall(byt)
        print("sent")
        sock.close()

    print("b4")
    channel.basic_consume(queue='Test', on_message_callback=callback, auto_ack=True)
    print("a4") 
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)