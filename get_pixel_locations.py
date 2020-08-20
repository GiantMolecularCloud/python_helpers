####################################################################################################
# get pixel locations for axis
####################################################################################################

def get_pixel_locations(fitsimage, axis):
    """
    Get a list of pixel locations for a given image and axis.

    Parameters
    ----------
    fitsimage : string or PrimaryHDU
        File name of a fits image or astropy.fits PrimaryHDU object.
    axis : int
        Axis number. No default.

    Returns
    -------
    astropy.unit list
        List of coordinates along the axis in the units of the header (e.g. degree for a RA or DEC axis).

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

    return (np.arange(naxis)*u.pix-crpix)*cdelt+crval


####################################################################################################
#
####################################################################################################
