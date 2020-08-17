#!/usr/bin/env python
# coding: utf-8

# In[16]:


import zipfile
from zipfile import ZipFile as zp

from PIL import Image
import pytesseract as ps
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
z= zp('readonly/images.zip') 
print(z.infolist())

z.extractall()
for i in z.infolist():
    print(i.filename)
    img = Image.open(i.filename)
    ps.image_to_string(img)
    cv_img = cv.imread(i.filename)
# tesseract to find Christopher in text.. when found use openCv on that page and make contact sheet using PIL


# In[1]:


import zipfile
from zipfile import ZipFile as zp

from PIL import Image
import pytesseract as ps
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
z= zp('readonly/images.zip') 
print(z.infolist())

z.extractall()
d=dict()
for i in range(len(z.infolist())):
    use= z.infolist()[i]
    img = Image.open(use.filename)
    d[use.filename]=ps.image_to_string(img).replace('\n',' ')
    


# In[19]:


#dict with image filename and text
import math, PIL

for i in z.infolist():
    cropped_images=[]
    if 'Mark' in d[i.filename]:
        cv_img = cv.imread(i.filename)
        gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.4)
        print('Results found in file',i.filename)
        if len(faces):
            pil_im = Image.open(i.filename)
            for x,y,w,h in faces:
                im = pil_im.crop((x,y,w+x,h+y))
                im.thumbnail((100,100))
                cropped_images.append(im)
            # now we have to make contact_sheet
            first_image = cropped_images[0]
            contact_sheet = PIL.Image.new(im.mode, (500, 100*math.ceil(len(cropped_images)/5) ))
            x=0
            y=0
            for img in cropped_images:
                contact_sheet.paste(img, (x,y))
                if x+100== 500:
                    x=0
                    y=y+100
                else:
                    x=x+100
            display(contact_sheet)
        else:
            print('But there were no faces in that file!')


# In[16]:


cv_img = cv.imread(use.filename)
gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.35)
print(len(faces))

