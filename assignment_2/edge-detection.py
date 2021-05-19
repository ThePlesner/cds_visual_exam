import os
import cv2

# creates a copy of an image, adds a rectangle with the given coordinates and returns the copy
def add_rectangle(image, coordinates):
    memorial_copy = image.copy()
    cv2.rectangle(
        memorial_copy, 
        (coordinates['x1'], coordinates['y1']), 
        (coordinates['x2'], coordinates['y2']), 
        (0, 255, 0), 3)

    return memorial_copy

def main():
    data_path = 'data'
    output_path = 'output'

    # load the image
    memorial_image_path = os.path.join(data_path, 'memorial.jpg')
    memorial_image = cv2.imread(memorial_image_path)

    # Rectangle coordinates. These are entirely founds by trial and error with different numbers
    coordinates = {
        'x1': 1380,
        'y1': 850,
        'x2': 2880,
        'y2': 2800
    }

    # create image with region of interest and save it in the output folder
    memorial_ROI = add_rectangle(memorial_image, coordinates)
    cv2.imwrite(os.path.join(output_path, 'image_with_ROI.jpg'), memorial_ROI)

    # crop image with the region of interest as coordinates and save it in the output folder
    memorial_cropped = memorial_image[coordinates['y1']:coordinates['y2'], coordinates['x1']:coordinates['x2']]
    cv2.imwrite(os.path.join(output_path, 'image_cropped.jpg'), memorial_cropped)

    # blur the image to smooth out noice and irregular pixels
    memorial_blurred = cv2.bilateralFilter(memorial_cropped, 8, 180, 200)

    # use the canny edge detector algorithm to find edges in the image
    memorial_canny = cv2.Canny(memorial_blurred, 50, 100)

    # use the edges found to find contours of the figures in the image (hopefully letters)
    contours, _ = cv2.findContours(memorial_canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw the contours on to a copy of the image and save it in the output folder
    memorial_letters = cv2.drawContours(memorial_cropped.copy(), contours, -1, (0, 255, 0), 1)
    cv2.imwrite(os.path.join(output_path, 'image_letters.jpg'), memorial_letters)


if __name__ == '__main__':
    main()