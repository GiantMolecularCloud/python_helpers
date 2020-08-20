###################################################################################################
# escape filenames
###################################################################################################

def escape_filename(str):
    """Escape the most often used characters in a string to be used as a file name.

    Parameters
    ----------
    str : str
        Input string to be escaped.

    Returns
    -------
    str
        String with escaped '(', ')'; replaced ' ' by '_' and removed '$'.
        
    """
    str = str.replace('(',r'\(')
    str = str.replace(')',r'\)')
    str = str.replace(' ',r'_')
    str = str.replace('$','')
    return str


###################################################################################################
#
###################################################################################################
