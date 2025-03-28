import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

edges = (
    (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
    (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
)

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    rotate_x, rotate_y = 0, 0
    rotation_speed = 3
    mouse_sensitivity = 0.2
    mouse_control = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotate_y = -rotation_speed
                elif event.key == pygame.K_RIGHT:
                    rotate_y = rotation_speed
                elif event.key == pygame.K_UP:
                    rotate_x = -rotation_speed
                elif event.key == pygame.K_DOWN:
                    rotate_x = rotation_speed
                elif event.key == pygame.K_s:
                    mouse_control = not mouse_control  # Toggle mouse control mode
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    rotate_y = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    rotate_x = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_control = True  # Enable mouse control when clicking the cube
            elif event.type == pygame.MOUSEMOTION and mouse_control:
                dx, dy = event.rel
                rotate_x += dy * mouse_sensitivity
                rotate_y += dx * mouse_sensitivity
        
        if not mouse_control:
            glRotatef(rotate_x, 1, 0, 0)
            glRotatef(rotate_y, 0, 1, 0)
        else:
            glRotatef(rotate_x, 1, 0, 0)
            glRotatef(rotate_y, 0, 1, 0)
            rotate_x, rotate_y = 0, 0  # Reset rotation after applying

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
