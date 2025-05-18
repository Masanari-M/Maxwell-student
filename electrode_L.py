# -*- coding: cp932 -*-
# -*- coding: cp932 -*-
from ansys.aedt.core import Maxwell3d

m3d = Maxwell3d(non_graphical=False, new_desktop=True)

# �p�����[�^
d1, d2, d3, d4, d5, d6, d7 = 1, 1.2, 1.5, 1.0, 0.8, 0.6, 0.4

# �|���S���̒��_���X�g
points = [
    [0, 0],
    [0, 20],
    [2, 20 - d1],
    [4, 20 - d2],
    [6, 20 - d3],
    [8 - d4, 18],
    [8 - d5, 16],
    [8 - d6, 14],
    [8 - d7, 12],
    [20, 12],
    [20, 0],
    [0, 0]  # ���邽�߂ɖ߂�
]

# �|���S�� �� �����o���ŗ��̂�
poly = m3d.modeler.create_polygon(points, name="OptL", material="copper")
m3d.modeler.sweep_along_vector(poly, [0, 0, 1])

# �ۑ��i��΃p�X�Ŏw��j
m3d.save_project(r"C:\Users\miyamoto\Documents\Maxwell3D\cui_student\maxwell_optimization\opt_ljunction.aedt")

m3d.release_desktop()
