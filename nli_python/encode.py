
from .utils import int_2_base, split_groups


# Encode Decimal
def encode_decimal(val: float, precision: int= 6) -> str:
    decimal_vals = str(val).split(".")[1][0:precision].ljust(6, '0')
    return "".join([
        int_2_base(int(digit_group), 32) 
        for digit_group in split_groups(decimal_vals, group_size=3)
])


# Encode Latitude
def encode_latitude_numerical(latitude: float) -> str:
    latitude_numerical = int(int(latitude) + 90)
    return int_2_base(latitude_numerical, 14)


def encode_latitude(latitude: float) -> str:
    assert -90.0 <= latitude <= 90.0, "Latitude out of bounds"

    return f"{encode_latitude_numerical(latitude)}{encode_decimal(latitude)}"


# Encode Longitude
def encode_longitude_numerical(longitude: float) -> str:
    longitude_numerical = int(int(longitude) + 180)
    return int_2_base(longitude_numerical, 19)


def encode_longitude(longitude: float) -> str:
    assert -180.0 <= longitude <= 180.0, "Latitude out of bounds"

    return f"{encode_longitude_numerical(longitude)}{encode_decimal(longitude)}"


def encode_storey(storey: int):
    assert -578 <= storey <= 577, "Storey must be between -578 and 577"
    storey += 578
    return int_2_base(storey, 34)


def encode_ground_level(ground_level: int):
    assert -19652 <= ground_level <= 19651, "Ground Level must be between -19652 and 19651"
    ground_level += 19652
    return int_2_base(ground_level, 34)


# Encode Elevation
def encode_elevation(elevation: int, elevation_type: str = "storey"):
    if elevation_type == "storey":
        return encode_storey(storey=elevation)
    elif elevation_type == "ground_level":
        return encode_ground_level(ground_level=elevation)
    else:
        raise ValueError(f"elevation_type={elevation_type} not in ('storey', 'ground_level')")


# Encode Point
def encode_point(latitude: float,
                 longitude: float,
                 elevation: int = 0,
                 elevation_type: str = "storey") -> str:
    return f"{encode_latitude(latitude)}-{encode_longitude(longitude)}-{encode_elevation(elevation, elevation_type)}"
