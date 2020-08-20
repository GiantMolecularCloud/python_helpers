####################################################################################################
# LaTeX float formatting
####################################################################################################

def latex_float(f, fmt='{:.1e}', phantom=False):
    """Convert float to LaTex number with exponent.

    Parameters
    ----------
    f : float,int,double
    fmt : str
        Python format string. Default: '{:.1e}'
    phantom : bool
        Add phantom zeros to pad the number if it does not fill the format string.
        Default: False

    Returns
    -------
    str
        Formatted string to be used in LaTeX.

    """
    float_str = fmt.format(f)
    if phantom:
        float_str = float_str.replace(' ',r'\phantom{0}')
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str


####################################################################################################
#
####################################################################################################
