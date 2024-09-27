import json

#!/usr/bin/env python3

"""Library for converting CcID into protein_id.

Functions
---------
output_protein_id: Output protein_id by CcIDs.

"""

def output_protein_id(*input_ids: str) -> None:
    """Output protein_id by CcIDs.

    Args
    ----
    input_ids : tuple
       Input CcIDs.

    """
    with open("../data/cc.json", "r") as input_handle:
        cc_dict = json.load(input_handle)

    for input_id in input_ids:
        if input_id in cc_dict:
            print(cc_dict[input_id])

