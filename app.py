import reqRes
import re
import webbrowser
import subprocess
import datetime
from pyowm import OWM


def assistant(command):
 
#  conversation 
    if 'hello' in command:
        t = datetime.datetime.now()
        if t.hour < 12:
            greet = "Good Morning"
        elif t.hour > 12 and t.hour < 18:
            greet = "Good Afternoon"
        else:
            greet = "Good Evening"
                
        reqRes.botResponse("{}! What can I do for you?".format(greet))
    
    elif 'shutdown' in command:
        reqRes.botResponse("Enjoy your day!")
        exit() 

#   task 1 - Open website
    elif "open" in command:
        reg_ex = re.search('open (.+)', command)
        domain = reg_ex.group(1)
        if reg_ex:
            url = 'https://www.'+domain
            webbrowser.open(url)
            reqRes.botResponse("Opening {}".format(domain))
        else:
            pass
#   task 2 - Weather functionality
    elif "current weather" in command:
        reg_ex = re.search('current weather in (.+)', command)
        if reg_ex: 
            city = reg_ex.group(1)
            owm = OWM('043c95bd84b2bbcdcf7404f634788f85')
            mgr = owm.weather_manager()
            obs = mgr.weather_at_place(city)
            w = obs.weather
            s = w.status()
            t = w.temperature('celsius')
            reqRes.botResponse('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, s, t['temp_max'], t['temp_min']))

    elif "time" in command:
        t = datetime.datetime.now()
        h = t.hour
        m = t.minute
        s = t.second
        res = 'The time is {} hours {} minutes and {} seconds.'.format(h,m,s)
        print(res)
        reqRes.botResponse(res)

    elif "date" in command:
        t = datetime.datetime.now()
        d = t.day
        m = t.month
        y = t.year
        res = 'Today is {}, {}, {}.'.format(d,m,y)
        print(res)
        reqRes.botResponse(res)



# TODO: News feed
# TODO: Search


# #   task 2 - Launch System Application
#     elif 'launch' in command:
#         reg_ex = re.search('open (.+)', command)
#         appName = reg_ex.group(1)
#         if reg_ex:
#             subprocess.Popen("open", "-n", "/Applications")

#             reqRes.botResponse("Opening {}".format(appName))
#         else:
#             pass
