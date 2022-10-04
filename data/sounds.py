from os import path
import pygame as pg


sounds_folder = path.join(path.dirname(__file__), 'resources', 'sounds')

#Load sounds of cards movements
touch = pg.mixer.Sound(path.join(sounds_folder, 'touch.ogg')) # FIXME: find free ogg file

# Load music theme
music_game_theme = path.join(sounds_folder, 'game_theme.wav') # FIXME: find free wav file
