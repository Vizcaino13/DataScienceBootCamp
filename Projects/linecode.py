import cv2

def add_line_to_image(input_image_path, output_image_path, start_point, end_point, color, thickness=2):
    # Load the image from the specified path
    img = cv2.imread(input_image_path)

    # Draw a line on the image
    cv2.line(img, start_point, end_point, color, thickness)

    # Save the modified image
    cv2.imwrite(output_image_path, img)

if __name__ == '__main__':
    input_image_path = '/Users/ashleyvizcaino/Desktop/dataforbootcamp/DGZ5ZsTUQAAtfVz.png'  # Replace with your input image file path
    output_image_path = 'line.jpg'  # Replace with your desired output image file path
    start_point = (50, 50)  # Start point of the line (x1, y1)
    end_point = (150, 150)  # End point of the line (x2, y2)
    color = (0, 0, 255)  # BGR color (in this case, red)
    thickness = 2  # Line thickness (optional)

    add_line_to_image(input_image_path, output_image_path, start_point, end_point, color, thickness)

def add_text_to_image(input_image_path, output_image_path, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 0, 255), thickness=2):
    # Load the image from the specified path
    img = cv2.imread(input_image_path)

    # Add text to the image
    cv2.putText(img, text, position, font, font_scale, color, thickness)

    # Save the modified image
    cv2.imwrite(output_image_path, img)

if __name__ == '__main__':
    input_image_path = '/Users/ashleyvizcaino/Desktop/dataforbootcamp/DGZ5ZsTUQAAtfVz.png'  # Replace with your input image file path
    output_image_path = 'text.jpg'  # Replace with your desired output image file path
    text = 'I am sonic'  # The text you want to add
    position = (50, 100)  # Position of the text (x, y)
    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
    font_scale = 1  # Font scale
    color = (0, 0, 255)  # BGR color (in this case, red)
    thickness = 2  # Text thickness (optional)

    add_text_to_image(input_image_path, output_image_path, text, position, font, font_scale, color, thickness)
