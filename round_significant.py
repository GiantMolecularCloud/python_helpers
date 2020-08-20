####################################################################################################
# round to x significant digits
####################################################################################################

def round_significant(x, significant=2):
    """Round to a number of significant digits.

    Parameters
    ----------
    x : int/float
        The number to be rounded.
    significant : int
        Number of significant digits to round to.

    Returns
    -------
    int
        if the number can be expressed as an int
    float
        otherwise

    Note: this does NOT add zeros if the requested significant digits is higher than the given digits.
    """
    import numpy as np
    rounded = np.round(x, significant-int(np.floor(np.log10(np.abs(x))))-1)

    # convert to int if possible
    if rounded > 10**(significant-1):
        rounded = int(rounded)

    return rounded


####################################################################################################
#
####################################################################################################
