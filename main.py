"""Main module."""

from src.parser import parse_response
from src.to_csv import save_to_file


def main():
    data = parse_response(input("Please enter a URL to parse: ").strip())
    if not data or not len(data):
        print("No data found")
        return

    save_to_file(data)


if __name__ == "__main__":
    main()
    # https://auto.ru/moskva/cars/vendor-foreign/all/engine-benzin/?resolution_filter=is_accidents_ok&steering_wheel=LEFT&transmission=AUTOMATIC&body_type_group=HATCHBACK_5_DOORS&body_type_group=ALLROAD_5_DOORS&body_type_group=SEDAN