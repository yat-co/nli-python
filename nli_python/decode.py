
from .utils import base_2_int, split_groups

from typing import Tuple


# Decode Decimal
def decode_decimal(encoded_val: str):
    encoded_pair = split_groups(encoded_val, 2)
    return "".join([
        str(base_2_int(encoded_val=encoded_digit, base=32)).zfill(3)
        for encoded_digit in encoded_pair
    ])


# Decode Latitude
def decode_latitude(encoded_val: str):
    whole_digit_encoded = encoded_val[0:2]
    decimal_encoded = encoded_val[2:6]

    whole_digit_decode = base_2_int(encoded_val=whole_digit_encoded, base=14)
    decimal_decoded = decode_decimal(encoded_val=decimal_encoded)
    return float(f"{int(whole_digit_decode)-90}.{decimal_decoded}")


# Decode Longitude
def decode_longitude(encoded_val: str):
    whole_digit_encoded = encoded_val[0:2]
    decimal_encoded = encoded_val[2:6]

    whole_digit_decode = base_2_int(encoded_val=whole_digit_encoded, base=19)
    decimal_decoded = decode_decimal(encoded_val=decimal_encoded)
    return float(f"{int(whole_digit_decode)-180}.{decimal_decoded}")


# Decode Storey
def decode_storey(encoded_val: str):
    return base_2_int(encoded_val, 34) - 578


# Decode Ground Level
def decode_ground_level(encoded_val: str):
    return base_2_int(encoded_val, 34) - 19652


# Decode Elevation
def decode_elevation(encoded_val: str):
    if len(encoded_val) == 2:
        return decode_storey(encoded_val=encoded_val), "storey"
    elif len(encoded_val) == 3:
        return decode_ground_level(encoded_val=encoded_val), "ground_level"
    else:
        raise ValueError(f"encoded_val={encoded_val} must be of length 2 or 3")


# Decode Point
def decode_point(encoded_val: str) -> Tuple[float, float, Tuple[int, str]]:
    assert len(encoded_val.split("-")) == 3, "encoded value requires <lat>-<long>-<elev>"
    
    # Decoding Point
    encoded_lat, encoded_long, encoded_elev = encoded_val.split("-")
    return (
        decode_latitude(encoded_val=encoded_lat), 
        decode_longitude(encoded_val=encoded_long),
        *decode_elevation(encoded_val=encoded_elev)
    )
