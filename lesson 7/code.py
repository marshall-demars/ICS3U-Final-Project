#!/usr/bin/env python3

# Created by: Marshall Demars and Cameron Diedrich
# Created on: Jan 2023
# This program is the "David Dash" program on the PyBadge


#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: November 2022
# This program is the "Space Aliens" program on the PyBadge

import constants
import stage
import ugame


def menu_scene():
    # This function is the main game game_scene

    image_bank_background = stage.Bank.from_bmp16("ball.bmp")

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
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # create a stage for the background to show up on
    #  and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = text + [background]

    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene():
    # This function is the main game game_scene

    image_bank_background = stage.Bank.from_bmp16("ball.bmp")
    image_bank_sprites2 = stage.Bank.from_bmp16("space_aliens.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("ball.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # set the background to image 0 in the image bank
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # a sprite that will be updated every frame
    ball = stage.Sprite(
        image_bank_sprites, 2, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    squid = stage.Sprite(
        image_bank_sprites2,
        8,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # create a stage for the background to show up on
    #  and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = [ball] + [squid] + [background]

    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ball.x <= (constants.SCREEN_X - constants.SPRITE_SIZE):
                ball.move((ball.x + constants.SPRITE_MOVEMENT_SPEED), ball.y)
            else:
                ball.move((constants.SCREEN_X - constants.SPRITE_SIZE), ball.y)

        if keys & ugame.K_LEFT != 0:
            if ball.x >= 0:
                ball.move((ball.x - constants.SPRITE_MOVEMENT_SPEED), ball.y)
            else:
                ball.move(0, ball.y)
        if keys & ugame.K_UP:
            ball.move(ball.x, ball.y - 1)
        if keys & ugame.K_DOWN:
            ball.move(ball.x, ball.y + 1)

        game.render_sprites([ball] + [squid])
        game.tick()


if __name__ == "__main__":
    menu_scene()
