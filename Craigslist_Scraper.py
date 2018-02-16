import urllib2
import re
import time
from random import randint

import winsound

def cl():
    lastResults2 = None
    i=0
    while i<10000:
        req = urllib2.Request("http://orlando.craigslist.org/search/zip")
        response = urllib2.urlopen(req)
        htmltext = response.read()
        regex = '<small> (.+?)</small>'
        pattern = re.compile(regex)
        results = re.findall(pattern,htmltext)
        
        regex2 = 'class="hdrlnk">(.+?)</a>'
        pattern2 = re.compile(regex2)
        results2 = re.findall(pattern2,htmltext)
        
        regex3 = 'data-id="(.+?)"'
        pattern3 = re.compile(regex3)
        results3 = re.findall(pattern3,htmltext)
        results3 = results3[:3]

        results4 = []
        for a in results3:
            new_elem = "http://orlando.craigslist.org/zip/" + a + ".html"
            results4.append(new_elem)
        

        if results2 != lastResults2:
            winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)

        lastResults2 = results2

        print "\n"
        print results[:3]
        print "\n"
        print results2[:3]
        print "\n"
        print results4
        

        time.sleep(randint(60,180))
        i+=1;
cl()



