from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
#add_box(edges, 400, 400, 0, 200, 200, 200)
#add_sphere(edges, 500, 500, 500, 200, .005, .002)
#add_torus(edges, 500, 500, 500, 100, 300, .005, .002)
#draw_lines(edges, screen, DRAW_COLOR)
#save_extension(screen, "pic.png")

parse_file( 'script2', edges, transform, screen, color )
