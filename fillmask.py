import numpy as np
import os
import cv2
from PIL import Image


def fillMask(label):
    urban_land = (0, 255, 255)
    argriculture_land = (255, 255, 0)
    range_land = (255, 0, 255)
    forest_land = (0, 255, 0)
    water = (0, 0, 255)
    barren_land = (255, 255, 255)
    unknown = (0, 0, 0)

    '''
     show all rgb value that need to be replace
    '''
    print(label[np.any(np.logical_and(np.logical_and(label != unknown, label <= (254, 254, 254)), np.logical_and(
        np.logical_and(np.logical_and(label != urban_land, label != argriculture_land), np.logical_and(label != forest_land, label != water)), np.logical_and(label != range_land, label != barren_land))), axis=-1)])
    '''
     replace all pixel that is not equal to the rgb value stated to a certain rgb value,
    '''
    label[np.any(np.logical_and(np.logical_and(label != unknown, label <= (254, 254, 254)), np.logical_and(
        np.logical_and(np.logical_and(label != urban_land, label != argriculture_land), np.logical_and(label != forest_land, label != water)), np.logical_and(label != range_land, label != barren_land))), axis=-1)] = urban_land
    '''
    to check if their are any pixel which doesn't have an cetain rgb value that represent a class stated above
    will return [] if all pixel in the image have an cetain rgb value that represent a class stated above
    '''
    print(label[np.any(np.logical_and(np.logical_and(label != unknown, label <= (254, 254, 254)), np.logical_and(
        np.logical_and(np.logical_and(label != urban_land, label != argriculture_land), np.logical_and(label != forest_land, label != water)), np.logical_and(label != range_land, label != barren_land))), axis=-1)])

    return label


def start(input):
    print(input)
    im = cv2.imread(input)
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    output = fillMask(im)
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

    try:
        print("saving...")
        status = cv2.imwrite(
            '/Users/gohyuhan/Documents/test/google_earth_image/label125-1.png', output)

    except:
        print("fail to save")


start('/Users/gohyuhan/Documents/test/google_earth_image/label125-1.png')

