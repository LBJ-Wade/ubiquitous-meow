"""
Functions for Argonaut Simulation snapshot processing
"""

import os
import shutil

from . import conf, templates


DATA_DIR = conf.DATA_DIR
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")


def apply_totipnat(snapshot_input_file, tipsy_output_file):
    """Converts an Argonaut simulation snapshot to tipsy binary format using totipnat

    snapshot_input_file (str): path to snapshot input file
    tipsy_output_file (str): desired destination for output tipsy binary
    """
    exit_val = os.system("{totipnat} < {snapshot} > {dest}".format(
            totipnat=conf.TOTIPNAT,
            snapshot=snapshot_input_file,
            dest=tipsy_output_file))
    if exit_val != 0:
        raise Exception("Conversion to tipsy failed. Check snapshot file permissions.")

    return tipsy_output_file

def _generate_ahf_input_file(dest_dir, tipsy_input_file):
    """Geneartes ahf params.input from template with desired tipsy input file path"""
    template = templates.get("ahf.params.input")
    input_file_path = os.path.join(dest_dir, "params.input")

    with open(input_file_path, "w+") as input_file:
        input_file.write(template.format(
            input_filename=tipsy_input_file,
            output_prefix=os.path.join(dest_dir, "ahf")))

    return input_file_path

def _generate_gas_file(dest_dir, d_hubble_0):
    """Generates gas.param file for ahf output"""
    template = templates.get("ahf.gas.param")
    gas_file_path = os.path.join(dest_dir, "gas.param")

    with open(gas_file_path, "w+") as gas_file:
        gas_file.write(template.format(dHubble0=d_hubble_0))

    return gas_file_path

def apply_ahf(tipsy_input_file, dest_dir):
    """Applies Amiga Halo Finder algorithm to tipsy binary file

    tipsy_input_file (str): path to tipsy binary to apply ahf to
    dest_dir (str): path to directory to store ahf output files
    """
    input_file_path = _generate_ahf_input_file(tipsy_input_file, dest_dir)

    # setup dest dir by creating directories and copying template files
    exit_val = os.system("{ahf} {input_file}".format(
        ahf=conf.AHF,
        input_file=input_file_path))
    if exit_val != 0:
        raise Exception("AHF failed for tipsy binary {}".format(tipsy_input_file))

    # TODO: get dhubble0 somehow, which can be determined from the snapshot's redshift, z
    # maybe use a mapping between redshifts and dhubble0
    d_hubble_0 = 2.060
    _generate_gas_file(dest_dir, d_hubble_0)


def run(sim_run, snapshot_filename):
    snapshot_path = os.path.join(RAW_DATA_DIR, sim_run, snapshot_filename)
    output_path = os.path.join(PROCESSED_DATA_DIR, sim_run, snapshot_filename, "apply_totipnat")

    try:
        os.makedirs(output_path)
    except OSError:
        pass

    apply_totipnat(snapshot_path, os.path.join(output_path, "tipsy.bin"))

    ahf_output_dir = os.path.join(PROCESSED_DATA_DIR, sim_run, snapshot_filename, "apply_ahf")
    try:
        os.makedirs(ahf_output_dir)
    except OSError:
        pass

    apply_ahf(tispy_bin_path, ahf_output_dir)
    shutil.copy(snapshot_path, os.path.join(ahf_output_dir, "ahf"))
