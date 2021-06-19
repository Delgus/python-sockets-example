from urllib import request

response = request.urlopen("http://example.com")
print(response.read().decode())