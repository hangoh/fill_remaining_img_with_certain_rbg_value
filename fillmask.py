import numpy as np
import os
import cv2

def fillMask(label):
    
    '''
    pixel classes
    '''
    urban_land = (0, 255, 255)
    argriculture_land = (255, 255, 0)
    range_land = (255, 0, 255)
    forest_land = (0, 255, 0)
    water = (0, 0, 255)
    barren_land = (255, 255, 255)
    unknown = (0, 0, 0)
    
     '''
     replace all pixel that is not equal to the rgb value stated to a certain rgb value,
     
     rgb(255,255,0) was the value replaced by the code below
     '''
    label[np.all(label!=(argriculture_land and range_land and forest_land and water and barren_land ) ,axis=-1)] = (255,255,0)
    
    '''
    to check if their are any pixel which doesn't have an cetain rgb value that represent a class stated above
    will return [] if all pixel in the image have an cetain rgb value that represent a class stated above
    '''
    
    left = label[np.all(label!=(urban_land and argriculture_land and range_land and forest_land and water and barren_land ) ,axis=-1)]
    print(left)
    return label


def start(input):
    print(input)
    im = cv2.imread(input)
    output = fillMask(im)
    try:
        print("saving...")
        status = cv2.imwrite('/Users/gohyuhan/Documents/test/google_earth_image/label122-1.png', output)
        print(status)
    except:
        print("fail to save")


start('/Users/gohyuhan/Documents/test/google_earth_image/label122.png')
