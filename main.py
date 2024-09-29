import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

# Initialize camera capture (index 0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Set camera resolution (optional)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# Initialize FaceMeshDetector from cvzone
detector = FaceMeshDetector(maxFaces=1)

# Initialize LivePlot for plotting blink ratio over time
plotY = LivePlot(640, 360, [20, 50], invert=True)

# List of landmarks around the eyes (from FaceMesh points)
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
blinkCounter = 0
counter = 0
color = (255, 0, 255)

while True:
    # Capture frame from the camera
    success, img = cap.read()

    # Check if the frame was successfully captured
    if not success:
        print("Failed to capture image from camera.")
        break

    # Detect face mesh
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]

        # Draw circles around the key landmarks for visualization
        for id in idList:
            cv2.circle(img, face[id], 5, color, cv2.FILLED)

        # Get key points for the left eye (example)
        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]

        # Calculate vertical and horizontal distances between the landmarks
        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

        # Draw lines between the landmarks (optional visualization)
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        # Calculate the blink ratio (vertical length / horizontal length)
        ratio = int((lenghtVer / lenghtHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)

        # Check if the ratio indicates a blink (lower value means eyes closed)
        if ratioAvg < 35 and counter == 0:
            blinkCounter += 1
            color = (0, 200, 0)
            counter = 1

        if counter != 0:
            counter += 1
            if counter > 10:
                counter = 0
                color = (255, 0, 255)

        # Display blink count on the image
        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100), colorR=color)

        # Update the plot with the current blink ratio
        imgPlot = plotY.update(ratioAvg, color)

        # Resize the image and stack it with the plot for side-by-side display
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, imgPlot], 2, 1)
    else:
        # If no face is detected, just resize and stack the same image twice
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, img], 2, 1)

    # Display the stacked image with OpenCV
    cv2.imshow("Eye Blink Counter", imgStack)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
