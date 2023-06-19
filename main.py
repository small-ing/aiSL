import hand_tracking_module as htm
import cv2
import mediapipe as mp
import random
#Leo am exist
cap = cv2.VideoCapture(0)
tracker = htm.handTracker()

def letter_parser():
    letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return letter
# brandon was here
#Austin is here
#Aloha from William
while True:
    try:
        success, image = cap.read()
    except:
        print("Camera not found")
        break
    image = tracker.hands_finder(image)
    lmList = tracker.position_finder(image)
    tracker.update_letter()
    tracker.letter_display(image)
    #if len(lmList) != 0:
        #print(lmList[4])

    cv2.imshow("Video",image)
    if cv2.waitKey(1) != -1:
        break

cv2.destroyAllWindows()
 
