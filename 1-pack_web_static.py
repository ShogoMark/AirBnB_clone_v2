#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static folder"""

import os
from datetime import datetime
from fabric.api import local

def do_pack():
"""Creates an archive from the content of a folder"""
    dt = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                             dt.month,
                                                             dt.day,
                                                             dt.hour,
                                                             dt.minute,
                                                             dt.second)
    
    if os.path.isdir("./versions") is False:
        if local('mkdir versions').failed is True:
            return None
    if local("tar -cvf {} web_static".format(filename)).failed is True:
        return None
    return filename
