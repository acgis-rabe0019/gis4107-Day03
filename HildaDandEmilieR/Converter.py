def miles_to_km(miles):
    return 1.609 * miles

def km_per_hr_to_m_per_sec(KmPerHr):
    return 0.277 * KmPerHr

def sqmetres_to_hectares(sqmetres):
    return 0.0001 * sqmetres

def sqmetres_to_acres(sqmetres):
    return 0.000247 * sqmetres

def acres_to_edge_of_square(acres):
    meterSq = acres * 4046.85
    m = (meterSq) ** 0.5
    return m

def get_bear_count(bear_d,a_sqmetres):
    get_bear_count = (a_sqmetres * 0.000001) * (bear_d)
    return get_bear_count

def dms_to_dd(degree,min,sec):
    dms_to_dd = degree + (min/60.000) + (sec/3600.000)
    return dms_to_dd

def dd_to_dms(dd):
    degrees = int(dd)
    dd_minutes = (dd - degrees) * 60
    minutes = int(dd_minutes)
    seconds  = round((dd_minutes - minutes) * 60)
    dd_to_dms = str(dd) + " = " + str(degrees) + ":" + str(minutes) + ":" + str(seconds)
    return dd_to_dms

def get_fuel_cost(km,mpg,dl):
    get_fuel_cost = (((km / 1.6) / mpg) * 3.78)* dl
    return get_fuel_cost