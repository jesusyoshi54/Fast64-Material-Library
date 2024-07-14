import bpy

def render():
    try:
        bpy.ops.render.render(animation=True)
        print("render done")
    except error as e:
        print("oops")
        raise e

render()