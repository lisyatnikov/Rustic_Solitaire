from os import path
import pygame as pg
from PIL import Image

graphics_folder = path.join(path.dirname(__file__), 'resources', 'graphics')

#Load atlases of sprites
backgrond = pg.image.load(path.join(graphics_folder, 'background.jpg'))
