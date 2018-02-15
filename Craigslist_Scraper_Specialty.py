import urllib2
import re
import pygame
import time
from random import randint
import webbrowser
from winsound import PlaySound, SND_ALIAS
i = 0
lastResults = None
lastx = None
desired = ['pool table','billiard','trailer','bicycle','bike','engine','tv stand','shelving','shelves','treadmill','flatscreen','LED','ladder','cushion','carseat','wheelchair','mower']
j=0
print 'Choose your keywords to search for\n'
print 'Some common valuable items could be \npool table, billiard, trailer, bicycle, \nbike, engine, tv stand, shelving, \nshelves, treadmill, flatscreen, LED, \nladder, seat, cushion, carseat, \nwheelchair, curb alert, curb call, curb\n, mower, lawnmower\n'
print 'Hit enter after each keyword added or type nothing and hit enter to continue \n'
while j<1:
    specific = raw_input("Add to the list ")
    if specific == '':
        j+=1
    else:
        desired.append(specific)
print desired
while i<10000:
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/54.0.2840.99')]
    url = opener.open("http://orlando.craigslist.org/search/zip")
    url2 = opener.open("http://orlando.craigslist.org/search/sss?sort=rel&query=pool%20table")
    htmltext = url.read()
    regex = 'class="result-title hdrlnk">(.+?)</a>'
    pattern = re.compile(regex)
    results = re.findall(pattern,htmltext)

        
    regex3 = 'data-id="(.+?)"'
    pattern3 = re.compile(regex3)
    results3 = re.findall(pattern3,htmltext)
    results3 = results3[:3]

    results4 = []
    for a in results3:
        new_elem = "http://orlando.craigslist.org/zip/" + a + ".html"
        results4.append(new_elem)

    results = [element.lower() for element in results]
    if results != lastResults:
        for x in results[:3]:
            for z in desired:
                if z in x:
                    if x != lastx:
                        print z
                        PlaySound("SystemExit", SND_ALIAS)
                        from twilio.rest import TwilioRestClient
                        client = TwilioRestClient("ACf4cae3c213df8879c64e7ad65935b37c", "725ae08e3996068eb70258787a075efa")

                        client.messages.create(from_='+14072581360',
                                                to='+*(your number here)*',
                                                body=(z))
                        lastx = x
                        
                            

        print results[:3]
        print "\n"
        print results4
        print '\n'
    lastResults = results
    time.sleep(randint(60,120))
    i+=1


        
            
