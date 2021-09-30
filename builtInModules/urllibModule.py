import urllib.request
import urllib.parse

# GET request

x = urllib.request.urlopen('https://www.google.com')

# prints google home page html
print(x.read())

# POST request

url = 'http://pythonprogramming.net'
values = {'s': 'basic', 'submit': 'search'}
headers = {
  'my': 'header'
}

# encode to create query string from dictionary
data = urllib.parse.urlencode(values)
# encode to utf-8
data = data.encode('utf-8')
request = urllib.request.Request(url, data, headers=headers)
response = urllib.request.urlopen(request)
responseData = response.read()

print(responseData)