#!/usr/bin/env python3

# Created by: Marshall Demars and Cameron Diedrich
# Created on: Jan 2023
# This program is the "David Dash" program on the PyBadge


import random
import time

import constants
import stage
import supervisor
import ugame


def splash_scene():
    # this function is the splash scene game loop

    # an image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render background
    game.render_block()

    while True:
        time.sleep(1.0)
        menu_scene()


def menu_scene():
    # This function is the main game game_scene

    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # set the background to image 0 in the image bank
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage for the background to show up on
    #  and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = text + [background]

    game.render_block()

    # repeat forever, game loop
    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene():
    # This function is the main game game_scene

    # for score
    squid_count = 0
    score = 0

    score_text = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    def show_squid():
        # this function takes an alien from off screen and moves it on screen
        for squid_number in range(len(squids)):
            if squids[squid_number].x < 0:
                squids[squid_number].move(
                    random.randint(
                        8,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    image_bank_background = stage.Bank.from_bmp16("ball.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("ball.bmp")
    image_bank_sprites2 = stage.Bank.from_bmp16("space_aliens.bmp")

    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    ball = stage.Sprite(
        image_bank_sprites, 2, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    squid = stage.Sprite(
        image_bank_sprites2,
        8,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # create list of lasers for when we shoot
    squids = []
    for squid_number in range(constants.TOTAL_NUMBER_OF_SQUIDS):
        a_single_squid = stage.Sprite(
            image_bank_sprites2, 8, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        squids.append(a_single_squids)
    # place 1 alien on the screen
    show_squid()

    game = stage.Stage(ugame.display, 60)
    game.layers = [score_text] + [ball] + squids + [background]
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_RIGHT:
            if ball.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                ball.move((ball.x + constants.SPRITE_MOVEMENT_SPEED), ball.y)
            else:
                ball.move((constants.SCREEN_X - constants.SPRITE_SIZE), ball.y)

        if keys & ugame.K_LEFT:
            if ball.x >= 0:
                ball.move((ball.x - constants.SPRITE_MOVEMENT_SPEED), ball.y)
            else:
                ball.move(0, ball.y)

        if keys & ugame.K_UP:
            if ball.y >= (constants.OFF_TOP_SCREEN):
                ball.move(ball.x, (ball.y - constants.SPRITE_MOVEMENT_SPEED))
            else:
                ball.move(ball.x, 0)

        if keys & ugame.K_DOWN:
            if ball.y <= (constants.SCREEN_Y - constants.SPRITE_SIZE):
                ball.move(ball.x, (ball.y + constants.SPRITE_MOVEMENT_SPEED))
            else:
                ball.move(ball.x, (constants.SCREEN_Y - constants.SPRITE_SIZE))

            # each frame move the aliens down, that are on the screen
        for squid_number in range(len(squids)):
            if squids[squid_number].x > 0:
                squids[squid_number].move(
                    squids[squid_number].x,
                    squids[squid_number].y + constants.SQUID_SPEED,
                )
                if squids[squid_number].y > constants.SCREEN_Y:
                    squids[squid_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    show_squid()
                    show_squid()
                    show_squid()
                    score = score + 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        for squid_number in range(len(squids)):
            if squids[squid_number].x > 0:
                if stage.collide(
                    squids[squid_number].x + 1,
                    squids[squid_number].y,
                    squids[squid_number].x + 15,
                    squids[squid_number].y + 15,
                    ball.x,
                    ball.y,
                    ball.x + 15,
                    ball.y + 15,
                ):
                    time.sleep(3.0)
                    game_over_scene(score)
        # redraw sprite list
        game.render_sprites([ball] + squids)
        game.tick()


if __name__ == "__main__":
    splash_scene()
