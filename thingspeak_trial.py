import urllib2
import time
print('we start here')
response=None
temp=59
rpm=100














while True:
    url_new='https://thingspeak.com/update?key=7uoxpoxpx6soqkd0&field1='+str(temp)+'&field2='+str(rpm)
    print rpm
    print temp
    rpm=rpm-5
    temp=temp+10
    
    response=urllib2.urlopen(url_new)
    print response.code
    print("--------------------------------")
    time.sleep(15)
    
