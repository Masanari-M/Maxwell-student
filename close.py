# -*- coding: cp932 -*-
# -*- coding: cp932 -*-
from ansys.aedt.core import Maxwell3d

# Maxwell3D�ɐڑ��i���ɊJ���Ă�����̂ɐڑ��j
m3d = Maxwell3d(non_graphical=False, new_desktop=False)

# �f�X�N�g�b�v�����i�S�v���W�F�N�g�ۑ�����Ă��Ȃ��ꍇ�͖��ۑ��ŏI���j
m3d.release_desktop()
