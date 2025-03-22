import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Window size
WIDTH, HEIGHT = 800, 600

# Track whether the sphere is being controlled
sphere_controlled = False

def draw_sphere():
    """Draws a 3D sphere in black and white using OpenGL."""
    quad = gluNewQuadric()
    gluQuadricTexture(quad, GL_TRUE)
    glColor3f(1, 1, 1)  # Set the sphere color to white (black & white mode)
    gluSphere(quad, 1, 32, 32)
    gluDeleteQuadric(quad)

def main():
    global sphere_controlled

    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    gluPerspective(45, WIDTH / HEIGHT, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Detect mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sphere_controlled = True  # Activate movement on click
            
            elif event.type == pygame.MOUSEBUTTONUP:
                sphere_controlled = False  # Stop movement when the mouse is released

        # If the sphere is controlled, update its position
        if sphere_controlled:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            x_pos = (mouse_x / WIDTH) * 4 - 2  # Convert to OpenGL coordinates
            y_pos = -(mouse_y / HEIGHT) * 3 + 1.5  # Invert Y-axis and scale

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            gluPerspective(45, WIDTH / HEIGHT, 0.1, 50.0)
            glTranslatef(x_pos, y_pos, -5)  # Move sphere based on mouse position
            draw_sphere()
            pygame.display.flip()

        pygame.time.wait(10)  # Small delay for smooth animation

    pygame.quit()

main()
