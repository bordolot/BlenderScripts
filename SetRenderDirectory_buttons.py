import bpy
import re


#object = list(bpy.data.objects)[0] #Lenoland #Bloin #Thog


switch = 4
path_base = "E:\\Godot\\02_PROJEKTY_TRENINGOWE\\41_17.09.2021_WOiRDo\\03_assets\\cats\\"



def test():   
    for collection in bpy.data.collections["Buttons"].children:
        
        bpy.data.collections[collection.name].hide_render = False
        path = path_base + give_name(collection.name)
        bpy.data.scenes[0].render.filepath = path
        bpy.ops.render.render(write_still = True, animation=False)
        bpy.data.collections[collection.name].hide_render = True



def render_all():
    path=""
    bpy.context.scene.camera = bpy.data.objects.get("Camera.001")
    for collection in bpy.data.collections["MainObject"].children:
        original_y_location = collection.all_objects[0].location.y
        change_light_intensity(collection.name)
        take_objects_from_collection_in_front_of_camera(collection)
        path = path_base + give_name(collection.name)
        bpy.data.scenes[0].render.filepath = path
        bpy.ops.render.render(write_still = True, animation=False)
        take_object_back_to_original_place(collection,original_y_location)


def render_specific_object(collection_name=""):
    path=""
    bpy.context.scene.camera = bpy.data.objects.get("Camera.001")
    for collection in bpy.data.collections["MainObject"].children:
        if collection.name==collection_name:
            original_y_location = collection.all_objects[0].location.y
            change_light_intensity(collection.name)
            take_objects_from_collection_in_front_of_camera(collection)
            path = path_base + give_name(collection.name)
            bpy.data.scenes[0].render.filepath = path
            bpy.ops.render.render(write_still = True, animation=False)
            take_object_back_to_original_place(collection,original_y_location) 


def move_objects_of_collection(collection,vector):
    for object in collection.all_objects:
        object.location.y=vector



def change_light_intensity(collentions_name):
    if collentions_name == "Delete_drum_snake":
        bpy.data.objects["Light.002"].data.energy = 1
    else:
        bpy.data.objects["Light.002"].data.energy = 10
         
        
def give_name(collentions_name):
    name=""
    camera=""
    if collentions_name == "Paste_word":
        name="Paste_word"
    if collentions_name == "Challange":
        name="Challange"
    if collentions_name == "Memory":
        name="Memory"
    camera=bpy.data.objects.get(name)
    bpy.context.scene.camera=camera
    return name


def make_sure_collection_is_visible(collection):
    bpy.data.collections[collection].hide_viewport = True
           
        
def take_objects_from_collection_in_front_of_camera(collection):
    original_y_location = collection.all_objects[0].location.y
    for object in collection.all_objects:
        object.location.y=0

def take_object_back_to_original_place(collection,original_loc):
    for object in collection.all_objects:
        object.location.y=original_loc

def take_collection_in_front_of_camera(collentions_name):
    for collection in bpy.data.collections:
        if collection.name == collention_name:
            original_y_location = collection.all_objects[0].location.y
            for object in collection.all_objects:
                object.location.y=0

def take_collection_back_to_original_place(collentions_name):
    for collection in bpy.data.collections:
        if collection.name == collention_name:
            for object in collection.all_objects:
                object.location.y=original_y_location



if __name__ == "__main__":
    if switch==1:
        render_all()
    if switch==2:
        render_specific_object("Back")
    if switch==3:
        move_objects_of_collection(bpy.data.collections["MainObject"].children["Speed"],40)
    if switch==4:
        test()




