# rename module on import
import statistics as s

# import specific property from module
from statistics import variance

# combine the two
from statistics import variance as v

# import multiple properties from module
from statistics import variance, mean

# import multiple properties renamed
from statistics import variance as v, mean as m

# import everything from statistics (e.g. will assign variance to variance)
from statistics import *
