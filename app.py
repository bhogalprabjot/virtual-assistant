import reqRes
import re
import webbrowser
import subprocess




def assistant(command):
 
# TODO: greet according to time

#  conversation 
    if 'hello' in command:
        reqRes.botResponse("Hello! What can I do for you?")
    
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

# TODO: Weather functionality
# TODO: current time
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
