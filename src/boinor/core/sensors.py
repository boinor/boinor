from numba import njit as jit
import numpy as np


@jit
def min_and_max_ground_range(h, eta_fov, eta_center, R):
    """Calculates the minimum and maximum values of ground-range angles.

    Parameters
    ----------
    h : float
        Altitude over surface.
    eta_fov : float
        Angle of the total area that a sensor can observe.
    eta_center : float
        Center boresight angle.
    R : float
        Attractor equatorial radius.

    Returns
    -------
    lambdaBig_min: float
        Minimum value of latitude and longitude.
    lambdaBig_max: float
        Maximum value of latitude and longitude.

    Notes
    -----
    For further information, please take a look at :cite:t:`Vallado2013`, pages 853-860.

    """
    r_sat = R + h
    eta_max = eta_center + eta_fov / 2
    eta_min = eta_center - eta_fov / 2
    gamma_max = np.arcsin(r_sat * np.sin(eta_max) / R)

    if abs(gamma_max) <= np.pi / 2:
        gamma_max = np.pi - gamma_max
    gamma_min = np.arcsin(r_sat * np.sin(eta_min) / R)
    if abs(gamma_min) <= np.pi / 2:
        gamma_min = np.pi - gamma_min

    # Maximum and minimum slant ranges
    rho_max = R * np.cos(gamma_max) + r_sat * np.cos(eta_max)
    rho_min = R * np.cos(gamma_min) + r_sat * np.cos(eta_min)
    lambdaBig_max = np.arcsin(rho_max * np.sin(eta_max) / R)
    lambdaBig_min = np.arcsin(rho_min * np.sin(eta_min) / R)

    return lambdaBig_min, lambdaBig_max


@jit
def ground_range_diff_at_azimuth(
    h, eta_fov, eta_center, beta, phi_nadir, lambda_nadir, R
):
    """Calculates the difference in ground-range angles from the eta_center angle and the latitude and longitude of the target
    for a desired phase angle, beta, used to specify where the sensor is looking.

    Parameters
    ----------
    h : float
        Altitude over surface.
    eta_fov : float
        Angle of the total area that a sensor can observe.
    eta_center : float
        Center boresight angle.
    beta : float
        Phase angle, used to specify where the sensor is looking.
    phi_nadir : float
        Latitude angle of nadir point.
    lambda_nadir : float
        Longitude angle of nadir point.
    R : float
        Earth equatorial radius.

    Returns
    -------
    delta_lambda : float
        The difference in ground-range angles from the eta_center angle.
    phi_tgt: float
        Latitude angle of the target point.
    lambda_tgt : float
        Longitude angle of the target point.

    Notes
    -----
    For further information, please take a look at :cite:t:`Vallado2013`, pages 853-860.

    """
    if not 0 <= beta < np.pi:
        raise ValueError("beta must be between 0º and 180º")

    r_sat = R + h
    gamma = np.arcsin(r_sat * np.sin(eta_center) / R)
    if abs(gamma) <= np.pi / 2:
        gamma = np.pi - gamma

    rho = R * np.cos(gamma) + r_sat * np.cos(eta_center)
    lambdaBig = np.arcsin(rho * np.sin(eta_center) / R)
    phi_tgt = np.arcsin(
        np.cos(beta) * np.cos(phi_nadir) * np.sin(lambdaBig)
        + np.sin(phi_nadir) * np.cos(lambdaBig)
    )
    delta_lambdaBig = np.arcsin(
        np.sin(beta) * np.sin(lambdaBig) / np.cos(phi_tgt)
    )
    lambda_tgt = lambda_nadir + delta_lambdaBig
    lambdaBig_min, lambdaBig_max = min_and_max_ground_range(
        h, eta_fov, eta_center, R
    )
    delta_lambda = (lambdaBig_max - lambdaBig_min) / 2

    return delta_lambda, phi_tgt, lambda_tgt
