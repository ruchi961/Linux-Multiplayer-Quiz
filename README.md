# :green_circle: Linux-Multiplayer-Quiz
* **Operating System Innovative Project, python scripts written in the Linux Operating System with Socket communication and logic for a multiplayer Quiz game.**
* Using the concepts of **Peer-to-Peer network and distributed system**, implementing a **multiplayer quiz** which works on two different systems connected. 
* In order **to start the quiz** the users have to wait **till other user joins in**. 
* Once **both the users are available**, users on these two different machines can **play quiz simultaneously**. 
* Depending **on the time taken the winner(with less time)** will be selected. 
* **Cases with incorrect answers are also reflected**. 
* scratch implementation is done in virtualbox two

## > Information

* <b>Language:</b> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" height=50> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"  height=50/> Oracle VirtualBox 
          

* <b>Date Created :</b> Innovative Project

* <b> Subject :</b> Operating System

* <b>Date Created :</b> November 2020

* <b>Concepts used :</b> 
  *  Multithreading
  *  Socket Communication
  *  Game stratergy
  *  Mimicing distributed computing in linux operating system with python scripts
  *  Exception Handling
  *  Virtual Machine
  *  Communication betwen multiple Linux Virtual Machines


## > Package
* sys
* socket
* time
* threading

## > Install Package (Dependency)
```
cd to_Scripts
```

```
pip install threading
```

```
pip install socket
```

## > Output 

Users waiting for each other
![image](https://github.com/ruchi961/Linux-Multiplayer-Quiz/assets/128241982/52676961-f342-4883-8257-f2c46b6ddac5)


Users are connected
![image](https://github.com/ruchi961/Linux-Multiplayer-Quiz/assets/128241982/274cd18a-59e5-4f00-be69-54d616c3c2c3)


Case 1: One user with incorrect and other with correct answer
![image](https://github.com/ruchi961/Linux-Multiplayer-Quiz/assets/128241982/1f593699-0e96-4778-bad2-797fe26e3139)


Case 2: Both user answer correctly. User with less time wins.
![image](https://github.com/ruchi961/Linux-Multiplayer-Quiz/assets/128241982/4c67a092-d02d-4dd4-8dfd-1f09b048c3c1)


Case 3: Both users answer incorrectly
![image](https://github.com/ruchi961/Linux-Multiplayer-Quiz/assets/128241982/77eace40-4ca4-4811-9e16-721cd950e97e)


*_ Demo video for the implementation of the project _*


## > Prerequst to run
**Linux Systems must be connected in LAN in the virtualbox. (with Bridge Connection or any other connection so their IP are in the one network) **


## > Run

* Linux Machine Terminal
```
cd to_python_files
```

```
python3 Peer1Player1Machine1.py
```


* Another Linux Machine's Terminal
```
python3 Peer1Player1Machine1.py
``````
cd to_python_files
```

```
python3 Peer1Player1Machine1.py
```
