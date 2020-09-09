####################################################################################################
# RMS map of a spectral cube
####################################################################################################

def spectralcube_rms(cube, lfchans):
    """Compute RMS map from a SpectralCube.

    Parameters
    ----------
    cube : SpectralCube
        The cube to compute the RMS of.

    lfchans : list, tuple, np.ndarray
        List of line-free channels to compute the RMS over.

    Returns
    -------
    spectral_cube.lower_dimensional_structures.Projection
        2D map of the RMS values.
    """

    from spectral_cube.lower_dimensional_structures import Projection
    from spectral_cube import SpectralCube,wcs_utils
    from spectral_cube.spectral_cube import np2wcs

    if not isinstance(cube, SpectralCube):
        raise TypeError("Cube is not a SpectralCube.")
    if not isinstance(lfchans, (list, tuple, np.ndarray)):
        raise TypeError("lfchans must be a list of channels.")

    # rms noise values
    rms = np.sqrt(np.mean(np.square(cube.filled_data[lfchans]), axis=0))

    # wcs with dropped spectral axis
    new_wcs = wcs_utils.drop_axis(cube._wcs, np2wcs[0])

    # return RMS map as Projection
    return Projection(rms, copy=False, wcs=new_wcs, header=cube._nowcs_header, beam=cube.beam)


####################################################################################################
#
####################################################################################################
