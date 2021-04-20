# Caleb Bayles ID: 001271009 WORKS
import csv
from my_hash_class import MyHash

# hash will need to have:
# id as key,
# delivery add.,
# delivery deadline,
# delivery city,
# delivery state,
# delivery zipcode,
# package weight,
# delivery status(delivered, en route, at hub)
# note
# start time
# deliver time

# it needs 10 values including 0

# read in data from package_file.csv
with open('./c950_ups_project/csv_data/package_file.csv', encoding='utf-8-sig') \
        as package_data:
    read_data = csv.reader(package_data, delimiter=',')

    # declare package hash map
    package_hash = MyHash()

    # 3 trips will be sufficient for 40 packages if each can only hold 16

    # trip 1 is truck 1
    # trip 2 is truck 2
    # trip 3 is truck 2

    # has_to_be_on_1_or_2 = [1, 29, 30, 31, 34, 37, 40]
    can_only_be_truck_2 = [3, 18, 36, 38]

    # first trip starts at 8:00 CAN HAVE 10
    has_to_stay_1 = [15, 13, 14, 16, 19, 20]
    the_first_trip_ids = has_to_stay_1 + [1, 29, 30, 31, 34, 37, 39, 40, 32, 21]
    the_first_trip = []

    # second at 9:05 CAN HAVE 14
    has_to_stay_2 = [6, 25]
    the_second_trip_ids = has_to_stay_2 + [2, 3, 4, 5, 7, 12, 26, 38, 36]
    the_second_trip = []

    # third at 11:00 CAN HAVE 16
    the_third_trip_ids = [8, 9, 10, 11, 17, 18, 22, 23, 24, 27, 28, 33, 35]
    the_third_trip = []

    # now we read in the package details into the hashmap O(n)
    for row in read_data:
        # data from csv
        package_id = int(row[0])

        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        deadline = row[5]
        weight = row[6]
        notes = row[7]
        delivery_status = 'At hub'
        delivery_start_time = ''
        delivery_time = ''

        # create a value for hash insert
        value = [package_id, address, city, state, zipcode, deadline, weight,
                 notes, delivery_status, delivery_start_time, delivery_time]

        # add id to the id list for use later
        if package_id in the_first_trip_ids:
            the_first_trip.append(value)
        elif package_id in the_second_trip_ids:
            the_second_trip.append(value)
        elif package_id in the_third_trip_ids:
            the_third_trip.append(value)
        package_hash.add_to_hash(package_id, value)

    # now we need functions to get and transfer to other files

    # these three are very important and will hold the lists of the trips that will be used later O(1)
    def get_first_trip():
        return the_first_trip

    def get_second_trip():
        return the_second_trip

    def get_third_trip():
        return the_third_trip

    # this holds the data for the trip ids for each trip O(1)
    def get_first_package_ids():
        return the_first_trip_ids

    def get_second_package_ids():
        return the_second_trip_ids

    def get_third_package_ids():
        return the_third_trip_ids

    # this will return the updated package hash O(1)
    def get_package_hash():
        return package_hash
