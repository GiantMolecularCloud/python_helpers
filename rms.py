####################################################################################################
# root-mean-square
####################################################################################################

def rms(array, axis=0):
    """Simple root-mean-square calculation.

    Parameters
    ----------
    array : np.ndarray
        Some array to calculate the rms over.
    axis : int
        Array axis to calculate the rms over. The default axis=0 is set to return the rms map of a
        3D input array.
        Default: 0

    Returns
    -------
    type
        Description of returned object.

    """
    from numpy import nanmean, sqrt, square
    return sqrt(nanmean(square(array), axis=axis))


####################################################################################################
#
####################################################################################################
