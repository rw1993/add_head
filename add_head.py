from snake import *

@when_buffer_is("python")
def add_python_head(ctx):
    b = get_current_buffer()
    contents = get_buffer_contents(b).split()
    if not contents:
        set_buffer_contents(b,"# -*- coding: utf-8 -*-\n# author: rw\n# E-mail: weiyanjie10@gmail.com\n")
        set_cursor_position((4,0))
