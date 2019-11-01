# Clout chaser is script written for sharing photos from reddit to other places. 
# In this instance it is being shared on Instagram, but can be repurposed for Twitter which will be coming soon. 
# Importing the needed dependencies

import praw
from bs4 import BeautifulSoup as bs
import os
import urllib
import urllib.request
import glob
from InstagramAPI import InstagramAPI
import time

#creating reddit instance 
# You will beed to create your own reddict account to get access
reddit = praw.Reddit(client_id = '', 
                     client_secret ='',
                     user_agent = '', 
                     password = '',
                     username = ''
                     )
#selecting which subreddit you want to get the images from 
subreddit= reddit.subreddit('')#subreddit name can be passed 
hot = subreddit.new()#In this instance I choose new, but you can sort for hot, trending
image_links = [] #initalize an empty array for image paths 
ids=[]# empty array for post_id for future validation so same post isnt uploaded. 

for item in hot:
    #selecting ext that have the jpg extension, and appending them to the empy list image_links
    if item.url[-3:] == 'jpg':
        image_links.append(item.url)
        ids.append(item.id)
        # Initalizing a count, we don't want to many photos populating.
        count = 0 
        for link in image_links: 
            for title in ids:
                full_name = str(count) +'.jpg'
                url = link
                file_path = 'File Path'+ full_name
                urllib.request.urlretrieve(url, file_path)
                if count <10:
                    count+=1
                else:
                    break
# Now that all those images have been saved. We can move forward to the instagram portion. 
# create a variable to place password and login information. 
#Instagram login
login=""
#Instagram password 
password= ""

InstagramAPI = InstagramAPI(login, password)
InstagramAPI.login()  # login

# Creating 
jpgfiles = []
#We use the glob module to search through a specified directory, and * x to denote which file that you are searching for. 
for file in glob.glob("File Path *.jpg"):
    if file[-3:] == 'jpg':
        jpgfiles.append(file)    

#Loogping through the array to create specific 
for image in jpgfiles:
    #some images may not conform to IG size dimensions. 
    photo_path = image
    # You can add topics based on trending tags, or up to you. 
    caption = ""
    try:
        InstagramAPI.uploadPhoto(photo_path, caption=caption)
        #gives it enough time to upload. 
        os.unlink(image) #removes path from array, no duplicates, could use os to remove from directory as well. 
        time.sleep(30)
    except:
        print('error')
        os.unlink(image)

# Futre iterations will be using ML to classify images, and generating tags based on classification 
# Tweet images from collection as well. 
# Even Tweet content from post comments. 
# Fork script and play around with it if you like it. 
