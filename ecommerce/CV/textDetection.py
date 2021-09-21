import cv2
import pytesseract
import store.models as store_model
# from store import models as store_model



img = cv2.imread('CV/static/images/IMG_1159.jpg')

# Image from BGR2RGB

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))


# #Detecting Characters
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)

# for b in boxes.splitlines():
#     # print(b)
#     b = b.split(' ')
#     print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),3)
#     cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


#Detecting words
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            # cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
            # cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
            detected_text = (b[11])
            # print(detected_text)
            product_list = [store_model.Product.name]
            print(product_list)




# cv2.imshow('Result',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)


# # get grayscale image

# def get_grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# # noise removal
# def remove_noise(image):
#     return cv2.medianBlur(image, 5)


# # thresholding

# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# img = get_grayscale(img)
# img = thresholding(img)
# img = remove_noise(img)


# def ocr_core(img):
#     # text = pytesseract.image_to_string(img)
#     text = pytesseract.image_to_string(img)
#     return text
    
# print(ocr_core(img))
