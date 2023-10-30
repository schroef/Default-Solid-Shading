
bl_info = {
	"name": "Default Solid Shading",
	"description": "Restores scene shading type to solid upon opening files",
	"location": "3dView > Shading Type > Solid Shading PopOver",
	"author": "Rombout Versluijs",
	"version": (0, 0, 1),
	"blender": (2, 80, 0),
	"wiki_url": "https://github.com/schroef/default-solid-shading",
	"tracker_url": "https://github.com/schroef/default-solid-shading/issues",
	"category": "Viewport"
}

import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler(context, a):
	""" Set the 3dviewport to solid shading type if not set """
	
	prefs = bpy.context.preferences.addons['Default-Solid-Shading'].preferences
	if prefs.default_solid_shading:
		for i, area in enumerate(bpy.context.screen.areas):
			if area.type == 'VIEW_3D':
				if (area.spaces[0].shading.type != 'SOLID'):
					area.spaces[0].shading.type  = 'SOLID'

class DSS_PT_AddonPreferences(bpy.types.AddonPreferences):
	""" Preference Settings Addin Panel"""
	bl_idname = __name__

	default_solid_shading: bpy.props.BoolProperty(
        name="Default to Solid Shading",
        default=False,
		description="Default to Solid Shading after opening file")

def default_solid_shading(self, context):
	layout = self.layout
	prefs = bpy.context.preferences.addons['Default-Solid-Shading'].preferences
	col = layout.column()
	col.prop(prefs, "default_solid_shading")

classes = [
	DSS_PT_AddonPreferences
]

def register():
	for cls in classes:
		bpy.utils.register_class(cls)

	bpy.app.handlers.load_post.append(load_handler)
	bpy.types.VIEW3D_PT_shading_options.append(default_solid_shading)

def unregister():
	bpy.app.handlers.load_post.remove(load_handler)
	bpy.types.VIEW3D_PT_shading_options.remove(default_solid_shading)
	for cls in classes:
		bpy.utils.unregister_class(cls)

if __name__ == "__main__":
	register()
