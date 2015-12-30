import os


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DATA_DIR = os.getenv("DATA_DIR", os.path.join(PROJECT_DIR, "data"))
TEMPLATES_DIR = os.getenv("TEMPLATES_DIR", os.path.join(PROJECT_DIR, "templates"))

# AHF processed snapshot to use in jupyter Notebooks
NOTEBOOK_SAMPLE = os.path.join(
    DATA_DIR, "processed", "nSFR5_MR",
    "G184948_veryhighRes_WMAP3_toz2.00240", "apply_ahf", "ahf")

TOTIPNAT = os.getenv("TOTIPNAT", "totipnat")
AHF = os.getenv("AHF", "ahf")

M_STAR_APERTURE = "12 kpc"
SLICE_DISC_HEIGHT = "50 kpc"
