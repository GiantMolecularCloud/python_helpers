####################################################################################################
# RMS map of a spectral cube
####################################################################################################

def spectralcube_projection(fitsimage, hdu=0):
    """Initialize a SpectralCube Projection instance from a 2D fits image.

    Parameters
    ----------
    fitsimage : str
        Path and file name of the image to load.
    hdu : int
        The HDU to use. Defaults to 0.

    Returns
    -------
    spectral_cube.lower_dimensional_structures.Projection
    """

    from astropy.io import fits
    from astropy.wcs import WCS
    from astropy import units as u
    from spectral_cube.lower_dimensional_structures import Projection

    image = fits.open(fitsimage)[hdu]
    wcs   = WCS(image.header)

    if image.header['naxis'] != 2:
        raise TypeError("Image does not have two axes: naxis="+str(image.header['naxis']))

    bunit = False
    if 'bunit' in image.header:
        if image.header['bunit'] == 'beam-1 Jy':
            bunit = u.Jy/u.beam
        else:
            try:
                bunit = u.Quantity(image.header['bunit'])
            except:
                print("Failed to parse bunit. Specify manually.")

    if bunit:
        data = image.data*bunit
    else:
        data = image.data

    if ('bmaj' in image.header) and ('bmin' in image.header) and ('bpa' in image.header):
        from radio_beam.beam import Beam
        major = image.header['bmaj']*u.degree
        minor = image.header['bmin']*u.degree
        pa    = image.header['bpa']*u.degree
        beam = Beam(major, minor, pa)
        return Projection(data, wcs=wcs, header=image.header, beam=beam)
    else:
        print("Could not find a beam.")
        return Projection(data, wcs=wcs, header=image.header)


####################################################################################################
#
####################################################################################################
