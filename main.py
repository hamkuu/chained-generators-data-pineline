def data_stream(data: list):
    for datum in data:
        yield datum


def kelvin_to_celsius(kelvin_data):
    for kelvin_datum in kelvin_data:
        yield kelvin_datum - 273.15


def round_one_decimal(data):
    for datum in data:
        yield round(datum, 1)


def celsius_format(celsius_data):
    for celsius_datum in celsius_data:
        yield f"{celsius_datum}°C"


def pipeline_process(data):
    readings = celsius_format(
        round_one_decimal(
            kelvin_to_celsius(
                data_stream(data)
            )
        )
    )
    print(list(readings))


if __name__ == '__main__':
    raw_data = [0, 273.15, 300, 373.15]
    pipeline_process(raw_data)
