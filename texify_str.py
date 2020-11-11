####################################################################################################
# convert string to LaTeX
####################################################################################################

def texify_str(s):
    """Escape a string to not crash LaTeX

    Parameters
    ----------
    s : str
        String to escape for use in LaTeX

    Returns
    -------
    str
        Formatted string to be used in LaTeX.

    """

    # the following replacements will get added to whenever needed
    tex_str = s.replace('_',' ')

    return tex_str


####################################################################################################
#
####################################################################################################
