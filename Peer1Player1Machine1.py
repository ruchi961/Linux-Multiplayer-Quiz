#!/usr/bin/python3
import socket 
import sys
from threading import Thread
import time
#acting as a server
PEER1_IP="192.168.118.6"
PEER1_PORT=9999
ss_peer1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss_peer1.bind((PEER1_IP,PEER1_PORT))
buf=1024
#acting as a client
PEER2_IP="192.168.118.7"
PEER2_PORT=9991


ss_peer2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
stop_send=False

print("Welcome to the Quiz")
print("Whoever will answer first will win")
print("All the best".center(78,"*"))
print("\nWaiting for Player 2 to connect\n")
def send():
	while True:
		ss_peer2.sendto("conn".encode('utf-8'),(PEER2_IP,PEER2_PORT))
		
		global stop_send
		if stop_send:
			break
def recieve():
	while True:
		(data,address)=ss_peer1.recvfrom(buf)
		data=data.decode('utf-8')
		if data=="conn":

			global stop_send
			stop_send=True
			
			break
		
t1=Thread(target=recieve)
t1.start()
t2=Thread(target=send)
t2.start()
t1.join()
t2.join()
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
	global data
	while True:
		(data,address)=ss_peer1.recvfrom(buf)
		data=data.decode('utf-8')
		try:
			if int(data):
				break
		except ValueError:
			continue
		



def dis():	
		global time_val
		global data
		if int(data)>=0:
			print("Player 1 (you) Time Taken: ",time_val,"\nPlayer 2 Time Taken: ",data)	
			if int(data)>int(time_val):
				print("Player 1 (you) win")
				
			else:
				print("Player 2 wins. Try another time...........")
		else:
			print("Player 2 answered incorrectly !!, \nPlayer 1 (you) win")
			 
t3=Thread(target=timecount)
t3.start()
t4=Thread(target=display)
t4.start()
print("\nConnected to Player 2 \n")
print("Which of the following is a programming language\n\t1.Python\n\t2.English")
ans=int(input("Enter an option number"))
buf2=1024


while True:
	if ans==1:
		stop_time=True

		t3.join()
		
		ss_peer2.sendto(str(time_val).encode('utf-8'),(PEER2_IP,PEER2_PORT))
		print("\nYou guessed it correctly!!, Waiting for the other player to complete")
		
		#t4=Thread(target=display)
		t4.join()
		print("Results: ")
		dis()
		break
		

		
	else:
		stop_time=True
		print("Sorry Incorrect answer!!\nTry another time............")
		
		ss_peer2.sendto("-1".encode('utf-8'),(PEER2_IP,PEER2_PORT))
		break
