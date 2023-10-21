import cv2
import numpy as np

def add_circle_to_image(input_image_path, output_image_path, center, radius, color, thickness=2):
    # Load the image from the specified path
    img = cv2.imread(input_image_path)

    # Draw a circle on the image
    cv2.circle(img, center, radius, color, thickness)

    # Save the modified image
    cv2.imwrite(output_image_path, img)

if __name__ == '__main__':
    input_image_path = '/Users/ashleyvizcaino/Desktop/dataforbootcamp/DGZ5ZsTUQAAtfVz.png'  # Replace with your input image file path
    output_image_path = 'output.jpg'  # Replace with your desired output image file path
    center = (100, 100)  # Center of the circle (x, y)
    radius = 30  # Radius of the circle
    color = (0, 0, 255)  # BGR color (in this case, red)

    add_circle_to_image(input_image_path, output_image_path, center, radius, color)

def add_rec_to_image(input_image_path2, output_image_path2, start_point, end_point, color, thickness=3):
    # Load the image from the specified path
    img2 = cv2.imread(input_image_path2)

    # Draw a circle on the image
    cv2.rectangle(img2, start_point, end_point, color, thickness)

    # Save the modified image
    cv2.imwrite(output_image_path2, img2)

if __name__ == '__main__':
    input_image_path2 = '/Users/ashleyvizcaino/Desktop/dataforbootcamp/DGZ5ZsTUQAAtfVz.png'  # Replace with your input image file path
    output_image_path2 = 'rect.jpg'  # Replace with your desired output image file path
    start_point = (5, 5)  # Center of the circle (x, y)
    end_point = (220, 220) # Radius of the circle
    color = (255, 0, 0)   # BGR color (in this case, red)

    add_rec_to_image(input_image_path2, output_image_path2, start_point, end_point, color)