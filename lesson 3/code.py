#!/usr/bin/env python3

# Created by: Marshall Demars and Cameron Diedrich
# Created on: Jan 2023
# This program is the "David Dash" program on the PyBadge


import stage
import ugame


def game_scene():
   # this function is the main game game_scene

   # image banks for CircuitPython
   image_bank_background = stage.Bank.from_bmp16("ball.bmp")
   image_bank_sprites = stage.Bank.from_bmp16("ball.bmp")

   # set the background to image 0 in the image bank
   #    and the size (10x8 tiles of size 16x16)
   background = stage.Grid(image_bank_background, 10, 8)

   # a sprite that will be updated every frame
   ball = stage.Sprite(image_bank_sprites, 2, 75, 66)

   # create a stage for the background to show up on
   #    and set the frame rate to 60fps
   game = stage.Stage(ugame.display, 60)

   # set the layers of all sprites, items show up in order
   game.layers = [ball] + [background]

   # render all sprites
   #    most likely you will only render the background once per game scene
   game.render_block()

   # repeat forever, game loop
   while True:
       # get user input

       # update game logic

       # redraw Sprite
       game.render_sprites([ball])
       game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
   game_scene()
