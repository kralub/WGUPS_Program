# Caleb Bayles ID: 001271009 WORKS

import csv
from datetime import timedelta
from get_package_info_from_csv import package_hash

# opening index for mapping distances
with open('./c950_ups_project/csv_data/index_address_names.csv',
          encoding='utf-8-sig') as index_address_names:
    index_address_names_data = list(csv.reader(index_address_names, delimiter=','))

# opening distance table for mapping
with open('./c950_ups_project/csv_data/distance_data_clean.csv',
          encoding='utf-8-sig') as distance_file:
    distance_file_data = list(csv.reader(distance_file, delimiter=','))


# returns the address name data O(1)
def return_address_name_list():
    return index_address_names_data


# return the distance from a row to a column and add it to sum. O(1)
def return_distance_sum(row, col, the_sum):
    distance = distance_file_data[row][col]
    # if the distance is on the flip side do this to not get a null value
    if distance == '':
        distance = distance_file_data[col][row]
    return the_sum + float(distance)


# return the row or column for this address in the address index file O(1)
def find_address_index(address_string):
    # print('finding index for ', address_string)
    row_column_index = -1
    for row in index_address_names_data:
        if address_string in row[2]:
            row_column_index = int(row[0])
    if row_column_index == -1:
        print('index not found')
    # else:
    # print('index is: ', row_column_index)
    return row_column_index


# this function will find an index from the values in the truck list, using the address O(1)
def find_index_from_truck_list(value):
    address = value[0]
    the_index = find_package_loc_index_from_package_num(address)
    return the_index


# function to find the address from an index value O(n)
def find_address_from_index(the_index):
    the_address = 'address name not found'
    for row in index_address_names_data:
        if int(row[0]) == the_index:
            the_address = row[2]
            return the_address
    return the_address


# returns the package location index for algorithm use O(1)
def find_package_loc_index_from_package_num(package_num):
    if int(package_num) == 0:
        return 0
    this_package_value = package_hash.get_package(package_num)
    this_address = this_package_value[1]
    if this_address is not None:
        this_address_index = find_address_index(this_address)
        return this_address_index
    else:
        print('find_package_location_from_package_num() did not work!')
        return -1


# return the distance from row to column indexes O(1)
def return_distance(row, col):
    distance = distance_file_data[row][col]
    # if the distance is on the flip side do this to not get a null value
    if distance == '':
        distance = distance_file_data[col][row]
    return float(distance)


# THIS IS MY ALGORITHM TO FIND THE SHORTEST PATH
# I will use the nearest neighbor algorithm

# algorithm INPUT will be The trip number, the trips package list, and the location it is at.

# first lets declare important variables
# package order variables are here, this will have a 0 at the front because it will start at the hub
# and example would look like 0, 3, 4, 8, 13, 0
optimized_first_trip_package_order = []
optimized_second_trip_package_order = []
optimized_third_trip_package_order = []

# this trip distances list is used to know how long the trip took to the next. this will be used in the trip simulator
# example: 2.3, 3.3, 4.1
first_trip_distances = []
second_trip_distances = []
third_trip_distances = []
# this is a list that will hold the whole package data values in order for the package_simulator to use later
first_packages = []
second_packages = []
third_packages = []


# my nearest neighbor truck distance algorithm, GOAL: find shortest path first O(n^2)
def find_shortest_path(package_list, trip_number, current_location_index):
    # this helps the algorithm know when to end the function so that it does not produce an error,
    #  this is the last part that is called and ends it
    if len(package_list) < 1:
        # print('The list is empty for trip ', trip_number, ' optimization.')
        return True
    # declaring variables
    #  this is starting at a high number so that when the loop starts it picks the first distance automatically
    shortest_dist = 1000
    #  this helps to keep track of what package will be delivered next
    shortest_dist_package_num = -1
    # this is important so that we know that index can be used to find the distance
    this_location_index = -1
    # this creates an empty list that will be assigned to one of the values of the truck list to be added for the next
    #  shortest distance.
    value_to_pop = []
    # now it will loop throught each value in package list,
    for value in package_list:
        the_package_id = value[0]
        package_location_index = find_package_loc_index_from_package_num(the_package_id)
        distance_to_next = return_distance(current_location_index, package_location_index)
        # this is for list one and puts 15 at the very beginning because of its timing constraint.
        # if the id is 15 it will break out of this loop and put it first
        if the_package_id == 15:
            shortest_dist = distance_to_next
            shortest_dist_package_num = the_package_id
            this_location_index = package_location_index
            value_to_pop = value
            break
        # here is where it gets nearest! Here the we are testing to see if it will create a shorter path,
        #   if it does, then that will be the new path that it will add, but it will go through
        #   every value to see if it can find a shorter one first
        if distance_to_next < shortest_dist:
            shortest_dist = distance_to_next
            shortest_dist_package_num = the_package_id
            this_location_index = package_location_index
            value_to_pop = value

    # now for the add part it works like so:
    # 1. add to the optimized package list AND distance list
    # 2. remove from the package list for the next iteration (on last call it would make list 0)
    # 3. update the current location
    # 4. (removed, not necessary) if it is the list length is 0, add in the distance for going back to the hub
    # 5. then recursively call the function again after these updates

    # eventually when the list is empty it will finish and the package list will be optimized
    if trip_number == 1:
        # 1.
        first_packages.append(value_to_pop)
        optimized_first_trip_package_order.append(shortest_dist_package_num)
        first_trip_distances.append(shortest_dist)
        # 2.
        package_list.pop(package_list.index(value_to_pop))
        # 3.
        current_location_index = this_location_index
        # 4.
        # if len(package_list) == 0:
        #     optimized_first_trip_package_order.append(0)
        #     first_trip_distances.append(return_distance(0, this_location_index))
        #     print('Truck is heading back to the hub from location index: ', this_location_index,
        #           ', for trip: ', trip_number, '.')
        # 5.
        find_shortest_path(package_list, 1, current_location_index)
    elif trip_number == 2:
        # 1.
        second_packages.append(value_to_pop)
        optimized_second_trip_package_order.append(shortest_dist_package_num)
        second_trip_distances.append(shortest_dist)
        # 2.
        package_list.pop(package_list.index(value_to_pop))
        # 3.
        current_location_index = this_location_index
        # 4.
        # if len(package_list) == 0:
        #     # optimized_second_trip_package_order.append(0)
        #     # second_trip_distances.append(return_distance(0, this_location_index))
        #     print('Truck is heading back to the hub from location index: ', this_location_index,
        #           ', for trip: ', trip_number, '.')
        # 5.
        find_shortest_path(package_list, 2, current_location_index)
    elif trip_number == 3:
        # 1.
        third_packages.append(value_to_pop)
        optimized_third_trip_package_order.append(shortest_dist_package_num)
        third_trip_distances.append(shortest_dist)
        # 2.
        package_list.pop(package_list.index(value_to_pop))
        # 3.
        current_location_index = this_location_index
        # 4.
        # if len(package_list) == 0:
        #     # optimized_first_trip_package_order.append(0)
        #     # first_trip_distances.append(return_distance(0, this_location_index))
        #     print('Truck is heading back to the hub from location index: ', this_location_index,
        #           ', for trip: ', trip_number, '.')
        # 5.
        find_shortest_path(package_list, 3, current_location_index)


# inserting 0 at beginning for WGU HUB
optimized_first_trip_package_order.insert(0, 0)
optimized_second_trip_package_order.insert(0, 0)
optimized_third_trip_package_order.insert(0, 0)


# getting optimized trip lists, this will only return the ids not the values O(1)
def get_first_optimized_trip_list():
    return optimized_first_trip_package_order


def get_second_optimized_trip_list():
    return optimized_second_trip_package_order


def get_third_optimized_trip_list():
    return optimized_third_trip_package_order


# getting trip lists this will return the values in order O(1)
def get_first_list():
    return first_packages


def get_second_list():
    return second_packages


def get_third_list():
    return third_packages


# getting distance lists in order O(1)
def get_optimized_first_trip_distances_list():
    return first_trip_distances


def get_optimized_second_trip_distances_list():
    return second_trip_distances


def get_optimized_third_trip_distances_list():
    return third_trip_distances


# time function that will be used in the package simulator to find distances time O(n)
def get_time(distance, truck_list):
    # makes time with 18 mph speed in consideration
    eighteen_time = distance / 18
    # converts the time to readable 00:00:00
    distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(eighteen_time * 60, 60))
    final_time = distance_in_minutes + ':00'
    truck_list.append(final_time)
    total = timedelta()
    for i in truck_list:
        (hrs, mins, secs) = i.split(':')
        total += timedelta(hours=int(hrs),
                           minutes=int(mins), seconds=int(secs))
    return total
