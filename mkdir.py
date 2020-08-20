####################################################################################################
# make directory without fuzz
####################################################################################################

def mkdir(path):
    """mkdir

    Parameters
    ----------
    path : str
        Path to directory to create
    """
    import os
    if ' ' in path:
        raise Exception("Path contains spaces! This will most probably not create the directory you want!")
    if not os.path.exists(path):
        os.system('mkdir -p '+path)
        print("Created "+path)


####################################################################################################
#
####################################################################################################
