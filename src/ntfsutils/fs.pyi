from typing import Tuple

class FILETIME:
    dwLowDateTime: int
    dwHighDateTime: int

class BY_HANDLE_FILE_INFORMATION:
    dwFileAttributes: int
    ftCreationTime: FILETIME
    ftLastAccessTime: FILETIME
    ftLastWriteTime: FILETIME
    dwVolumeSerialNumber: int
    nFileSizeHigh: int
    nFileSizeLow: int
    nNumberOfLinks: int
    nFileIndexHigh: int
    nFileIndexLow: int

def getdirinfo(path: str) -> BY_HANDLE_FILE_INFORMATION:
    """
    Return information for the directory at the given path. This is going to be a
    struct of type BY_HANDLE_FILE_INFORMATION.
    """

def getfileinfo(path: str) -> BY_HANDLE_FILE_INFORMATION:
    """
    Return information for the file at the given path. This is going to be a
    struct of type BY_HANDLE_FILE_INFORMATION.
    """

def getvolumeinfo(path: str) -> Tuple[str, int]:
    """
    Return information for the volume containing the given path. This is going
    to be a pair containing (file system, file system flags).
    """

def hardlinks_supported(path: str) -> bool: ...
def junctions_supported(path: str) -> bool: ...
