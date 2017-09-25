import Converter
reload(Converter)

print  "10 miles = " + str(Converter.miles_to_km(10.0)) + "km"

print "100 km per hour = " + str(Converter.km_per_hr_to_m_per_sec(100)) + " m per seconds"

print "10000 square metres = " + str(Converter.sqmetres_to_hectares(10000)) + " hectares"

print "10000 square metres = " + str(Converter.sqmetres_to_acres(10000)) + " acres"

print "Edge length of a 2 acres square is " + str(Converter.acres_to_edge_of_square(2)) + " metres."

print "When bear density is 4 bears per square km and area is"