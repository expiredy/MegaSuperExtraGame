import os
import sys

import pygame
import cv2


def callback(self, player):
    print('FPS =', player.get_fps())
    print('time =', player.get_time(), '(ms)')
    print('FRAME =', .001 * player.get_time() * player.get_fps())




    # Enable in Windows to use directx renderer instead of windib
    # os.environ["SDL_VIDEODRIVER"] = "directx"
def run(path=os.path.join('Sprites', 'BackgroundCity.mp4')):
    video = cv2.VideoCapture(path)
    if (video.isOpened()== False):
        print("Error opening video stream or file")
        raise Exception
    return video