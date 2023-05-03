from dat.clear_dat import clear_data
import pytesseract as pt
import cv2
from dat.strings import *
from dat.embeds import error_embed
import os
import numpy as np

# Constants
LOWER_GREEN = (40, 75, 75)
UPPER_GREEN = (70, 255, 255)
RATIO_THRESH = 0.02
RATIO_SIZE = (0.40, 0.1)

pt.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Check if image is a Pithka's screenshot or not based on ratio
def validate(path):
    image = cv2.imread(path)
    height, width, _ = image.shape
    print(height / width)
    if abs((height / width) - RATIO_SIZE[0]) <= RATIO_SIZE[1]:
        return True     
    return False

# Image processing and clear list construction
def im_proc(path):
    image = cv2.imread(path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Based on HSV script in testing folder
    lower = np.array([0, 0, 170])
    upper = np.array([160, 160, 255])
    
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))
    dilate = cv2.dilate(mask, kernel, iterations=5)
    #thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 5)

    result = 255 - cv2.bitwise_and(dilate, mask)
    boxes = pt.image_to_boxes(result, lang='eng',config='--psm 6 --oem 3')

    # Create a list of word boxes: (char, x-coord, y-coord)
    word_boxes = []
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        char = b[0]

        word_boxes.append((char, x, y))

    #print(word_boxes)

    # Looking for the 'H' in 'Hel Ra Citadel' and check that next letter is 'e' to avoid confusion with other H's sometimes recognized
    reverse_boxes = list(reversed(word_boxes))
    upper_left = None
    lower_right = None    
    for i, char in enumerate(word_boxes):
        if ord(char[0]) == 72 and ord(word_boxes[i + 1][0]) == 101:
            upper_left = (char[1], char[2] + 25)
            break    

    # Looking for the 'W' in 'WATERMARKS'
    for i, char in enumerate(reverse_boxes):
        if ord(char[0]) == 87 and ord(reverse_boxes[i -1][0]) == 65:
            lower_right = (char[1], char[2] - 15)
            break
            
    # Crops from top to bottom (even though coords are bottom to top) and left to right
    cropped_img = image[(image.shape[0] - upper_left[1]):(image.shape[0] - lower_right[1]), upper_left[0]:lower_right[0]]            

    # Preprocessing for check mark detection
    hsv = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)
    mask_green = cv2.inRange(hsv, LOWER_GREEN, UPPER_GREEN)
    result_green = cv2.bitwise_and(cropped_img, cropped_img, mask=mask_green)
    contours_green, hierarchy_green = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a green rectangle around each contour in the original image and save the location
    cont_coords = []
    num_clears = 0
    for i, contour in enumerate(contours_green):
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(cropped_img, (x, y), (x+w, y+h), (0, 255 , 0), -1)    
        cv2.circle(cropped_img, (x + (w // 2), y + (h // 2)), 3, (0, 0, 255), -1)
        
        cont_coords.append((x, y, w, h))
        num_clears += 1
            
    #print(cont_coords)

    cont_coords = sorted(cont_coords, key=lambda x: x[0])
    clears = []
    for cont in cont_coords:
        #print(f'x ratio: {(cont[0] + (w // 2)) / cropped_img.shape[1]}, y ratio: {(cont[1] + (w // 2)) / cropped_img.shape[0]}')
        #print((cont[0] + (w // 2)) / cropped_img.shape[1] + (cont[1] + (w // 2)) / cropped_img.shape[0])
        
        x_rat = (cont[0] + (w // 2)) / cropped_img.shape[1]
        y_rat = (cont[1] + (w // 2)) / cropped_img.shape[0]

        # Where clear[1] is the x ratio and clear[2] is the y ratio defined in clears_dat.py
        for i, clear in enumerate(clear_data):
            if abs(x_rat - clear[1]) <= RATIO_THRESH and abs(y_rat - clear[2]) <= RATIO_THRESH:
                clears.append(clear[0])
                
    cv2.imwrite('./temp/result.png', cropped_img)                
    return clears

async def process(attachments, channel):
    paths = []
    clears = []
    if attachments:
        for i, file in enumerate(attachments):
            if file.url[-3:] == 'jpg' or file.url[-3:] == 'peg' or file.url[-3:] == 'png':                
                path = f'./temp/image{i}.jpg'
                paths.append(path)
                await file.save(path)
                
                if validate(path):
                    clears = im_proc(path)
                    delete(paths)                        
                    break 
                else:
                    await channel.send(embed=error_embed(ERROR_INVALID_IMAGE))                                           
            else:
                await channel.send(embed=error_embed(ERROR_BAD_TYPE))
    else:
        await channel.send(embed=error_embed(ERROR_NO_IMAGE)) 
            
    return clears

def delete(paths):
    for path in paths:
        os.remove(path)  
    return