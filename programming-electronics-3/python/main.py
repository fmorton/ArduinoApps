from arduino.app_utils import App, Bridge
from arduino.app_bricks.video_objectdetection import VideoObjectDetection

video_detector = VideoObjectDetection(confidence=0.4, debounce_sec=5)

def person_detected():
    print("Person found")

    #Bridge.notify("makeNoise")
    #Bridge.notify("flashLED")

    Bridge.notify("bothThings", 8)

def all_detected(detected: dict):
    print("All detected" + str(detected))

    if('cat' in detected):
        print("Cat found")

    if('cup' in detected):
        print("Cup found")

video_detector.on_detect("person", person_detected)
video_detector.on_detect_all(all_detected)

App.run()

# list of all object types
# airplane
# apple
# backpack
# banana
# baseball bat
# baseball glove
# bear
# bed
# bench
# bicycle
# bird
# boat
# book
# bottle
# bowl
# broccoli
# bus
# cake
# car
# carrot
# cat
# cell phone
# chair
# clock
# couch
# cow
# cup
# dining table
# dog
# donut
# elephant
# fire hydrant
# fork
# frisbee
# giraffe
# hair drier
# handbag
# horse
# hot dog
# keyboard
# kite
# knife
# laptop
# microwave
# motorcycle
# mouse
# orange
# oven
# parking meter
# person
# pizza
# potted plant
# refrigerator
# remote
# sandwich
# scissors
# sheep
# sink
# skateboard
# skis
# snowboard
# spoon
# sports ball
# stop sign
# suitcase
# surfboard
# teddy bear
# tennis racket
# tie
# toaster
# toilet
# toothbrush
# traffic light
# train
# truck
# tv
# umbrella
# vase
# wine glass
# zebra
