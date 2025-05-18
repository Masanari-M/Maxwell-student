# -*- coding: cp932 -*-
import os
from ansys.aedt.core import Maxwell3d

save_dir = r"C:\Users\miyamoto\Documents\Maxwell3D\aedtfile"
os.makedirs(save_dir, exist_ok=True)

m3d = Maxwell3d(non_graphical=False, new_desktop=True)

# Triangle shape (explicitly closed by repeating the first point)
points = [
    [0, 0, 0],
    [10, 0, 0],
    [5, 10, 0],
    [0, 0, 0]  # explicitly close the shape
]

# Record existing objects
before = set(m3d.modeler.object_names)

# Create polyline (NO 'closed' keyword)
poly = m3d.modeler.create_polyline(
    points,
    name="MyShape",
    material="gold",
    segment_type="Line"
)

# Cover lines to create sheet
m3d.modeler.cover_lines(poly.id)

# Get new sheet object
after = set(m3d.modeler.object_names)
sheet_names = list(after - before)
sheets = [name for name in sheet_names if "Sheet" in name]

# Sweep if successful
if sheets:
    sheet = sheets[0]
    m3d.modeler.sweep_along_vector(sheet, [0, 0, 1])
    print("Sweep success:", sheet)
else:
    print("Sheet creation failed.")

# Save project
save_path = os.path.join(save_dir, "triangle_test_final.aedt")
m3d.save_project(save_path)

# m3d.release_desktop()
