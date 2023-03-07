import cv2
vline_pos = 320
hline_pos = 240
def update_line_pos(x):
    global vline_pos, hline_pos
    vline_pos = cv2.getTrackbarPos('X', 'Adjust Line Position')
    hline_pos = cv2.getTrackbarPos('Y', 'Adjust Line Position')
cv2.namedWindow('Adjust Line Position')
cv2.createTrackbar('X', 'Adjust Line Position', vline_pos, 640, update_line_pos)
cv2.createTrackbar('Y', 'Adjust Line Position', hline_pos, 480, update_line_pos)
Frame = cv2.VideoCapture(0)
while True:
    ret, frame = Frame.read()
    cv2.putText(frame, 'MBS3523 Assignment 1 – Q3 Name: YEUNG YAT', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(125, 0, 125), 2)
    # Draw vertical and horizontal lines at current positions
    cv2.line(frame, (vline_pos, 0), (vline_pos, 480), (255, 255, 255), 2)
    cv2.line(frame, (0, hline_pos), (640, hline_pos), (255, 255, 255), 2)
    cv2.imshow('Adjust Line Position', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close all windows
Frame.release()
cv2.destroyAllWindows()