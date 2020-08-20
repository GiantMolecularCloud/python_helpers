####################################################################################################
# axis location to pixel
####################################################################################################

def coordinate_to_pixel(fitsimage, axis, coordinates, precision=2):
    """
    Calculate the pixel positions corresponding to a given coordinate along an
    axis of an fits image.

    Parameters
    ----------
    fitsimage : string or PrimaryHDU
        File name of a fits image or astropy.fits PrimaryHDU object.
    axis : int
        Axis number. No default.
    coordinates : astropy.Quantity or Quantity list
        The coordinates to be converted in the same unit as the header axis unit.
    precision : int
        Precision  of the return pixel position. Defaults to two decimal places.

    Returns
    -------
    astropy.Quantity or Quantity list
        Single value or list of pixel position corresponding to the given coordinates.

    """

    import astropy.units as u
    from astropy.io import fits

    if isinstance(fitsimage, str):
        header = fits.getheader(fitsimage)
    elif isinstance(fitsimage, fits.hdu.image.PrimaryHDU):
        header = fitsimage.header
    else:
        raise TypeError("Unknown format for fitsimage. Must be filename or HDUList.")

    crpix = header['crpix'+str(axis)]*u.pix
    crval = u.Quantity(str(header['crval'+str(axis)])+header['cunit'+str(axis)])
    cdelt = u.Quantity(str(header['cdelt'+str(axis)])+header['cunit'+str(axis)])/u.pix
    naxis = header['naxis'+str(axis)]

    if not coordinates.unit==crval.unit:
        raise TypeError("Header unit is "+str(crval.unit)+". Use matching unit.")

    return np.round((coordinates-crval)/cdelt+crpix, precision)



####################################################################################################
#
####################################################################################################
