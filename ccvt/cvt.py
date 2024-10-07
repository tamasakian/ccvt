import json
from pathlib import Path

#!/usr/bin/env python3

"""Library for converting CcID into protein_id.

Functions
---------
output: Output protein_id by CcIDs.
generate_list: Generate protein_id list by CcIDs.
convert_tsv: Parse TSV file and Convert CcID to protein_id.

"""

def output(*input_ids: str) -> None:
    """Output protein_id by CcIDs.

    Args
    ----
    input_ids : tuple
       Input CcIDs.

    """
    with open(f"{Path(__file__).parents[1]}/ccvt/data/cc.json", "r") as input_handle:
        cc_dict = json.load(input_handle)

    for input_id in input_ids:
        if input_id not in cc_dict:
            continue
        print(f"{input_id} -> {cc_dict[input_id]}")

def generate_list(input_filename: str, output_filename: str) -> None:
    """Generate protein_id list by CcIDs.

    Args
    ----
    input_filename : str
       Input CcIDs txt filename.
    output_filename : str
       Output CcIDs txt filename.

    """

    with open(f"{Path(__file__).parents[1]}/ccvt/data/cc.json", "r") as input_handle:
        cc_dict = json.load(input_handle)

    with open(input_filename, "r") as input_handle, open(output_filename, "w") as output_handle:
        for line in input_handle:
            if line.startswith("#"):
                continue
            line = line.strip()
            if line not in cc_dict:
                continue
            output_handle.write(f"{line} -> {cc_dict[line]}\n")


def convert_tsv(input_filename: str, output_filename: str) -> None:
    """Parse TSV file and Convert CcID to protein_id.

    Args
    ----
    input_filename : str
       Input CcIDs TSV filename.
    output_filename : str
       Output CcIDs TSV filename.

    """

    with open(f"{Path(__file__).parents[1]}/ccvt/data/cc.json", "r") as input_handle:
        cc_dict = json.load(input_handle)

    with open(input_filename, "r") as input_handle, open(output_filename, "w") as output_handle:
        for line in input_handle:
            if line.startswith("#"):
                continue
            li = line.strip().split("\t")
            cvt_li = [cc_dict.get(l, l) for l in li]
            output_handle.write("\t".join(cvt_li) + "\n")
