import bpy
import re

context = bpy.context
scene = context.scene

#vector_font = list(bpy.data.fonts)[1]
font_location='C:\\Windows\\Fonts\\calibril.ttf'

all_fonts = list(bpy.data.collections['Fonts'].children)


def print_sth(nr=3):
    obj = get_objects_and_path(nr)[0]
    for i in range(len(obj)):
        print(obj[i])
        obj[i].hide_viewport = True

def get_objects_and_path(nr):
    if nr==0 : 
        objects = list(bpy.data.collections["MainObject"].objects)
        path="E:/Blender/FONT/Alfabeth/"
    if nr==1 : 
        objects = list(bpy.data.collections["SpecialObject"].objects)
        path="E:/Blender/FONT/Special_Objects/"
    if nr==2 : 
        objects = list(bpy.data.collections["PL_Objects"].objects)
        path="E:/Blender/FONT/PL_Alfabeth/"
    if nr==3 : 
        objects = list(bpy.data.collections["ESP_Objects"].objects)
        path="E:/Blender/FONT/ESP_Alfabeth/"
    if nr==4 : 
        objects = list(bpy.data.collections["DE_Objects"].objects)
        path="E:/Blender/FONT/DE_Alfabeth/"
    if nr==5 : 
        objects = list(bpy.data.collections["DK_Objects"].objects)
        path="E:/Blender/FONT/DK_Alfabeth/"
    if nr==6 : 
        objects = list(bpy.data.collections["SE_Objects"].objects)
        path="E:/Blender/FONT/SE_Alfabeth/"
    if nr==7 : 
        objects = list(bpy.data.collections["FI_Objects"].objects)
        path="E:/Blender/FONT/FI_Alfabeth/"
    if nr==8 : 
        objects = list(bpy.data.collections["EE_Objects"].objects)
        path="E:/Blender/FONT/EE_Alfabeth/"
    if nr==9 : 
        objects = list(bpy.data.collections["LV_Objects"].objects)
        path="E:/Blender/FONT/LV_Alfabeth/"
    if nr==10 : 
        objects = list(bpy.data.collections["LT_Objects"].objects)
        path="E:/Blender/FONT/LT_Alfabeth/"
    if nr==11 : 
        objects = list(bpy.data.collections["CZ_Objects"].objects)
        path="E:/Blender/FONT/CZ_Alfabeth/"
    if nr==12 : 
        objects = list(bpy.data.collections["SK_Objects"].objects)
        path="E:/Blender/FONT/SK_Alfabeth/"
    if nr==13 : 
        objects = list(bpy.data.collections["FR_Objects"].objects)
        path="E:/Blender/FONT/FR_Alfabeth/"
    if nr==14 : 
        objects = list(bpy.data.collections["PT_Objects"].objects)
        path="E:/Blender/FONT/PT_Alfabeth/"
    if nr==15 : 
        objects = list(bpy.data.collections["SL_Objects"].objects)
        path="E:/Blender/FONT/SL_Alfabeth/"
    if nr==16 : 
        objects = list(bpy.data.collections["HU_Objects"].objects)
        path="E:/Blender/FONT/HU_Alfabeth/"
    if nr==17 : 
        objects = list(bpy.data.collections["HR_Objects"].objects)
        path="E:/Blender/FONT/HR_Alfabeth/"
    if nr==18 : 
        objects = list(bpy.data.collections["RO_Objects"].objects)
        path="E:/Blender/FONT/RO_Alfabeth/"
    if nr==19 : 
        objects = list(bpy.data.collections["TR_Objects"].objects)
        path="E:/Blender/FONT/TR_Alfabeth/"




    return [objects,path]




def render_objects(group,path):
    hide_obj_from_viewport(group)
    for obj in group:
        obj.hide_render = False
        file_name = obj.name
        new_path = path+file_name +".jpg"
        bpy.data.scenes[0].render.filepath = new_path
        bpy.ops.render.render(write_still = True)
        obj.hide_render = True
 

def change_letters_into_mesh(nr):
    all_fonts[nr].hide_viewport = False
    group=get_objects_and_path(nr)[0]
    for obj in group:
        print("start meshing:")
        print(obj)
        obj.select_set(True)    
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.convert(target="MESH")
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        #x_dir = 0.003
        #y_dir = 0.006
        #z_dir = 0.006
        x_dir = 0.08
        y_dir = 0.04
        z_dir = 0.04
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(x_dir, y_dir, z_dir), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.object.editmode_toggle()
        obj.select_set(False) 
        print("done")
        print("--------------------")    
    all_fonts[nr].hide_viewport = True


def hide_obj_from_viewport(group):
    for obj in group:
          obj.hide_viewport = True
          obj.hide_render = True
                   

def unhide_obj_from_viewport(group):
    for obj in group:
          obj.hide_viewport = False
          obj.hide_render = False 

def change_font(group):
    #fnt=bpy.data.fonts.load(font_location)
    for obj in group:
        #obj.data.font = fnt
        obj.data.font = vector_font

def change_scale(group):
    for obj in group:
        obj.scale[0]=1
        obj.scale[1]=1.15
        obj.scale[2]=1
bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

def change_sth():
#    for obj in group:
#        obj.select_set(True)
#        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
#        obj.select_set(False)
    for i in range(3):
        print(i)

def render_all():
    nr_of_fonts=len(list(bpy.data.collections['Fonts'].children))
    for i in range(nr_of_fonts):
        if i >=10:
            render_specific_col(i)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
        #name=all_fonts[i].name
        
#       if name=="MainObject" or name=="SpecialObject" or name=="PL_Objects":
#            print("do some staff")
#            change_letters_into_mesh(i)
#            print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
#            render_specific_col(i)
#        else:
#            print("do nothing just render")
#            render_specific_col(i)

def render_specific_col(nr):
    all_fonts[nr].hide_render = False 
    objects=get_objects_and_path(nr)[0]
    path=get_objects_and_path(nr)[1]
    render_objects(objects,path)
    all_fonts[nr].hide_render = True
            


switch = 1
sub_swich = 0


if __name__ == "__main__":
    if switch == 0:
        print("XDDDDDDDDDDDDDDDDDDDDDDDDDD")
        render_specific_col(sub_swich)
    if switch ==1:
        print("OLABOGAAAAAAAAAAAAA")
        render_all()
    


    if switch == 100:
        hide_obj_from_viewport(get_objects_and_path(sub_swich)[0])
    if switch == 101:
        unhide_obj_from_viewport(get_objects_and_path(sub_swich)[0])
    if switch == 102:
        change_font(get_objects_and_path(sub_swich)[0])
    if switch == 103:
        change_letters_into_mesh(sub_swich)
    if switch == 104:
        change_scale()
    if switch == 105:
        change_sth()
    if switch == 106:
        print_sth(sub_swich)
        
        
#special_objects
#engl_letters
#pl_letters
#esp_letters
