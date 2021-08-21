import statistics # built in python module

example_list = [5,67,44,5,65,6,4,3,3,5,6,7,4,3,3,22,21,5,65,64,63,436]

mean = statistics.mean(example_list)
print(mean)

median = statistics.median(example_list)
print(median)

stdev = statistics.stdev(example_list)
print(stdev)

variance = statistics.variance(example_list)
print(variance)