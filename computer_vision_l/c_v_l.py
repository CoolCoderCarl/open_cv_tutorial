import numpy as np
import cv2 as cv

###
### That func is highlight the corners on the picture
###
def corner_detector(filename):
    ### Create container with readed image
    img = cv.imread(filename)
    ### Always make original image gray
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    dst = cv.cornerHarris(gray, 2, 3, 0.04)
    dst = cv.dilate(dst, None)

    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv.imshow('Corner detector', img)

    ### Wait for any key
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()

###
### That func is make pic lighter
###
def gray_light(filename):
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ### Add light to pixels
    gray_add = cv.add(gray, 200)
    ### Multiply light to pixels
    gray_mul = cv.multiply(gray, 1.8)

    cv.imshow('Original gray', img)
    cv.imshow('Add light', gray_add)
    cv.imshow('Multuply light', gray_mul)

    ### Wait for any key
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()

###
### This func is simmilar Harris Corner Detection, but good for large pic
###
def sift(filename):
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    sift = cv.SIFT_create()
    kp = sift.detect(gray, None)
    grayimg = cv.drawKeypoints(gray, kp, img)
    # cv.imwrite('house_sift.jpg', img)
    cv.imshow('SIFT', grayimg)

    ### Wait for any key
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()
