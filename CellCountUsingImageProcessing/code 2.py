from copy import copy
import cv2
import numpy as np



# Helper function
def nothing(*arg):
    pass

#
# Commandline options
#
from optparse import OptionParser
parser = OptionParser()
parser.set_description("Counts cells in an image using the Contour binary thresholding.")
parser.add_option("-i", "--image", dest="imageFileName", action="store", metavar="FILE", help="input image")
parser.add_option("-g", "--gui", dest="gui", action="store_true", default=False, help="display gui")

(options, args) = parser.parse_args()
display_gui = options.gui is not None

#
# Script behavior
#
process_name = "Theshold"
threshold_trackbar_name = "adjust_thrs"

image = cv2.imread("2.jpg",cv2.CV_LOAD_IMAGE_GRAYSCALE)

mask = np.zeros(image.shape, np.uint8)

#
# Binary Thresholding
#
cv2.namedWindow(process_name)
cv2.imshow(process_name, mask)
cv2.createTrackbar(threshold_trackbar_name, process_name, 0, 220, nothing)

template = cv2.imread("3.jpg", 0)
template_result = cv2.matchTemplate(image, template, cv2.TM_SQDIFF_NORMED)
matched_image = np.array(template_result * -500, dtype=np.uint8)

# Gui loop
while True:
    # Threshold the template mask result based on user input
    threshold = cv2.getTrackbarPos(threshold_trackbar_name, process_name)
    ret, mask = cv2.threshold(matched_image, threshold, 25, cv2.THRESH_BINARY_INV)

    # Find contours of the threshold
    contours, ret = cv2.findContours(copy(mask), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        contour += 20    # offset the template match which returns the match quality at the corner, not center (opencv is shitty)

    # Draw the center of each contour onto the image
    image_copy = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image_copy, contours, -2, (0, 0, 0), 3)
# noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 2)
# Finding unknown region    
    sbg = cv2.dilate(opening,kernel,iterations=3)
    sfg=np.uint8(mask)
    u=cv2.subtract(sbg,sfg)
    
    
        # Display the image
    cv2.imshow(process_name, image_copy)

    # Only show one step of this loop if there's no gui
    if not display_gui:
        break
    else:
        print len(contours)
        
        

    # Exit on user pressing escape key
    key = cv2.waitKey(5)
    if key == 27: #escape key
        break
    elif key == ord('s'):#press s to save
        cv2.imwrite('ms.png',image_copy)
        

cv2.destroyAllWindows()
