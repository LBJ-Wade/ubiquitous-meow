import matplotlib
matplotlib.use("Agg")

import pynbody


def load_snapshot_and_halos(snapshot_file):
    """Load snapshot and halos from file.

    Return tuple of (snapshot object, halo catalog)

    TODO: Update function to take a whole directory, and find snapshot file automatically
    """
    s = pynbody.load(snapshot_file)
    h = s.halos()
    s["pos"]  # triggers pynbody to load attributes
    del s["rho"]
    s.physical_units()

    return s, h
