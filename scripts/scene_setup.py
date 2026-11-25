import bpy

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Add a basic studio lighting setup and camera
bpy.ops.object.light_add(type='AREA', location=(4, -4, 5))
light = bpy.context.active_object
light.data.energy = 500

bpy.ops.object.camera_add(location=(0, -6, 2), rotation=(1.3, 0, 0))
bpy.context.scene.camera = bpy.context.active_object

print("Studio scene setup complete.")
