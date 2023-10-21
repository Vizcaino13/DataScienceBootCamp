import cv2

def main():
    # Initialize the video capture from the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    # Create a background subtractor
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Apply the background subtractor to the frame
        fg_mask = bg_subtractor.apply(frame)

        # Display the original frame and the foreground mask
        cv2.imshow('Original', frame)
        cv2.imshow('Foreground Mask', fg_mask)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
