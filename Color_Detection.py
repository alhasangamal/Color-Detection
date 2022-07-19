# ===============================================
# * Program : Color Detection
# * Author  : Alhasan Gamal
# * Date    : 12 - 07 - 2022
# ===============================================

# * Import Libraries
import argparse
import cv2
import pandas as pd


# * Taking an image from user
sp = argparse.ArgumentParser()
sp.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(sp.parse_args())
img_path = args['image']

clicked =False
r = g = b = xpos = ypos = 0


# * Reading image with opencv
img = cv2.imread(img_path)

# * Reading csv file
data = pd.read_csv('colors.csv', names=[
    "Color", "Color_Name", "HEX", "R", "G", "B"], header=None)

# * Creat function to get Color Name


def get_ColorName(R, G, B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R - int(data.loc[i, 'R'])) + abs(G -
                                                 int(data.loc[i, 'G'])) + abs(B - int(data.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            color_name = data.loc[i, 'Color_Name']
    return color_name

# * Creat function to get x,y


def draw(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw)

# * Display image on the windows

while(1):
    cv2.imshow("Image", img)
    if (clicked):
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = get_ColorName(r, g, b) + " R = " + str(r) + \
            " G = " + str(g) + " B = " + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
