# Caleb Bayles ID: 001271009 WORKS

import get_package_info_from_csv as package_file
import get_distance_info_from_csv as distance_file

# first lets get the optimized lists
# these lists are going to be used then popped just for the algorithm to be used recursively
# 1. first trip
first_delivery_data = []
# 2. second trip
second_delivery_data = []
# 3. first trip
third_delivery_data = []

# declare distance variables for later use
first_delivery_total_distance = 0
second_delivery_total_distance = 0
third_delivery_total_distance = 0

# now we need optimal start times
# 8:00 is best for the first as that is the earliest it can leave and can get packages with deadlines out of the way.
first_trip_leave_time = ['08:00:00']
# 9:05 is best for the second for the packages that have deadlines that will arrive to the hub late,
#  they will go on this one.
second_trip_leave_time = ['09:05:00']
# 11:00 is for all of the other packages that don't really have deadlines
third_trip_leave_time = ['11:00:00']

# now set leave times. O(n)
#  set leave time for first
for index, value in enumerate(package_file.get_first_trip()):
    package_file.get_first_trip()[index][9] = first_trip_leave_time[0]
    first_delivery_data.append(package_file.get_first_trip()[index])
#  set leave time for second
for index, value in enumerate(package_file.get_second_trip()):
    package_file.get_second_trip()[index][9] = second_trip_leave_time[0]
    second_delivery_data.append(package_file.get_second_trip()[index])

#  set leave time for third
for index, value in enumerate(package_file.get_third_trip()):
    package_file.get_third_trip()[index][9] = third_trip_leave_time[0]
    third_delivery_data.append(package_file.get_third_trip()[index])

# find best route form trip lists using our algorithm
#  this will add the values in order to the first trip list in the package file.
distance_file.find_shortest_path(first_delivery_data, 1, 0)
distance_file.find_shortest_path(second_delivery_data, 2, 0)
distance_file.find_shortest_path(third_delivery_data, 3, 0)

# now get the time info for the packages O(n)
iteration = 0
for index in range(len(distance_file.get_first_optimized_trip_list())):
    try:
        iteration += 1
        location_0 = int(distance_file.get_first_optimized_trip_list()[index])
        location_1 = int(distance_file.get_first_optimized_trip_list()[index + 1])
        location_0_index = distance_file.find_package_loc_index_from_package_num(location_0)
        location_1_index = distance_file.find_package_loc_index_from_package_num(location_1)
        first_delivery_total_distance = distance_file.return_distance_sum(
            location_0_index,
            location_1_index,
            first_delivery_total_distance)
        deliver_package = distance_file.get_time(
            distance_file.return_distance(location_0_index, location_1_index),
            first_trip_leave_time)
        distance_file.get_first_list()[index][10] = (str(deliver_package))
    # this errors message is commented because it only happens when its at the end of the list.
    except IndexError:
        # print('Passing due to index error')
        # print('index of error: ', index)
        pass

# for trip 2:
iteration = 0
for index in range(len(distance_file.get_second_optimized_trip_list())):
    try:
        iteration += 1
        location_0 = int(distance_file.get_second_optimized_trip_list()[index])
        location_1 = int(distance_file.get_second_optimized_trip_list()[index + 1])
        location_0_index = distance_file.find_package_loc_index_from_package_num(location_0)
        location_1_index = distance_file.find_package_loc_index_from_package_num(location_1)
        second_delivery_total_distance = distance_file.return_distance_sum(
            location_0_index,
            location_1_index,
            second_delivery_total_distance)
        deliver_package = distance_file.get_time(
            distance_file.return_distance(location_0_index, location_1_index),
            second_trip_leave_time)
        distance_file.get_second_list()[index][10] = (str(deliver_package))
    except IndexError:
        # print('Passing due to index error')
        # print('index of error: ', index)
        pass

# for trip 3:
iteration = 0
for index in range(len(distance_file.get_third_optimized_trip_list())):
    try:
        iteration += 1
        location_0 = int(distance_file.get_third_optimized_trip_list()[index])
        location_1 = int(distance_file.get_third_optimized_trip_list()[index + 1])
        location_0_index = distance_file.find_package_loc_index_from_package_num(location_0)
        location_1_index = distance_file.find_package_loc_index_from_package_num(location_1)
        third_delivery_total_distance = distance_file.return_distance_sum(
            location_0_index,
            location_1_index,
            third_delivery_total_distance)
        deliver_package = distance_file.get_time(
            distance_file.return_distance(location_0_index, location_1_index),
            third_trip_leave_time)
        distance_file.get_third_list()[index][10] = (str(deliver_package))
    except IndexError:
        # print('Passing due to index error')
        # print('index of error: ', index)
        pass

# getting the sum for the distances
sum_one = first_delivery_total_distance
sum_two = second_delivery_total_distance
sum_three = third_delivery_total_distance
sum_total = sum_one + sum_two + sum_three


# print('sum of distance: ', sum_one)
# print('sum of distance 2: ', sum_two)
# print('sum of distance 3: ', sum_three)
#
# print('sum_total: ', sum_total)


# returns the total O(1)
def get_total_distance():
    return sum_total
