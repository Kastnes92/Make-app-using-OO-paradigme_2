def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "feet": 12,
        "inches": 1,
        "mm": 1/25.4,
        "cm": 1/2.54,
        "m": 1/0.0254
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        "pints": 1,
        "quarts": 2,
        "cups": 0.5,
        "ML": 0.00211338,
        "DL": 0.0211338,
        "L": 2.11338
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]


valid_units = {
    "length": ["feet", "inches", "mm", "cm", "m"],
    "volume": ["pints", "quarts", "cups", "ml", "dl", "l"]
}


while True:
    from_type = input("What do you want to convert? (length/volume): ")
    if from_type not in valid_units:
        print("No can do! Pick either 'length' or 'volume'.")
        continue
    from_unit_options = ", ".join(valid_units[from_type])
    from_unit = input(f"Type in {from_type} unit you want to convert from ({from_unit_options}): ")
    if from_unit not in valid_units[from_type]:
        print(f"Not a valid {from_type} unit.")
        continue
    to_unit = input(f"Type in {from_type} unit you want to convert to ({from_unit_options}): ")
    if to_unit not in valid_units[from_type]:
        print(f"Not a valid {from_type} unit.")
        continue
    break

value = float(input(f"Type in {from_unit} value you want to convert: "))

if from_type == "length":
    result = convert_length(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")
else:
    result = convert_volume(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")