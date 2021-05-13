# 当該ディレクトリをパスに追加(import error 対応)
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from swagger_server.__main__ import app
application = app
