# Summary

Demonstrating an efficient data pipeline processing in Python
by chaining multiple generators.

# Simulated Situation

Given a possibly infinite temperature readings (kelvin) from thermal devices,
we need to render them as Celsius with custom format.

For instance, upon receiving a stream of temperature readings:
`[0.00, 273.15]`, we should expect result `["-273.1°C", "0.0°C"]`


# Processing Steps

- Load raw data and create data stream
- Convert Kelvin to Celsius
- Adjust number with one decimal
- Format with °C symbol 

