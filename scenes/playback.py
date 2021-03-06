import os
import sys
import pygame as pg

sys.path.insert(1,os.getcwd())

from utility.mathematics.matrix import Matrix
from template.scene import scene
from simulation.camera import camera
from playback.player import player
from utility.io.load import load
from playback.player import player


"""
Playback program window
"""

class playback(scene):
    def __init__(self):
        super().__init__()
        self.cam = camera()
        self.loaded = False

    def load(self):
        self.data = load()
        self.loaded = True
        self.player = player(self.data.particles)


    def run(self,event,screen,data):
        screen.fill([30,60,30])
        self.cam.update(screen,event)
        if self.loaded:
            self.player.next(screen,self.cam,True)

        return(super().run(event,screen,data))
