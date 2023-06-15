#Peer 2
import sys
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import threading
import time

PEER1_IP   = '192.168.118.6'
PEER1_PORT = 9999
PEER2_IP   = '192.168.118.7'
PEER2_PORT = 9991

buf=1024

print("Welcome to the Quiz")
print("Whoever wil answer first will win")
print("Allthe best".center(78,"*"))
print("\n\nWaiting for the player 1 to connect")
mySocket_peer1= socket(AF_INET,SOCK_DGRAM)
mySocket_peer2= socket(AF_INET,SOCK_DGRAM)
mySocket_peer2.bind((PEER2_IP,PEER2_PORT))

send_stop=False


def recieve():
        while True:
                
               
                (data,address)=mySocket_peer2.recvfrom(buf)
                data=data.decode('utf-8')
                if data=="conn":

                        global send_stop
                        send_stop=True
                        
                        break
        

def send():
        while True:
                
                mySocket_peer1.sendto("conn".encode('utf-8'),(PEER1_IP,PEER1_PORT))
                
                global send_stop
                if send_stop:
                        

                        break
                

t1=threading.Thread(target=recieve)
t1.start()
t2=threading.Thread(target=send)
t2.start()
t1.join()
t2.join()
buf2=1024

time_val=0
stop_time=False
def timecount():
        global time_val
        time_val=0
        global stop_time
        while True:
                time.sleep(1)
                if stop_time:
                        break
                time_val=time_val+1
data=None
def display():
        while True:
               	global data
                (data,address)=mySocket_peer2.recvfrom(buf)
                data=data.decode('utf-8')
                try:
                      if int(data):
                           break
                except ValueError:
                       continue
                
		

def dis():
		global data            
		global time_val
		if int(data)>=0:
			print("Player 1 Time taken: ",data,"\nPlayer 2 (you) Time taken: ",time_val)
			if int(data)>int(time_val):
				print("\nPlayer 2(you) win")
                        
			else:
				print("\nPlayer 1 wins. Try another time......")
		else:
			print("Player 1 answered incorrectly.\nPlayer 2 (you) win.")
                                        
t3=threading.Thread(target=timecount)
t3.start()
t4=threading.Thread(target=display)
t4.start()
print("\nConnected to Player 1\n")
print("Which of the following is a programming language\n\t1.Python\n\t2.English")
ans=int(input("Enter an option number"))

mySocket_peer1
mySocket_peer1.connect((PEER1_IP,PEER1_PORT))

while True:
    
    if ans==1:
        stop_time=True

        t3.join()
        mySocket_peer1.sendto(str(time_val).encode('utf-8'),(PEER1_IP,PEER1_PORT))
        print("\nYou guessed it correctly!!, waiting for the other player to finish")
       

        t4.join()
        print("Results: ")
       
        dis()
        break
        
    else:
       stop_time=True
       print("Sorry incorrect answer.\nTry another time...........")
       
       mySocket_peer1.sendto("-1".encode('utf-8'),(PEER1_IP,PEER1_PORT))
       
       
       break
