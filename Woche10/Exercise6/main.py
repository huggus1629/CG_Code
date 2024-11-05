import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from cg_helper import *

window = create_window("Das ist ein Testfenster")

glClearColor(1.0, 0.7, 0.5, 0)

# load shader programs
vertex_shader_source_triangle = read_shader_source('triangle.vertex')
fragment_shader_source_triangle = read_shader_source('triangle.fragment')

shader_program_triangle = create_shader_program(vertex_shader_source_triangle, fragment_shader_source_triangle)



# VAO and VBO for triangle
vao_triangle = glGenVertexArrays(1)
glBindVertexArray(vao_triangle)

vertex_data_triangle = [-1, -1, 0,
                        1, -0.5, 0,
                        0.8, 0.5, 0,
                        0,  1, 0]

vertex_buffer_triangle = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_triangle)

array_type = (GLfloat * len(vertex_data_triangle))
glBufferData(GL_ARRAY_BUFFER,
             len(vertex_data_triangle) * ctypes.sizeof(ctypes.c_float),
             array_type(*vertex_data_triangle),
             GL_STATIC_DRAW)

#connection to vertex shader (in-attributes)
attr_id = 0
glVertexAttribPointer(
    attr_id,            # attribute 0.
    3,                  # components per vertex attribute
    GL_FLOAT,           # type
    False,              # to be normalized?
    0,                  # stride
    None                # array buffer offset
)
glEnableVertexAttribArray(attr_id)



color_data_triangle = [1.0, 1.0, 1.0,
                        0.0, 0.0, 1.0,
                        0.0, 1.0, 0.0,
                        1.0,  0.0, 0.0]

color_buffer_triangle = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, color_buffer_triangle)

array_type = (GLfloat * len(color_data_triangle))
glBufferData(GL_ARRAY_BUFFER,
             len(color_data_triangle) * ctypes.sizeof(ctypes.c_float),
             array_type(*color_data_triangle),
             GL_STATIC_DRAW)

#connection to vertex shader (in-attributes)
attr_id = 1
glVertexAttribPointer(
    attr_id,            # attribute 1.
    3,                  # components per vertex attribute
    GL_FLOAT,           # type
    False,              # to be normalized?
    0,                  # stride
    None                # array buffer offset
)
glEnableVertexAttribArray(attr_id)





# VAO and VBO for triangle 2
vao_triangle_2 = glGenVertexArrays(1)
glBindVertexArray(vao_triangle_2)

vertex_data_triangle_2 = [-0.8, 0.5, 0,
                        0, -0.5, 0,
                        0.8, 0.1, 0,
                        0.2,  0.8, 0]

vertex_buffer_triangle_2 = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_triangle_2)

array_type = (GLfloat * len(vertex_data_triangle_2))
glBufferData(GL_ARRAY_BUFFER,
             len(vertex_data_triangle_2) * ctypes.sizeof(ctypes.c_float),
             array_type(*vertex_data_triangle_2),
             GL_STATIC_DRAW)

#connection to vertex shader (in-attributes)
attr_id = 0
glVertexAttribPointer(
    attr_id,            # attribute 0.
    3,                  # components per vertex attribute
    GL_FLOAT,           # type
    False,              # to be normalized?
    0,                  # stride
    None                # array buffer offset
)
glEnableVertexAttribArray(attr_id)



color_data_triangle_2 = [0.0, 0.0, 0.0,
                        1.0, 0.0, 1.0,
                        1.0, 1.0, 0.0,
                        1.0,  0.0, 1.0]

color_buffer_triangle_2 = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, color_buffer_triangle_2)

array_type = (GLfloat * len(color_data_triangle_2))
glBufferData(GL_ARRAY_BUFFER,
             len(color_data_triangle_2) * ctypes.sizeof(ctypes.c_float),
             array_type(*color_data_triangle_2),
             GL_STATIC_DRAW)

#connection to vertex shader (in-attributes)
attr_id = 1
glVertexAttribPointer(
    attr_id,            # attribute 1.
    3,                  # components per vertex attribute
    GL_FLOAT,           # type
    False,              # to be normalized?
    0,                  # stride
    None                # array buffer offset
)
glEnableVertexAttribArray(attr_id)



show_second_shape = True


def key_callback(window, key, scancode, action, mods):
    global show_second_shape
    if key == glfw.KEY_S and action == glfw.PRESS:
        show_second_shape = not show_second_shape

glfw.set_key_callback(window, key_callback)


while (glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and not glfw.window_should_close(window)):
    #clear buffer first
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #general approach to draw an object: activate shader, bind VAO, call draw
    glUseProgram(shader_program_triangle)
    glBindVertexArray(vao_triangle)
    glDrawArrays(GL_TRIANGLE_FAN, 0, 4)

    if show_second_shape:
        glUseProgram(shader_program_triangle) #we could also write separate shaders - one per shape
        glBindVertexArray(vao_triangle_2)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()

