import pynbody
import numpy as np

from . import conf


def get_halfmass_radius(halo):
    """Return radius at which half the stellar mass of the halo is contained"""
    # generate a profile for the halo's stellar particles
    with pynbody.analysis.halo.center(halo, mode="pot"):
        p = pynbody.analysis.profile.Profile(halo.s, nbins=1000, ndim=2)

    M_star = sum(halo.s["mass"])

    # Find the radius at which half the stellar mass is contained
    # Interpolate between the point before we exceed half the mass and the point after
    for i, mass_enc in enumerate(p["mass_enc"]):
        if mass_enc > 0.5 * M_star:
            return np.mean(p["rbins"][i-1:i+1])


def get_halfmass_disc(halo):
    """Takes a halo and returns a disc containing half the stellar mass"""
    r = get_halfmass_radius(halo)
    cen = pynbody.analysis.halo.center(halo, mode="pot", retcen=True)
    with pynbody.analysis.angmom.faceon(halo):
        return pynbody.filt.Disc(r, height=conf.SLICE_DISC_HEIGHT, cen=cen)


def get_velocity_dispersion(halo):
    """Calculate velocity dispersion of halo

    Returns geometric mean of the std dev of velocity components perpendicular to ang mom vector
    """
    with pynbody.analysis.halo.center(halo, mode="pot"), pynbody.analysis.angmom.faceon(halo):
        x_velocities = halo.s["vel"][:, 0]
        z_velocities = halo.s["vel"][:, 2]
        return np.sqrt(pow(np.std(x_velocities), 2) + pow(np.std(z_velocities), 2))


def get_virial_sphere(halo):
    """Similar to the halfmass halo, but return a sphere with radius = halfmass radius

    This is a sphere of particles that should satisfy virial relations
    """
    r = get_halfmass_radius(halo)
    cen = pynbody.analysis.center(halo, retcen=True)
    return halo[pynbody.filt.Sphere(r, cen=cen)]


def collect_all(halo):
    results = {}

    cen = pynbody.analysis.halo.center(halo, mode="pot", retcen=True)
    aperture = pynbody.filt.Disc(conf.M_STAR_APERTURE, conf.SLICE_DISC_HEIGHT, cen=cen)
    results["m_star"] = pynbody.halo.SimArray(sum(halo[aperture].s["mass"]), units=halo.s["mass"].units)

    halfmass_disc = get_halfmass_disc(halo)
    halfmass_halo = halo[halfmass_disc]
    results["r_eff"] = halfmass_disc.radius
    results["v_disp"] = get_velocity_dispersion(halfmass_halo)

    sphere = halo[pynbody.filt.Sphere(results["r_eff"], cen=cen)]
    results["M_total"] = pynbody.halo.SimArray(sum(sphere["mass"]), units=sphere["mass"].units)
    results["M_s"] = pynbody.halo.SimArray(sum(sphere.s["mass"]), units=sphere["mass"].units)
    results["M_g"] = pynbody.halo.SimArray(sum(sphere.g["mass"]), units=sphere["mass"].units)
    results["M_d"] = pynbody.halo.SimArray(sum(sphere.d["mass"]), units=sphere["mass"].units)

    return results
