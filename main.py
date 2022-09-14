from math import ceil
import cv2
import numpy
import sys

def main():
    file = sys.argv[1]
    img = cv2.imread(sys.argv[1], 3)
    ascii = 'Ñ@#W$9876543210?!abc;:+=-,._ '
    ascii_len = len(ascii)
    orig_h = img.shape[0]
    orig_w = img.shape[1]
    H = 50
    W = (orig_w//orig_h)*H
    img = cv2.resize(img, (W, H), interpolation= cv2.INTER_LINEAR)
    mul = 16
    blank = numpy.zeros((H*mul, W*mul, 3), dtype='uint8')
    for i in range(0 , H):
        for j in range(0, W):
            pixel = img[i][j]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            bright = ceil((r+g+b)/3)
            ind = int((bright/255) * (ascii_len-1))
            c = ascii[ind]
            cv2.putText(blank, c, (j*mul, i*mul), cv2.FONT_HERSHEY_DUPLEX, 0.3, (int(r), int(g), int(b)), 1) 
    
    cv2.imshow("ascii art", blank)
    cv2.waitKey(0)

main()
