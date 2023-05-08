#!/usr/bin/python3
"""Generates a .tgz archive from the contents of web_static using fabric"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static"""
    try:
        dt = datetime.now()
        filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                                 dt.month,
                                                                 dt.day,
                                                                 dt.hour,
                                                                 dt.minute,
                                                                 dt.second)
        if not os.path.isdir("./versions"):
            local('mkdir versions')

        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None
