# Sublime relaxation beacon: <br/>

## Project Description <br/>
"Do you feel constantly tired in your day to day life? Sense everything falling apart and control slipping away? Constantly questioning existence, universe, life and everything, and you feel that the answer is not just mere 42? Prepare yourself to experience the magical power of relaxation beacon. Our network of connected devices will detect your stress from overworking and will send you on a journey of tranquility. The scanner is connected to a server which in turn is connected to a "beacon"- resonance tube with mounted speakers which will play relaxing music suitable for destressing. Sublime Relaxation Beacon - the beacon that cares about you." <br/>

Through this projected, we attempted to activate the atriums, by turning it as a relaxation hub with brainwave music for tired and stressed students. The sender pi would be running at the stress-induced sites such as the library and scanning the MAC address of the students at the location. Those MAC Addresses would be sent to the database, and when the receiver pi at the atrium scans a MAC Address from the database, the receiver.py would remove the existing MAC address and welcome the stressed person with a "bong". <br/>

## Process <br/>
Using all the components below, we came up with code sender.py (running at the site) and receiver.py (running at the atrium).

### Networking piece:

1. Scanning the Wifi <br/>
```pip install python3-nmap ``` or ```sudo apt-get install nmap``` <br/>
Then read through <a href="https://bitbucket.org/xael/python-nmap/src"> nmap </a> to learn more about network scanning.

2. Using a database (Firebase): <br/>
Networked the two raspberry pi at different location using the database function on Firebase. <br/>
As raspberry pi works on python, used <a href="https://github.com/thisbejim/Pyrebase"> pyrebase </a>, a simple python wrapper for the Firebase API.<br/>
