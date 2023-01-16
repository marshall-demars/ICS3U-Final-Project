#!/usr/bin/env python3

# Created by: Marshall Demars and Cameron Diedrich
# Created on: Jan 2023
# This program is the "David Dash" program on the PyBadge


import stage
import ugame


def game_scene():
   # this function is the main game game_scene

   # image banks for CircuitPython
   image_bank_background = stage.Bank.from_bmp16("water,jpg")

   # create a stage for the background to show up on
   #    and set the frame rate to 60fps
   game = stage.Stage(ugame.display, 60)
   # set the layers of all sprites, items show up in order
   game.layers = [background]
   # render all sprites
   #    most likely you will only render the background once per game scene
   game.render_block()

   # repeat forever, game loop
   while True:
       pass  # just a placeholder for now


if __name__ == "__main__":
   game_scene()
