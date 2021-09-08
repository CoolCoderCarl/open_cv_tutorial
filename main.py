import computer_vision_l.c_v_l as my_cv

### You can put here any picture you want
# filename = 'house.jpg'
filename = 'test.jpg'

if __name__ == '__main__':
    my_cv.corner_detector(filename)
    my_cv.gray_light(filename)
    my_cv.sift(filename)


