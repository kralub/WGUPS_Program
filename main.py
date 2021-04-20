# Caleb Bayles ID: 001271009 WORKS

import get_distance_info_from_csv as distance_file
import package_time_simulator
from datetime import timedelta

# row ints for package hash are as follows
package_id = 0
address = 1
city = 2
state = 3
zipcode = 4
deadline = 5
weight = 6
notes = 7
status = 8
leave_time = 9
deliver_time = 10


# trip 1 is truck 1
# trip 2 is truck 2
# trip 3 is truck 2
# just used for testing O(n)
def testing_trucks():
    # package list 1: works with constraints!
    iteration_num = 1
    print('Trip 1 order ids: ', distance_file.get_first_optimized_trip_list())
    for i in range(len(distance_file.get_first_list())):
        print('First trip iteration: ', iteration_num, distance_file.get_first_list()[i])
        iteration_num += 1

    # package list 2: works with constraints!
    iteration_num = 1
    print('Trip 2 order ids: ', distance_file.get_second_optimized_trip_list())
    for i in range(len(distance_file.get_second_list())):
        print('Second trip iteration:', iteration_num, distance_file.get_second_list()[i])
        iteration_num += 1

    # package list 3: works with constraints!
    iteration_num = 1
    print('Trip 3 order ids: ', distance_file.get_third_optimized_trip_list())
    for i in range(len(distance_file.get_third_list())):
        print('Third trip iteration:', iteration_num, distance_file.get_third_list()[i])
        iteration_num += 1

    sum_tot = package_time_simulator.get_total_distance()
    print('THE TOTAL DISTANCE IS: ', sum_tot)


# make lists for interface use
updated_first_list = distance_file.get_first_list()
updated_second_list = distance_file.get_second_list()
updated_third_list = distance_file.get_third_list()


# testing_list = updated_first_list + updated_second_list + updated_third_list

# displays the welcome test and sum O(1)
def display_welcome():
    print('All packages have been delivered with a TOTAL DISTANCE OF: ',
          package_time_simulator.get_total_distance(), ' MILES. \nTrip 1 was TRUCK 1, '
                                                       '\nTrip 2 and 3 were Truck 2.'
                                                       '\n\Starting up database...')
    print('\n******************************************************************'
          '\n           WELCOME TO THE WGUPS ROUTING SOFTWARE!!! '
          '\n******************************************************************')
    print(
        '-- Please enter "all" to see the status of all packages at a certain time. '
        '\n-- Enter "one" to see the status of one package at a certain time.\n'
        '-- Enter "test" to show the notes for verification in the I.2 requirement.\n'
        '-- Enter "exit" to stop the program.\n')


# this will get an inputted time and update the list with status and return that list. O(n)
def update_list_with_time(the_time):
    # users time input
    time_for_status = the_time

    # get all packages in one list
    full_updated_list = updated_first_list + updated_second_list + updated_third_list

    # make the input a time delta
    (hrs, mins, secs) = time_for_status.split(':')
    user_input_time = timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

    # loop through and change status based on time.
    # [21, '3595 Main St', 'Salt Lake City', 'UT', '84115', 'EOD', '3', 'none', 'At hub', '11:00:00', '11:07:00']
    for i in full_updated_list:
        try:
            # get times for each package
            this_leave_time = i[leave_time]
            this_deliver_time = i[deliver_time]

            # convert to time delta
            (hrs, mins, secs) = this_leave_time.split(':')
            this_leave_time = timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = this_deliver_time.split(':')
            this_deliver_time = timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

            # if at hub
            if this_leave_time > user_input_time:
                i[status] = 'At Hub'
            # if delivered
            elif ((this_leave_time < user_input_time) and (this_deliver_time < user_input_time)) \
                    or this_deliver_time == user_input_time:
                i[status] = 'Delivered'
            # if on the road
            elif (this_leave_time < user_input_time) and (this_deliver_time > user_input_time):
                i[status] = 'On The Road'

        except ValueError:
            print('there is a value error in update with time')
            return 0
            pass
    return full_updated_list


# this prints every package in consideration to the time inputted. O(n)
def print_all_with_input_time(updated_list):
    for package in updated_list:
        this_address = package[address] + ', ' + package[city] + ', ' + package[state] + ', ' + package[zipcode]
        if package[status] == 'Delivered':
            print('Package: ', package[package_id], ' with address: ', this_address, ', has been delivered at: ',
                  package[deliver_time], '.')
        elif package[status] == 'At Hub':
            print('Package: ', package[package_id], ' with address: ',
                  this_address, ', is still at the Hub and will leave at: ', package[leave_time])
        elif package[status] == 'On The Road':
            print('Package: ', package[package_id], ' with address: ', this_address, ', is En Route.')
        else:
            print('there has been an error with the value: ', package)


# this prints one value with the time inputted in consideration. O(n)
def print_one_with_input_time(updated_list, the_package_id):
    for package in updated_list:
        if int(package[package_id]) == int(the_package_id):

            this_address = package[address] + ', ' + package[city] + ', ' + package[state] + ', ' + package[zipcode]
            if package[status] == 'Delivered':
                print('Package: ', package[package_id], ' with address: ', this_address, ', has been delivered at: ',
                      package[deliver_time], '.')
            elif package[status] == 'At Hub':
                print('Package: ', package[package_id], ' with address: ',
                      this_address, ', is still at the Hub and will leave for delivery at: ', package[leave_time])
            elif package[status] == 'On The Road':
                print('Package: ', package[package_id], ' with address: ', this_address, ', is En Route.')
            else:
                print('there has been an error with the value: ', package)

            break


class Main:
    # USE THIS TO TEST TO SEE IF IT WORKS WITH CONSTRAINTS
    # testing_trucks()

    display_welcome()

    exit_num = 1
    while exit_num != 0:
        user_input = input()
        if user_input == 'exit':
            exit_num = 0
            print('ENDING PROGRAM...')
            break
        # TESTING USER INPUT FOR ERRORS
        if (user_input != 'all') and (user_input != 'one') and (user_input != 'test'):
            print('Invalid input... Try again...')

        # # get desired time from user
        # print('\nEnter a time in this format: HH:MM:SS\n')
        # time_for_status = input()

        # using verification function
        if user_input == 'test':
            testing_trucks()

        # print all
        if user_input == 'all':
            # get desired time from user
            print('\nEnter a time in this format: HH:MM:SS\n')
            time_for_status = input()
            print_all_with_input_time(update_list_with_time(time_for_status))

        # print one
        elif user_input == 'one':
            # get desired time from user
            print('\nEnter a time in this format: HH:MM:SS\n')
            time_for_status = input()
            print('\n----  Enter the package ID that you wish to search the status of: \n')
            this_package_id = input()
            print_one_with_input_time(update_list_with_time(time_for_status), this_package_id)
        # restarts so the user can do it again and will reshow commands they can use
        print(
            '\nRESTARTING... '
            '\nPlease enter "all" to see the status of all packages at a certain time. '
            '\nEnter "one" to see the status of one package at a specific time\n')
