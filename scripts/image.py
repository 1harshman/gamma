#!/usr/bin/env python

from PIL import Image, ImageFilter
import numpy as np

im00 = Image.open('00.jpg')
im05 = Image.open('05.jpg')
im10 = Image.open('10.jpg')
im15 = Image.open('15.jpg')
#print (im.size, im.mode)
#im = im.filter(ImageFilter.EDGE_ENHANCE)
#im = im.filter(ImageFilter.CONTOUR)
x1 = int(1100)
y1 = int(650)
imWidth = int(500)
imHeight = int(275)
x2 = x1 + imWidth
y2 = y1 + imHeight
box = (x1, y1, x2, y2)
crim00 = im00.crop(box)
crim05 = im05.crop(box)
crim10 = im10.crop(box)
crim15 = im15.crop(box)

# unpack the bands into 3 separate 2D arrays.
red00, green00, blue00 = np.array(crim00).T
red05, green05, blue05 = np.array(crim05).T
red10, green10, blue10 = np.array(crim10).T
red15, green15, blue15 = np.array(crim15).T

blueEdit00 = np.array([[blue00[i, j] for i in range(imWidth)] for j in range(imHeight)]).T
blueEdit05 = np.array([[blue05[i, j] for i in range(imWidth)] for j in range(imHeight)]).T
blueEdit10 = np.array([[blue10[i, j] for i in range(imWidth)] for j in range(imHeight)]).T
blueEdit15 = np.array([[blue15[i, j] for i in range(imWidth)] for j in range(imHeight)]).T

redEdit = [imWidth, imHeight] # list(red)
greenEdit = [imWidth, imHeight] #list(green)
redCt = 0

blueCt00 = 0
blueCt05 = 0
blueCt10 = 0
blueCt15 = 0

greenCt = 0
redThreshold = 160
blueThreshold00 = np.mean(blue00)-(15-(np.mean(blue00)/10))
blueThreshold05 = np.mean(blue05)-(15-(np.mean(blue05)/10))
blueThreshold10 = np.mean(blue10)-(15-(np.mean(blue10)/10))
blueThreshold15 = np.mean(blue15)-(15-(np.mean(blue15)/10))

# for x in xrange(0, imWidth):
#     for y in xrange(0,imHeight):
#         if red[x][y] < redThreshold:
#             redEdit[x,y] = 255
#             redCt += 1
# print('R pixels = ', str(redCt))
#
# redIm = Image.fromarray(np.dstack([item.T for item in (red,green,blue)]))


for i in range(imWidth):
    for j in range(imHeight):
        if blue00[i, j] < blueThreshold00:
            if blue00[(i+20),j]<blueThreshold00 or blue00[(i-20),j]<blueThreshold00:  
                blueEdit00[i, j] = 255
                blueCt00 += 1
        if blue05[i, j] < blueThreshold05:
            if blue05[(i+20),j]<blueThreshold05 or blue05[(i-20),j]<blueThreshold05:
                blueEdit05[i, j] = 255
                blueCt05 += 1
        if blue10[i, j] < blueThreshold10:
            if blue10[(i+20),j]<blueThreshold10 or blue10[(i-20),j]<blueThreshold10:
                blueEdit10[i, j] = 255
                blueCt10 += 1
        if blue15[i, j] < blueThreshold15:
            if blue15[(i+20),j]<blueThreshold15 or blue15[(i-20),j]<blueThreshold15:    
                blueEdit15[i, j] = 255
                blueCt15 += 1
                    
print(blueCt00)
print('05 B pixels = ', str(blueCt05))
print('10 B pixels = ', str(blueCt10))
print('15 B pixels = ', str(blueCt15))
        
blueIm00 = Image.fromarray(np.dstack([item.T for item in (red00,green00,blueEdit00)]))
blueIm05 = Image.fromarray(np.dstack([item.T for item in (red05,green05,blueEdit05)]))
blueIm10 = Image.fromarray(np.dstack([item.T for item in (red10,green10,blueEdit10)]))
blueIm15 = Image.fromarray(np.dstack([item.T for item in (red15,green15,blueEdit15)]))

#
# for x in xrange(0, 350):
#     for y in xrange(0,350):
#         if g[x,y] < 150:
#             g[x,y] = 0
#             Gct += 1
# print('G pixels = ', str(Gct))
#
# gim = Image.fromarray(np.dstack([item.T for item in (r,g,b)]))


# Put things back together...
#crim = Image.fromarray(np.dstack([item.T for item in (red,green,blue)]))

# select regions where red is less than 100
# mask = source[R].point(lambda i: i < 100 and 255)

#crim.save('output.jpg')
#redIm.save('rim.jpg')
blueIm00.save('blueIm00.jpg')
blueIm05.save('blueIm05.jpg')
blueIm10.save('blueIm10.jpg')
blueIm15.save('blueIm15.jpg')
#greenIm.save('gim.jpg')
