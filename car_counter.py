#!/usr/bin/env python
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os.path


def count_cars():
    names = get_correct_file_names()
    for name in names:
        im = cv2.imread(name)
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        print('Number of cars in the image [' + name + '] is ' + str(label.count('car')))
        plt.imshow(output_image)
        plt.show()
        plt.imsave(name.replace('.', '_counted.'), output_image)


def get_correct_file_names():
    input_names = input("Enter picture file names space separated\n")
    names = input_names.split()
    files = []
    for name in names:
        if os.path.exists(name):
            files.append(name)
        else:
            print("File [" + name + "] not found")
    return files


if __name__ == '__main__':
    count_cars()
