import Converter
reload(Converter)

print  "10 miles = " + str(Converter.miles_to_km(10.0)) + "km"

print "100 km per hour = " + str(Converter.km_per_hr_to_m_per_sec(100)) + " m per seconds"

print "10000 square metres = " + str(Converter.sqmetres_to_hectares(10000)) + " hectares"

print "10000 square metres = " + str(Converter.sqmetres_to_acres(10000)) + " acres"

print "Edge length of a 2 acres square is " + str(Converter.acres_to_edge_of_square(2)) + " metres."

print "When bear density is 4 bears per square km and area is 10 000 000 square metres, the probable number of bears is " + str(Converter.get_bear_count(4,10000000))

print "95:25:5 = " + str(Converter.dms_to_dd(95,25,5))

print str(Converter.dd_to_dms(95.41805))

print "100 km at 35 mi/gal and $ 1.30 per L will cost $" + str(Converter.get_fuel_cost(100,35,1.30))