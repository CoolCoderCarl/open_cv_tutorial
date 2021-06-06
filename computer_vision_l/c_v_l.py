import numpy as np
import cv2 as cv

###
### THAT FUNC IS HIGHLIGHT THE CORNER ON PICTURE
###
def corner_detector(filename):
    ### CREATE CONTAINER WITH READED IMAGE
    img = cv.imread(filename)
    ### ALWAYS MAKE ORIGINAL IMAGE GRAY
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    dst = cv.cornerHarris(gray, 2, 3, 0.04)
    dst = cv.dilate(dst, None)

    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv.imshow('Corner detector', img)

    ### WAIT FOR ANY KEY
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()

###
### THAT FUNC IS MAKE PIC LIGHTER
###
def gray_light(filename):
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ### ADD LIGHT TO PIXELS
    gray_add = cv.add(gray, 200)
    ### MULTIPLY LIGHT TO PIXELS
    gray_mul = cv.multiply(gray, 1.8)

    cv.imshow('Original gray', img)
    cv.imshow('Add light', gray_add)
    cv.imshow('Multuply light', gray_mul)

    ### WAIT FOR ANY KEY
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


def sift(filename):
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    sift = cv.SIFT_create()
    kp = sift.detect(gray, None)
    grayimg = cv.drawKeypoints(gray, kp, img)
    # cv.imwrite('house_sift.jpg', img)
    cv.imshow('SIFT', grayimg)

    ### WAIT FOR ANY KEY
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


###
### ANOTHER CORNER FOUNDER METHOD
###
def fast(filename):
    img = cv.imread(filename, 0)
    ### Initiate FAST object with default values
    fast = cv.FastFeatureDetector_create()
    ### find and draw the keypoints
    kp = fast.detect(img, None)
    img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
    # Print all default params
    print("Threshold: {}".format(fast.getThreshold()))
    print("nonmaxSuppression:{}".format(fast.getNonmaxSuppression()))
    print("neighborhood: {}".format(fast.getType()))
    print("Total Keypoints with nonmaxSuppression: {}".format(len(kp)))
    # cv.imwrite('fast_true.png', img2)
    cv.imshow('FAST_TRUEh', img2)
    # Disable nonmax Suppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img, None)

    print("Total Keypoints without nonmaxSuppression: {}".format(len(kp)))
    img3 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
    # cv.imwrite('fast_false.png', img3)
    cv.imshow('FAST_FALSE', img3)

    ### WAIT FOR ANY KEY
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()