####################################################################################################
# get axis info
####################################################################################################

def get_axis_info(fitsimage,axis):
    """
    Get the axis information (crpix, crval, cddelt) as astropy.units objects.

    Parameters
    ----------
    fitsimage : string or PrimaryHDU
        File name of a fits image or astropy.fits PrimaryHDU object.
    axis : int
        Axis number. No default.

    Returns
    -------
    list
        Returns crpix, crval, cdelt with astropy units.

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
    cdelt = u.Quantity(str(header['cdelt'+str(axis)])+header['cunit'+str(axis)])

    return crpix, crval, cdelt


####################################################################################################
#
####################################################################################################
