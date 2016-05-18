'''
This is a quick and dirty program to download the most recent 12 images/videos from an instagram page. 

issues:

doesn't download videos (only thumbnails)
can't download older pictures

'''

import urllib.request
import os 

print("Please enter the username you want to scrape")

user = input() # get desired username from user input 

url = 'https://www.instagram.com/' + user + '/'
path = 'dl/' + user + '/' #makes directory with desired username to save the media 

if not os.path.exists(path):
	os.makedirs(path) # make dl directory

response = urllib.request.urlopen(url)
html = response.read()
html = bytes.decode(html) #retrieve html and decode to string

count = 0

while (html.find('display_src":"https') != -1):
	start = html.find('display_src":"https')
	start += 14 #now start points to h in https
	html = html[start:] #cut everything before the first link
	start = 0 #now start again points to h in https
	end = html.find('.jpg') # end of thelink
	end += 4 #end of .jpeg
	resource = html[start:end] #location of image
	resource = resource.replace('\/', '/')
	file_name = path + resource.split('/')[-1] # everything after the last backslash
	urllib.request.urlretrieve(resource,file_name)
	count += 1
	html = html[end:]

#print(html)

# a[start:end+5]