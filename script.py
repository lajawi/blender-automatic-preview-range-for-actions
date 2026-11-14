bl_info = {
    "name": "Auto Action Frame-range",
    "blender": (4, 2, 0),
    "category": "Animation"
}

import bpy
from math import floor, ceil

prev_action = None
def Make_sure_this_has_a_very_unique_name_depsgraph_update_pre(scene, depsgraph):
    global prev_action
    action = bpy.context.active_object.animation_data.action

    if action == prev_action: # if the action hasn't changed, we skip.
        return
    
    if action.use_frame_range:
        start = action.frame_start
        end = action.frame_end
    else:
        start = action.curve_frame_range[0]
        end = action.curve_frame_range[1]

    scene.frame_preview_start = floor(start)
    scene.frame_preview_end = ceil(end)

    prev_action = action

def remove_handler_by_name(handlers, to_remove):
    for h in handlers:
        if h.__name__ ==  to_remove:
            handlers.remove(h)

def clean_handlers():
    remove_handler_by_name(bpy.app.handlers.depsgraph_update_pre, Make_sure_this_has_a_very_unique_name_depsgraph_update_pre.__name__)

def unregister():
    clean_handlers()

def register():
    bpy.app.handlers.depsgraph_update_pre.append(Make_sure_this_has_a_very_unique_name_depsgraph_update_pre)

if __name__ == "__main__":
    clean_handlers()
    register()
