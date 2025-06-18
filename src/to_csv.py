"""Save data to csv file."""

import csv
import os
import subprocess
from datetime import datetime

from settings import app_settings
from src import strings

DATA_FORMAT = "%Y-%m-%d_%H-%M-%S"


def save_to_file(data) -> None:
    """Save data to file."""
    file_path = _get_file_name()

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        w = csv.writer(file, delimiter=";")
        w.writerow(
            [
                strings.URL_TITLE,
                strings.CAR_TITLE,
                strings.PRICE_TITLE,
                strings.YEAR_TITLE,
                strings.FEATURES_TITLE,
                strings.BOX_TITLE,
                strings.CAR_TYPE_TITLE,
                strings.DRIVE_TYPE_TITLE,
                strings.COLOR_TITLE,
                strings.KM_AGE_TITLE,
                strings.CITY_TITLE,
                strings.CAR_ORDER,
                strings.SNAPSHOT_DTM
            ]
        )

        for car in data:
            w.writerow([car.url,
                        car.car_title,
                        car.price,
                        car.year,
                        car.features,
                        car.box,
                        car.car_type,
                        car.drive_type,
                        car.color,
                        car.km_age,
                        car.city,
                        car.order,
                        car.snapshot_dtm
                ])

    if app_settings.OPEN_CSV_FILE:
        _open_csv_file(file_path)


def _get_file_name() -> str:
    """Get file name."""
    directory = os.path.join(os.getcwd(), app_settings.CSV_FOLDER_NAME)
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = strings.CSV_FILE_NAME.format(
        current_data=datetime.now().strftime(DATA_FORMAT)
    )

    return os.path.join(directory, filename)


def _open_csv_file(file_path: str) -> None:
    """Open csv file."""
    if os.name == strings.WINDOWS:
        os.startfile(file_path)
    elif os.name == strings.LINUX_MAC:
        subprocess.run(["xdg-open", file_path])
