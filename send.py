import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Test')
file_opened = open('new.txt')
for line in file_opened:
    print(line)
    channel.basic_publish(exchange='', routing_key='Test', body=line)
    print("Message Sent")
connection.close()