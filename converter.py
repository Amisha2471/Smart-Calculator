from constant import LENGTH_UNITS , WEIGHT_UNITS

def convert_lenghth (value , from_unit, to_unit):

    #convert to base unit (meters)
    value_in_meters = value* LENGTH_UNITS[from_unit]

    #convert from base unit to target
    result = value_in_meters / LENGTH_UNITS[to_unit]

    return round(result , 6)

def convert_weight (value , from_unit, to_unit):

    #convert to base unit (grams)
    value_in_grams = value* WEIGHT_UNITS[from_unit]

    #convert from base unit to target
    result = value_in_grams / WEIGHT_UNITS[to_unit]

    return round(result , 6)

def convert_temperature (value , from_unit, to_unit):

    if from_unit == to_unit:
        return value
    
    #first convert everything to celsius

    if from_unit == "Fahrenheit":
        celsius = (value - 32)* 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value

    #Then convert celsius to target

    if to_unit == "Fahrenheit":
        return round ((celsius * 9/5) + 32 ,2)
    elif to_unit == "Kelvin":
        return round (celsius + 273.15 ,2)
    else:
        return round (celsius  ,2)