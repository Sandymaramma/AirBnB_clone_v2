#!/usr/bin/python3
"""Deploy an archive of static html to my web servers with Fabric3"""

from fabric.api import put, run, env, sudo 
# from fabric.contrib import files
from os.path import exists
env.hosts = ['54.146.56.165', '54.157.168.145']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
env.password = None

run("rm -rf /data/web_static/releases/web_static_202305184049/images")
run("rm -rf /data/web_static/releases/web_static_202305184049/styles")

def do_deploy(archive_path):
    """Function to transfer `archive_path` to web servers.
    Args:
        archive_path (str): path of the .tgz file to transfer
    Returns: True on success, False otherwise.
    """
    if exists(archive_path) is False:
        return False
    try:
        archive_name = archive_path.split("/")[-1]
        no_ext = archive_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/" + no_ext
	
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(path_no_ext))
        sudo("tar -xzf /tmp/{} -C {}/".format(archive_name, path_no_ext))
        sudo("rm /tmp/{}".format(archive_name))
        sudo("mv {}/web_static/* {}/".format(path_no_ext, path_no_ext))
        sudo("rm -rf {}/web_static".format(path_no_ext))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/ /data/web_static/current".format(path_no_ext))
        sudo("chmod -R 755 {}".format(path_no_ext))
        
        print('New version deployed!')
        return True
    except FileNotFoundError:
        return False
