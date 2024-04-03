#File: peter_speeding_fines.py
#Project: CSIS2101 Assignment 3
#Author: Peter Cruz
#History: Version 3.1 January 30, 2023

#The purpose of this program is to define the possible fine for speeding in certain zones.

def peter_speeding_fines():

    #Welcome Greeting for the user
    print("Hello user, if you wish to calculate any possible driving fine please follow the prompts below.")
    
    #Input for the speed limit zone
    speedLimit_zone_cruz = int(input("Please enter the speed limit of the zone: "))

    speed_veh_cruz = int(input("Please enter the speed that the vehicle was travelling: "))

    print("Certain zones have different fine rates: Regular - R, School - S, Workers were present - W, or Housing - H.  If a valid zone is not provided, the zone will be considered a school zone.")
    driv_zone_cruz = input("Please enter the type of zone that the vehicle was ticketed in: ")

    if (speed_veh_cruz - speedLimit_zone_cruz) < 0:
        fine = 0.00
    elif 0 < (speed_veh_cruz - speedLimit_zone_cruz) < 10:
        fine = 49.50
    elif 10 <= (speed_veh_cruz - speedLimit_zone_cruz) < 20:
        fine = 99.00
    elif 20 <= (speed_veh_cruz - speedLimit_zone_cruz) < 30:
        fine = 129.50
    elif 30 <= (speed_veh_cruz - speedLimit_zone_cruz) < 40:
        fine = 199.00
    elif 40<= (speed_veh_cruz - speedLimit_zone_cruz):
        fine = 0.00

    print("Speed Limit:", speedLimit_zone_cruz)
    print("Vehicle Speed:", speed_veh_cruz)
    print("Driving Zone:", driv_zone_cruz)

    if driv_zone_cruz == "R" or driv_zone_cruz == "r":
        print("Total calculated fine: $", fine)
    elif driv_zone_cruz == "H" or driv_zone_cruz == "h":
        print("Total calculated fine: $", (fine * 1.5))
    elif driv_zone_cruz == "W" or driv_zone_cruz == "w":
        print("Total calculated fine: $", (fine * 2))
    elif driv_zone_cruz == "S" or driv_zone_cruz == "s":
        print("Total calculated fine: $", (fine * 3))
    else:
        print("Invalid zone entered.  Setting zone to S.  Total calculated fine: $", (fine * 3))

    if speed_veh_cruz - speedLimit_zone_cruz >= 40:
        print("Court Mandatory - Fine to be decided in court.")
        print("See you in court!")
    elif speed_veh_cruz - speedLimit_zone_cruz >= 30:
        print("You are in the danger zone!")
    elif speed_veh_cruz - speedLimit_zone_cruz >= 20:
        print("You are over speeding!")
    elif speed_veh_cruz - speedLimit_zone_cruz >= 10:
        print("Caution - Reduce Speed!")
    elif speed_veh_cruz - speedLimit_zone_cruz >= 1:
        print("Please slow down!")
    elif speed_veh_cruz - speedLimit_zone_cruz <= 0:
        print("You are a good driver.")

peter_speeding_fines()