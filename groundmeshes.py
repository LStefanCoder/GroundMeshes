import bpy

bl_info = {
    "name": "GroundMeshes",
    "author": "LStefan",
    "version": (1, 0),
    "blender": (3, 6, 5),
    "location": "View3D > Add Menu",
    "description": "Enables the user to add mesh primitives whose origin is at the bottom of the mesh.",
    "category": "Add Mesh"
}

#https://blender.stackexchange.com/questions/152525/appending-a-sub-menu-under-an-existing-sub-menu-in-blender-2-8/152566#152566
#adding the menu
class Primitives_BottomMenu(bpy.types.Menu):
    bl_label = "Origin at the base"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("newmeshes.cube_operator", icon="MESH_CUBE")

        row = layout.row()
        row.operator("newmeshes.cylinder32_operator", icon="MESH_CYLINDER")

        row = layout.row()
        row.operator("newmeshes.cylinder64_operator", icon="MESH_CYLINDER")

        row = layout.row()
        row.operator("newmeshes.cylinder128_operator", icon="MESH_CYLINDER")

        row = layout.row()
        row.operator("newmeshes.cone32_operator", icon="MESH_CONE")

        row = layout.row()
        row.operator("newmeshes.cone64_operator", icon="MESH_CONE")

        row = layout.row()
        row.operator("newmeshes.cone128_operator", icon="MESH_CONE")

class AddBottomCubeOperator(bpy.types.Operator):
    """Add a cube with origin at the bottom"""
    bl_idname = "newmeshes.cube_operator"
    bl_label = "Cube"

    def execute(self, context):
        #checking whether the user is in edit mode, otherwise returning a warning popup
        #the first clause is needed for the case that there is no object selected
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
    
            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            #adding a warning popup - see: https://blender.stackexchange.com/questions/96715/how-to-script-add-on-info-and-warnings
            self.report({'ERROR'}, 'You have to be in object mode')

class AddBottomCylinder32Operator(bpy.types.Operator):
    """Add a cylinder with origin at the bottom"""
    bl_idname = "newmeshes.cylinder32_operator"
    bl_label = "Cylinder 32"

    def execute(self, context):
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
    
            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddBottomCylinder64Operator(bpy.types.Operator):
    """Add a cylinder with origin at the bottom"""
    bl_idname = "newmeshes.cylinder64_operator"
    bl_label = "Cylinder 64"

    def execute(self, context):
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
    
            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddBottomCylinder128Operator(bpy.types.Operator):
    """Add a cylinder with origin at the bottom"""
    bl_idname = "newmeshes.cylinder128_operator"
    bl_label = "Cylinder 128"

    def execute(self, context):
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cylinder_add(vertices=128, radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
    
            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddBottomCone32Operator(bpy.types.Operator):
    """Add a cone with origin at the bottom"""
    bl_idname = "newmeshes.cone32_operator"
    bl_label = "Cone 32"

    def execute(self, context):
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cone_add(vertices=32, radius1=1, radius2=0.1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)

            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddBottomCone64Operator(bpy.types.Operator):
    """Add a cone with origin at the bottom"""
    bl_idname = "newmeshes.cone64_operator"
    bl_label = "Cone 64"

    def execute(self, context):
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cone_add(vertices=64, radius1=1, radius2=0.1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)

            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

class AddBottomCone128Operator(bpy.types.Operator):
    """Add a cone with origin at the bottom"""
    bl_idname = "newmeshes.cone128_operator"
    bl_label = "Cone 128"

    def execute(self, context):
        if(bpy.context.active_object is None or bpy.context.active_object.mode == 'OBJECT'):
            bpy.ops.mesh.primitive_cone_add(vertices=128, radius1=1, radius2=0.1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

            bpy.ops.object.editmode_toggle()
    
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)

            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, 'You have to be in object mode')

#also see here
#https://blender.stackexchange.com/questions/152525/appending-a-sub-menu-under-an-existing-sub-menu-in-blender-2-8/152566#152566
def draw_menu(self, context):
    self.layout.menu(Primitives_BottomMenu.bl_idname)

def register():
    bpy.utils.register_class(Primitives_BottomMenu)
    bpy.utils.register_class(AddBottomCubeOperator)
    bpy.utils.register_class(AddBottomCylinder32Operator)
    bpy.utils.register_class(AddBottomCylinder64Operator)
    bpy.utils.register_class(AddBottomCylinder128Operator)
    bpy.utils.register_class(AddBottomCone32Operator)
    bpy.utils.register_class(AddBottomCone64Operator)
    bpy.utils.register_class(AddBottomCone128Operator)
    bpy.types.VIEW3D_MT_mesh_add.append(draw_menu)

def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(draw_menu)
    bpy.utils.unregister_class(AddBottomCubeOperator)
    bpy.utils.unregister_class(AddBottomCylinder32Operator)
    bpy.utils.unregister_class(AddBottomCylinder64Operator)
    bpy.utils.unregister_class(AddBottomCylinder128Operator)
    bpy.utils.unregister_class(AddBottomCone32Operator)
    bpy.utils.unregister_class(AddBottomCone64Operator)
    bpy.utils.unregister_class(AddBottomCone128Operator)
    bpy.utils.unregister_class(Primitives_BottomMenu)

if __name__ == "__main__":
    register()