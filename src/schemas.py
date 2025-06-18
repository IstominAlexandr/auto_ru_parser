"""Project schemas."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    url: str = ""
    car_title: str = ""
    price: int = 0
    year: int = 0
    features: str = ""
    box: str = ""
    car_type: str = ""
    drive_type: str = ""
    color: str = ""
    km_age: int = 0
    city: str = ""
    order: str = ""
    snapshot_dtm: str = ""