"""Aitoff projection sky map plotting in J2000 equatorial coordinates."""
from astropy import units as u
from astropy.time import Time
from matplotlib import pyplot as plt
import numpy as np
import spiceypy


class AitoffPlotter:
    """All-sky map plotter using Aitoff projection in J2000 equatorial coordinates.

    This class provides functionality to plot celestial bodies and spacecraft
    positions on an all-sky Aitoff projection. It operates in J2000 equatorial
    coordinates (right ascension and declination) without Earth-orientation or
    horizon effects, making it suitable for inertial sky visualization.

    Parameters
    ----------
    epoch : ~astropy.time.Time, optional
        Epoch for the sky map. Defaults to current time.
    ax : ~matplotlib.axes.Axes, optional
        Matplotlib axes to use. If None, creates a new figure with Aitoff projection.
    figsize : tuple, optional
        Figure size in inches. Defaults to (12, 8).
    style : str, optional
        Matplotlib style to use. Defaults to 'dark_background' for night sky appearance.
    show_ecliptic : bool, optional
        Whether to plot the ecliptic reference line. Defaults to True.
    ecliptic_obliquity : float, optional
        Mean obliquity of the ecliptic in degrees (J2000). Defaults to 23.439281.

    Examples
    --------
    >>> from boinor.plotting.aitoff import AitoffPlotter
    >>> from astropy.time import Time
    >>> plotter = AitoffPlotter(epoch=Time.now())
    >>> plotter.plot_ra_dec(ra=0*u.deg, dec=0*u.deg, label="Test")
    >>> plotter.show()

    Notes
    -----
    The Aitoff projection is a modified azimuthal map projection that displays
    the entire celestial sphere. Longitude values are converted to matplotlib's
    expected format ([-π, π]) and inverted to match standard sky map conventions
    where 0° longitude is on the left.

    References
    ----------
    - Aitoff projection: https://en.wikipedia.org/wiki/Aitoff_projection
    - J2000 coordinate system: https://en.wikipedia.org/wiki/Epoch_(astronomy)#J2000.0
    - Overview of Reference Frames and Coordinate Systems in SPICE: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/Tutorials/pdf/individual_docs/17_frames_and_coordinate_systems.pdf

    """

    def __init__(
        self,
        epoch=None,
        ax=None,
        figsize=(12, 8),
        style="dark_background",
        show_ecliptic=True,
        ecliptic_obliquity=23.439281,
    ):
        """Initialize the Aitoff plotter."""
        self.epoch = epoch if epoch is not None else Time.now()
        self.show_ecliptic = show_ecliptic
        self.ecliptic_obliquity = np.radians(ecliptic_obliquity)

        # Set matplotlib style
        plt.style.use(style)

        # Create or use provided axes
        if ax is None:
            self.fig, self.ax = plt.subplots(figsize=figsize, subplot_kw={"projection": "aitoff"})
        else:
            self.ax = ax
            self.fig = ax.figure

        # Plot ecliptic reference line if requested
        if self.show_ecliptic:
            self._plot_ecliptic()

    def _plot_ecliptic(self):
        """Plot the ecliptic (β = 0°) as a reference curve in equatorial coordinates.

        The ecliptic is converted from ecliptic coordinates (λ, β=0) to equatorial
        coordinates (α, δ) using a rotation about the x-axis by the obliquity angle.

        """
        # Sample ecliptic longitudes λ across [-π, π]; β = 0
        lam = np.linspace(np.pi, -np.pi, 2000)
        beta = 0.0

        # Convert ecliptic (λ, β=0) -> equatorial (α, δ) via rotation about x-axis by +ε
        # Ecliptic unit vector:
        x = np.cos(lam) * np.cos(beta)
        y = np.sin(lam) * np.cos(beta)
        z = np.sin(beta) * np.ones_like(lam)

        # Rotate to equatorial:
        eps = self.ecliptic_obliquity
        y_eq = y * np.cos(eps) - z * np.sin(eps)
        z_eq = y * np.sin(eps) + z * np.cos(eps)
        x_eq = x

        # Convert to RA/Dec
        ra = np.arctan2(y_eq, x_eq)  # [-π, π]
        dec = np.arcsin(z_eq)

        # Convert to matplotlib format (reverse and normalize to [-π, π])
        ra4plot = -ra
        ra4plot = (ra4plot + np.pi) % (2 * np.pi) - np.pi  # keep in [-π, π]

        self.ax.plot(
            ra4plot,
            dec,
            linestyle="-",
            linewidth=1.2,
            alpha=0.9,
            label="Ecliptic",
            color="gray",
        )

    def _convert_longitude_for_plot(self, longitude_rad):
        """Convert longitude values to matplotlib Aitoff format.

        Parameters
        ----------
        longitude_rad : ~numpy.ndarray or float
            Longitude values in radians (0 to 2π)

        Returns
        -------
        ~numpy.ndarray or float
            Longitude values in matplotlib format ([-π, π], inverted)

        Notes
        -----
        Matplotlib expects values between -π and +π. Sky maps count from
        0° longitude to the left, so we need to invert the longitude values.

        """
        # Normalize to [0, 2π) first
        if isinstance(longitude_rad, np.ndarray):
            normalized = longitude_rad % (2 * np.pi)
            return np.array([-1 * ((x % np.pi) - np.pi) if x > np.pi else -1 * x for x in normalized])

        normalized = longitude_rad % (2 * np.pi)
        return -1 * ((normalized % np.pi) - np.pi) if normalized > np.pi else -1 * normalized

    def plot_ra_dec(self, ra, dec, label=None, color=None, marker="o", markersize=12, **kwargs):
        """Plot a point on the sky map using right ascension and declination.

        Parameters
        ----------
        ra : ~astropy.units.Quantity or float
            Right ascension. If float, assumed to be in radians.
        dec : ~astropy.units.Quantity or float
            Declination. If float, assumed to be in radians.
        label : str, optional
            Label for the plotted point.
        color : str, optional
            Color for the marker. If None, uses matplotlib default.
        marker : str, optional
            Marker style. Defaults to 'o'.
        markersize : float, optional
            Size of the marker. Defaults to 12.
        **kwargs
            Additional keyword arguments passed to matplotlib's plot function.

        Returns
        -------
        ~matplotlib.lines.Line2D
            The plotted line/marker object.

        """
        # Convert to radians if needed
        if hasattr(ra, "to"):
            ra_rad = ra.to(u.rad).value
        else:
            ra_rad = ra

        if hasattr(dec, "to"):
            dec_rad = dec.to(u.rad).value
        else:
            dec_rad = dec

        # Convert RA to plot format (longitude)
        ra4plot = self._convert_longitude_for_plot(ra_rad)

        # Plot the point
        line = self.ax.plot(
            ra4plot,
            dec_rad,
            color=color,
            marker=marker,
            linestyle="None",
            markersize=markersize,
            label=label,
            **kwargs,
        )

        return line[0] if isinstance(line, list) else line

    def plot_spice_position(
        self,
        target,
        observer="EARTH",
        frame="J2000",
        abcorr="LT+S",
        label=None,
        color=None,
        marker="o",
        markersize=12,
        **kwargs,
    ):
        """Plot a body position using SPICE ephemeris.

        Parameters
        ----------
        target : str or int
            SPICE target name or NAIF ID code.
        observer : str or int, optional
            SPICE observer name or NAIF ID code. Defaults to "EARTH".
        frame : str, optional
            Reference frame. Defaults to "J2000".
        abcorr : str, optional
            Aberration correction. Defaults to "LT+S" (light time + stellar aberration).
        label : str, optional
            Label for the plotted point.
        color : str, optional
            Color for the marker. If None, uses matplotlib default.
        marker : str, optional
            Marker style. Defaults to 'o'.
        markersize : float, optional
            Size of the marker. Defaults to 12.
        **kwargs
            Additional keyword arguments passed to matplotlib's plot function.

        Returns
        -------
        ~matplotlib.lines.Line2D
            The plotted line/marker object.

        Raises
        ------
        ImportError
            If spiceypy is not installed.

        Notes
        -----
        This method requires SPICE kernels to be loaded beforehand using
        ``spiceypy.furnsh()``. The position is computed in the specified frame
        and converted to J2000 equatorial coordinates (RA/Dec).

        """
        if spiceypy is None:
            raise ImportError("spiceypy is required for SPICE-based plotting. Install it with: pip install spiceypy")

        # Convert epoch to ephemeris time
        if isinstance(self.epoch, Time):
            et = spiceypy.utc2et(self.epoch.utc.iso)
        else:
            et = self.epoch

        # Get position vector
        pos, _ = spiceypy.spkpos(str(target), et, frame, abcorr, str(observer))

        # Convert Cartesian to spherical (RA/Dec)
        # recrad returns: (distance, longitude, latitude)
        _, ra_rad, dec_rad = spiceypy.recrad(pos)

        # Plot using RA/Dec
        return self.plot_ra_dec(
            ra_rad * u.rad,
            dec_rad * u.rad,
            label=label,
            color=color,
            marker=marker,
            markersize=markersize,
            **kwargs,
        )

    def set_title(self, title=None):
        """Set the plot title.

        Parameters
        ----------
        title : str, optional
            Title text. If None, uses the epoch in UTC format.

        """
        if title is None:
            if isinstance(self.epoch, Time):
                title = f"{self.epoch.utc.iso} UTC"
            else:
                title = "Sky Map"
        self.ax.set_title(title, fontsize=10)

    def set_labels(self):
        """Set standard axis labels for the sky map."""
        self.ax.set_xlabel("Eq. long. in hours")
        self.ax.set_ylabel("Eq. lat. in deg")

    def set_ticks(self):
        """Set standard tick labels for right ascension in hours."""
        ticks = np.radians([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150])
        labels = ["10 h", "8 h", "6 h", "4 h", "2 h", "0 h", "22 h", "20 h", "18 h", "16 h", "14 h"]
        self.ax.set_xticks(ticks)
        self.ax.set_xticklabels(labels)

    def show(self):
        """Display the plot with legend and grid."""
        self.set_title()
        self.set_labels()
        self.set_ticks()
        self.ax.legend()
        self.ax.grid(True)
        plt.show()

    def save(self, filename, **kwargs):
        """Save the plot to a file.

        Parameters
        ----------
        filename : str
            Output filename.
        **kwargs
            Additional keyword arguments passed to matplotlib's savefig function.

        """
        self.fig.savefig(filename, **kwargs)
