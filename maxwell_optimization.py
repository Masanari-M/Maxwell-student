# -*- coding: cp932 -*-
from ansys.aedt.core import Maxwell3d

# version= を省略して自動検出（Student版にも対応しやすい）
m3d = Maxwell3d(non_graphical=False, new_desktop=True)

box = m3d.modeler.create_box([0, 0, 0], [10, 5, 1], name="Electrode", matname="copper")
print("Box created:", box.id)

m3d.save_project("test_project.aedt")
m3d.release_desktop()
