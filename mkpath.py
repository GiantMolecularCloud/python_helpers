####################################################################################################
# create path without fuzz
####################################################################################################

def mkpath(*paths):
    """mkpath

    Parameters
    ----------
    paths : str
        arbitrary number of strings to form the path
    """
    import os
    import .mkdir
    path = join(*paths)
    if ' ' in path:
        raise Exception("Path contains spaces! This will most probably not create the directory you want!")
    if not os.path.exists(path):
        os.system('mkdir -p '+path)
        print("Created "+path)


####################################################################################################
#
####################################################################################################
