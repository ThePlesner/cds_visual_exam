import os
import cv2
import csv
import argparse

#Generates a histogram for an image (read by cv2.imread) and normalizes it using minmax
def generate_histogram(image, normalize_function = cv2.NORM_MINMAX):
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    normalized_hist = cv2.normalize(hist, hist, 0, 255, normalize_function)
    return normalized_hist

#Checks if a file from a given path has the right extension and whether its the target image or not. 
def validate_image(file_path, target_path):
    filename = os.path.split(file_path)[1].lower()
    target_name = os.path.split(target_path)[1].lower()

    #Valid extentions to ensure its an image. More formats could be added.
    valid_extensions = ['.jpg', '.jpeg', '.png']
    file_extension = os.path.splitext(filename)[1]
    extension_is_valid = file_extension in valid_extensions

    #To avoid comparing the target image with itself, its left out. 
    return filename != target_name and extension_is_valid

def main(target_image_path, data_dir_path, output_path, comparison_function = cv2.HISTCMP_CHISQR):
    #opens the csv file straight away to only do it once 
    with open(output_path, 'w') as output:
        #using csv-writer to contruct the csv as we go
        csv_writer = csv.writer(output)
        
        #csv-header
        csv_writer.writerow(['image_name', 'chi_distance'])

        #Reading the target image file and create a histogram straight away
        target_image = cv2.imread(target_image_path)
        target_histogram = generate_histogram(target_image)

        #Create a list filtering away non image-files using list-comprehension and the validate-image function
        valid_images = [image_path for image_path in os.listdir(data_dir_path) if validate_image(image_path, target_image_path)]

        #Initiize a dictionary for the closest image
        most_similar_image = {
            'name': '',
            'chi_distance': float('inf')
        }

        #Run through the valid images, generate a histogram for each and compare it to the target histogram
        for image_name in valid_images:
            image_path = os.path.join(data_dir_path, image_name)
            image = cv2.imread(image_path)
            image_histogram = generate_histogram(image)
            chi_distance = cv2.compareHist(target_histogram, image_histogram, comparison_function)

            csv_writer.writerow([image_name, chi_distance])

            #Update the dictionary if the comparison image is more similar than the previous most similar 
            if chi_distance < most_similar_image['chi_distance']:
                most_similar_image['name'] = image_name
                most_similar_image['chi_distance'] = chi_distance

        print(f"The most similar image to {os.path.split(target_image_path)[1]} is the {most_similar_image['name']} with a score of {most_similar_image['chi_distance']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare histograms generated on a collection of images to find a target image based on said histograms.')
    parser.add_argument('--target_image_path', default='./data/jpg/image_0001.jpg', help='path to the image that should be compared to the rest of the collection')
    parser.add_argument('--data_dir_path', default='./data/jpg', help='path to the collection of images that the target should be compared with')
    parser.add_argument('--output_path', default='./output/output.csv', help='the path to the directory the output should be placed in')
    args = parser.parse_args()

    main(args.target_image_path, args.data_dir_path, args.output_path)



