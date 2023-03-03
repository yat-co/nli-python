# nli Python

An elegantly simple Encoding and Decoding of Location to eNLI Codes (Natural Location Identifier).

Reference: https://e-nli.org/enli-code

## Install 

With Python 3.7 or greater install the package with simple pip command.

```
pip install nli_python
```

## Usage

Convert Tuple of Latitude, Longitude and Elevation to nli then convert nli back 
to Tuple of Latitude, Longitude and Elevation

Encode Point
```python
from nli_python import encode_point

latitude, longitude = (39.048397, -94.484322)
elevation = 60
elevation_type="ground_level"
encoded_point = encode_point(
    latitude=latitude, longitude=longitude, elevation=elevation, elevation_type=elevation_type
)
print(encoded_point)
>>> 931GCD-4AF4A2-H1Q
```

Decode enli to Point
```python
from nli_python import decode_point

encoded_point = '931GCD-4AF4A2-H1Q'
decoded_point = decode_point(encoded_point)
print(decoded_point)
>>> (39.048397, -94.484322, 60)
```