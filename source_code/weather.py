import weather_functions
import terminal_alignment
import datetime
import time
       

terminal_alignment.clear_terminal()

temp_unit_name = "metric" #default value
temp_unit = "°C"          #default value
current_datetime = datetime.datetime.now()
current_time = current_datetime.strftime("%H:%S %p\n%A")
# current_day = current_datetime.strftime

try:
    # loop to stop program from termination+
    while True:
            terminal_alignment.print_center(f"WEATHER SHELL\nversion\n1.1.1\n") # heading

            # main menu starts here
            print("\nMain Menu\n-------\n|1| Quick search\n|2| Weather forecast\n|3| AQI index\n|4| Change unit system\n|0| Exit or Back\n")
            user_choice = input(terminal_alignment.center_input("> "))
            location = ""
            # weather search
            if user_choice == 1 or user_choice == "1":        
                while True:
                        terminal_alignment.print_center(f"\nQuick weather search: ")
                        location = str(input(terminal_alignment.center_input("(City/Town)> ")))
                        temperature, weather, max_temp, min_temp, feels_like, humidity, pressure = weather_functions.weather_info(location, temp_unit_name)
                        try:
                            if temperature and weather and max_temp and min_temp and feels_like and humidity and pressure:
                                terminal_alignment.print_center("_" * 10)
                                terminal_alignment.print_center(f"\n{current_time}\n\n{location.capitalize()}\n{format(temperature, ".1f")}{temp_unit}\n{weather}\n")
                                more = input(terminal_alignment.center_input("More(y/n)> "))
                                if more.upper() == "Y":
                                    terminal_alignment.print_center(f"{format(max_temp, ".1f")}{temp_unit} max / {format(min_temp, ".1f")}{temp_unit} min\nFeels like {format(feels_like, ".1f")}{temp_unit}")
                                    terminal_alignment.print_center(f"Humidity: {humidity}%\nPressure: {pressure} mb")
                                    terminal_alignment.print_center("_" * 10)
                                else:
                                    terminal_alignment.print_center("_" * 10)
                                
                            elif location == "":
                                terminal_alignment.print_center(f"Enter location name.\n")
                            elif location == 0 or location == "0":
                                terminal_alignment.clear_terminal()
                                break
                            else:
                                terminal_alignment.print_center("_" * 10)
                                terminal_alignment.print_center(f"No results found for {location}.")
                
                        except Exception as e:
                            print(f"An error occurred: {e}")
            
            #forecast search
            elif user_choice == 2 or user_choice == "2":
                while True:
                        terminal_alignment.print_center(f"\nSearch Forecast: ")
                        location = str(input(terminal_alignment.center_input("(City/Town)> ")))

                        if location == "":
                            terminal_alignment.print_center(f"Enter location name.\n")
                        elif location == 0 or location == "0":
                            terminal_alignment.clear_terminal()
                            break
                        else:
                            try:
                                forecast = weather_functions.forecast_info(location, temp_unit_name) # prints forecast table also
                            except:
                                terminal_alignment.print_center(f"\nNo results found.")
                                
                            
            # aqi finder
            elif user_choice == 3 or user_choice == "3":
                while True:
                        terminal_alignment.print_center(f"\nSearch AQI ")
                        location = str(input(terminal_alignment.center_input("(City/Town)> "))) 
                        aqi = weather_functions.fetch_aqi(location)
                        if aqi:
                             terminal_alignment.print_center(f"{aqi} AQI\n{location}")
                        elif location == 0 or location == "0":
                            terminal_alignment.clear_terminal()
                            break
                        else:
                             terminal_alignment.print_center("\nNo results found.")          
            
            # unit system change 
            elif user_choice == 4 or user_choice == "4": 
                terminal_alignment.print_center(f"Current unit system: {temp_unit_name}")
                while True:
                    try:
                        temp_unit = input(terminal_alignment.center_input("Change unit system: ")).capitalize()
                        if temp_unit == "F" or temp_unit == "Imperial":
                            temp_unit_name = "imperial" # case sensitive
                            temp_unit = "°F"
                            terminal_alignment.print_center(f"Units changed to {temp_unit_name}.")
                            time.sleep(1)
                            terminal_alignment.clear_terminal()
                            break
                        elif temp_unit == "C" or temp_unit == "Metric":
                            temp_unit_name = "metric" # case sensitive
                            temp_unit = "°C"
                            terminal_alignment.print_center(f"Units changed to {temp_unit_name}")
                            time.sleep(1.5)
                            terminal_alignment.clear_terminal()
                            break
                        elif temp_unit == "K" or temp_unit == "Kelvin" or temp_unit == "Standard":
                            temp_unit_name = "standard" # case sensitive
                            temp_unit = "K"
                            terminal_alignment.print_center(f"Units changed to {temp_unit_name}")
                            time.sleep(1)
                            terminal_alignment.clear_terminal()
                            break
                        elif temp_unit == "":
                            break
                        else:
                            terminal_alignment.print_center(f"Enter valid SI unit.")
                    
                    except Exception as e:
                        print(e)
                        break 
            
            #exit program
            elif user_choice == "0" or user_choice == 0:
                terminal_alignment.clear_terminal()
                print("Weather Shell ended.")
                break
            
            else:
                terminal_alignment.print_center(f"Type valid option.")
                time.sleep(1)  
                terminal_alignment.clear_terminal()                           
except KeyboardInterrupt:
    print("\nProgram ended by user.\n")
    
