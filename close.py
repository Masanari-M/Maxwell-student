# -*- coding: cp932 -*-
# -*- coding: cp932 -*-
from ansys.aedt.core import Maxwell3d

# Maxwell3Dに接続（既に開いているものに接続）
m3d = Maxwell3d(non_graphical=False, new_desktop=False)

# デスクトップを閉じる（全プロジェクト保存されていない場合は未保存で終了）
m3d.release_desktop()
