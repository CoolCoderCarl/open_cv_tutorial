import numpy as np
import cv2 as cv
### U CAN PUT HERE EVERY PICTURE U WANT
filename = 'house.jpg'

###
### THAT FUNC IS HIGHLIGHT THE CORNER ON PICTURE
###
def corner_detector():
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
def gray_light():
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


if __name__ == '__main__':
    # gray_light()
    corner_detector()
