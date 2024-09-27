# ccvt

CCVT: A Converter for Cuscuta campestris


## Install

```
pip3 install git+https://github.com/tamasakian/ccvt.git
```

## Usage

### output

Output protein_id by CcIDs.

```
python3 -m ccvt output <CcID1> <CcID2> ...
```

### generate_list

Generate protein_id list by CcIDs.

```
python3 -m ccvt generate_list <input_file> <output_file>
```

Input file must be in the format;

```{input_file}
<CcID1>
<CcID2>
...
```