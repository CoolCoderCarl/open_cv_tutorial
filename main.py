import cv2

def loading_displaying_saving():
    ### ADD UR PIC
    img = cv2.imread('ninja.jpg')


    cv2.imwrite('grayninja.jpg', img)

    print("Высота:" + str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    print("Количество каналов:" + str(img.shape[2]))

    (b, g, r) = img[0, 0]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))

    img[0, 0] = (255, 0, 0)
    (b, g, r) = img[0, 0]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))

    res_img = cv2.resize(img, (300, 300), cv2.INTER_NEAREST)
    cv2.imshow('ninja', res_img)
    cv2.waitKey(0)

loading_displaying_saving()