import re

string='I\'m a vlogger at https://www.google.com/'

pattern='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

url=re.findall(pattern,string)

print(url)