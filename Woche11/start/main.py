from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import glm
import numpy as np
from cg_helper import *

window = create_window("Das ist ein Testfenster")

glClearColor(0.5, 0.5, 0.5, 0)

# load shader programs
vertex_shader_source_cube = read_shader_source('cube.vertex')
fragment_shader_source_cube = read_shader_source('cube.fragment')

shader_program_cube = create_shader_program(vertex_shader_source_cube, fragment_shader_source_cube)

# Define cube vertices and indices
vertices = np.array([
    -0.5, -0.5, -0.5,
     0.5, -0.5, -0.5,
     0.5,  0.5, -0.5,
    -0.5,  0.5, -0.5,
    -0.5, -0.5,  0.5,
     0.5, -0.5,  0.5,
     0.5,  0.5,  0.5,
    -0.5,  0.5,  0.5
], dtype=np.float32)

indices = np.array([
    0, 1, 2, 2, 3, 0,  # Back face
    4, 5, 6, 6, 7, 4,  # Front face
    0, 1, 5, 5, 4, 0,  # Bottom face
    2, 3, 7, 7, 6, 2,  # Top face
    0, 3, 7, 7, 4, 0,  # Left face
    1, 2, 6, 6, 5, 1   # Right face
], dtype=np.uint32)

# VAO for cube
vao_cube = glGenVertexArrays(1)
glBindVertexArray(vao_cube)

# VBO for positions
vertex_buffer_cube = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_cube)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

# VBO for indices
face_buffer_cube = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, face_buffer_cube)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

#connection to vertex shader (in-attributes)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertices.itemsize, ctypes.c_void_p(0))
glEnableVertexAttribArray(0)

camera_position = glm.vec3(10,10,10)
view_matrix = glm.lookAt(camera_position, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0)) # camera position, camera target, up vector
projection_matrix = glm.perspective(glm.radians(60.0), 800.0/800.0, 0.1, 100.0) # FoV, Aspect Ratio, Near Clipping Plane, Far Clipping Plane

def key_callback(window, key, scancode, action, mods):
    global view_matrix, camera_position
    if key == glfw.KEY_I and action == glfw.PRESS:
        camera_position = camera_position*0.9
    if key == glfw.KEY_O and action == glfw.PRESS:
        camera_position = camera_position * 1.1

    view_matrix = glm.lookAt(camera_position, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))  # camera position, camera target, up vector

glfw.set_key_callback(window, key_callback)

while (glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and not glfw.window_should_close(window)):
    #clear buffer first
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #general approach to draw an object: activate shader, bind VAO, call draw
    glUseProgram(shader_program_cube)

    view_loc = glGetUniformLocation(shader_program_cube, 'view_matrix')
    projection_loc = glGetUniformLocation(shader_program_cube, 'projection_matrix')

    glUniformMatrix4fv(view_loc, 1, GL_FALSE, glm.value_ptr(view_matrix))
    glUniformMatrix4fv(projection_loc, 1, GL_FALSE, glm.value_ptr(projection_matrix))

    glBindVertexArray(vao_cube)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()

