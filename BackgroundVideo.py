import os
import sys

import pygame
import vlc


def callback(self, player):
    print('FPS =', player.get_fps())
    print('time =', player.get_time(), '(ms)')
    print('FRAME =', .001 * player.get_time() * player.get_fps())




    # Enable in Windows to use directx renderer instead of windib
    # os.environ["SDL_VIDEODRIVER"] = "directx"
def run(window, path='Sprites\BackgroundCity.mp4'):
    print("Using %s renderer" % pygame.display.get_driver())
    if not os.access(path, os.R_OK):
        print('Error: %s file not readable' % movie)
        sys.exit(1)

    vlcInstance = vlc.Instance()
    media = vlcInstance.media_new(path)

    player = vlcInstance.media_player_new()

    em = player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerTimeChanged, \
                    callback, player)
    # window = pygame.display.get_wm_info()['window']
    # window = pygame.display.get_wm_info()['window']
    if sys.platform == "linux2":  # for Linux using the X Server
        player.set_xwindow(window)
    elif sys.platform == "win32":  # for Windows
        player.set_hwnd(window)
    elif sys.platform == "darwin":  # for MacOS
        player.set_agl(window)

    # Load movie into vlc player instance
    player.set_media(media)

    # Quit pygame mixer to allow vlc full access to audio device (REINIT AFTER MOVIE PLAYBACK IS FINISHED!)
    pygame.mixer.quit()

    # Start movie playback
    player.play()

    # while player.get_state() != vlc.State.Ended:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit(2)
    #         if event.type == pygame.KEYDOWN:
    #             print("OMG keydown!")
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             print("we got a mouse button down!")
    
