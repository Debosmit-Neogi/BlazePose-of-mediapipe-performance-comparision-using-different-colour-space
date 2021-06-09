
import cv2
import mediapipe as mp
import time

Draw_object = mp.solutions.drawing_utils
pose_object = mp.solutions.pose
pose = pose_object.Pose()

cap = cv2.VideoCapture('/home/debosmit2001/Downloads/yoga.mp4')
prev_Time = 0
while True:
    success, img = cap.read()
    # openCv reads img in BGR but mediapipe neads RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        Draw_object.draw_landmarks(img, results.pose_landmarks, pose_object.POSE_CONNECTIONS)
        # Draw_object.draw_landmarks(img, results.pose_landmarks)

        for id, lm in enumerate(results.pose_landmarks.landmark): #landmark points given in mediapipe (id,landmark)
            h, w, c = img.shape #height,width,channel
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    current_Time = time.time()
    fps = 1 / (current_Time - prev_Time)
    prev_Time = current_Time  #after calculating fps, increment prev time to cuurent time

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
