############################################################
#                                                          #
#       This code written by A.L.Zulas                     #
#       Code purpose was just to check a website and       #
#         alert once the site had changed                  #
#       Code writen in Fall of 2018                        #
#                                                          #
#                                                          #
#                                                          #
############################################################

import urllib3
import certifi
import time
import smtplib
import sys
from random import randint

#Basic Premise:
#
#This code is basically the same as the other code, it just checks the "Hotel Registration Page" instead of the "Class registration Page"
#Outcome of this code? Hotel registration dropped about 5 minutes after class registration. :)
#
#The Madrona Fiber Arts Festival occured for someting like 20 years, and 2019 was set to be their last year
#So, I really wanted to attend and take a couple of classes for their last event
#However, the way in which they run Madrona, is that they tell people what day that reistration will occur, but not what time
#This means that there are a bunch of people refreshing their tab constantly from 9am until whenever the page changes
#To save myself the trouble, and allow myself to do other things while I waited, I created this script. 
#It's kind of a cheat, but it worked like a charm!

#these variables save the past state of the website, and save the new state of the website and compare. 
oldRequest = None
newRequest = None

#This goes to the website, and requests all data from the registration page
http = urllib3.PoolManager(
	cert_reqs='CERT_REQUIRED',
	ca_certs=certifi.where())
r = http.request('GET', 'http://madronafiberarts.com/hotel-travel-information/make-reservations/')
#On the first go round, the old data and the new data will be the same, because we have no old data to compare against.
newRequest = r.data
oldRequest = r.data

#So long as the old data and new data are the same, keep requesting the website
while (oldRequest == newRequest):
	#Pick a random amount of time, so we don't look like a bot, and we just look like everyone else
	randtime = randint(30, 65)
	#Wait that amount of time
	time.sleep(randtime)
	print("checking now after " + str(randtime) + " seconds")
	
	#Set the old request as whatever you pulled last time
	oldRequest = newRequest
	#Grab new data from the website
	http = urllib3.PoolManager(
		cert_reqs='CERT_REQUIRED',
		ca_certs=certifi.where())
	r = http.request('GET', 'http://madronafiberarts.com/hotel-travel-information/make-reservations/')
	#Set that as the new data and then repeat the check
	newRequest = r.data
	#print(r.status)
	
#When the website finally changes and breaks out of the while loop, print to the screen and make the computer complain a bunch.
print("HOTEL REZ!!!!!")

while(True):
	sys.stdout.write('\a')
	sys.stdout.flush()
	time.sleep(1)
