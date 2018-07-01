import tarfile
from os import getcwd
from os.path import normpath
from os.path import join as path_join
from pathlib import Path


def extract_tar(tar_filename, directory=getcwd()):
    with tarfile.open(tar_filename, 'r') as tar:
        for tar_file in tar.getmembers():
            # This check normalize the path for any directory traversal
            # then uses Path's parent attribute to check if the target
            # directory is a parent of the resulting path
            target_dir = Path(directory)
            target_file = Path(normpath(path_join(directory, tar_file.name)))
            if target_dir not in target_file.parents:
                continue

            # Same as above but for the symlink target
            if tar_file.issym() or tar_file.islnk():
                symlink_file = Path(normpath(
                    path_join(directory, tar_file.linkname)
                ))
                if target_dir not in symlink_file.parents:
                    continue

            tar.extract(tar_file, path=directory)


if __name__ == "__main__":
    extract_tar('testing.tar')
