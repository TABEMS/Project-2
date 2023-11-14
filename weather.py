import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    # DEGREE_SYBMOL = "&degC"
    return f"{temp}{DEGREE_SYBMOL}"



def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    d = datetime.fromisoformat(iso_string)
    # print(d)
    
    # print(type(d))
    # <class 'datetime.date'>
    
    converted_data = d.strftime("%A %d %B %Y")
    return converted_data



def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
# temperature in degrees Celsius = (Temperature in degress Fahrenheit -32)*5/9
# temperature in degrees celsius = (temp_in_farenheit-32)*5/9
    resultC = (float(temp_in_farenheit)-32)*5/9
#Add Float
# Round the result to one decimal place
    resultC_round = round(resultC,1)
    return resultC_round
    # Add Float 

# TEST THE FUNCTION
    #print(convert_temp_in_farenheitc(90))

    #pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
# mean = ((sum of list of numbers)/no. in List)
# Result_mean=((sum_of_list)/no_in_list)
# list weather data from test cal mean
# name variables
    sum_of_list=0
    for number in weather_data:
        sum_of_list += float(number)
  # with functions do have spaces      
    no_in_list = len(weather_data)
    result_mean = sum_of_list/no_in_list
    return result_mean



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    #with open(csv_file)
    # mode value from https docs.python.org/3/library/functions.html
    # interact with key arguments
    # import csv
    with open(csv_file, mode="r", encoding="utf-8") as data:
    # creat a csv.reader object to grad the data
        reader = csv.reader(data) 
        next(reader)
    # add list
        new_list=[]
    # loop, convert in list 
    # 2nd 3rd convert to elements
        for example in reader: 
            if not (example):
                continue
            new_list.append([(example[0]), int(example[1]), int(example[2])])
        return new_list        
    # print (example)
    # return the list created
    


def find_min(weather_data):

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    #min_value = float(weather_data[0])
    #min_index= 0S
    #for i in range(1,len(weather_data[i])):
    #current_value = float(weather_data)
    #if current_value<=min_value:
       # min_value = current_value
        #min_index = i
    #return min_value,min_index   
    
     
    # Python to find smallest 
    # number in a list
    # list of numbers
    # list1 = [10, 20, 4, 45, 99]

    # sorting the list
    # list1.sort()
 
    # printing the first element
    #print("Smallest element is:", list1[0])

    if not weather_data:
        return()
    weather_data=[float(x)for x in weather_data]
    min_value = min(weather_data)
    min_index =0
    for index, value in enumerate(weather_data):
        if value == min_value:
            min_index = index
    return (min_value,min_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return()
    # name functions, convert the elements to float
    weather_data = [float(x) for x in weather_data]
    max_value = max(weather_data)
    #float(weather_data[max])
    # maximum value and index
    # max_value = weather_data[0]
    max_index = 0
    # Loop through the list and update the maximum value and index
    for index,value in enumerate(weather_data):
        if value == max_value:
            max_index = index
    return (max_value,max_index)
    # for x in range(1,len(weather_data)):
        # current_value = float(weather_data[x])

        # if current_value >= max_value:
           # max_value = current_value
           # max_index = x
           # return max_value, max_index



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # if not weather_data:
    #     return "no weather data available"
    
    summary =""
    min_temperture=[]
    max_temperature=[]

    for day in weather_data:
        if not (day):
            continue
        #list and append (function)
        min_temperture.append(day[1])
        max_temperature.append(day[2])
    min_average = format_temperature (convert_f_to_c (calculate_mean(min_temperture)))
    max_average = format_temperature (convert_f_to_c (calculate_mean(max_temperature)))
    min_temp = min(min_temperture)
    max_temp = max(max_temperature)
    min_date=None
    max_date=None

    for date in weather_data:
        if not (date):
            continue
        if date[1] == min_temp:
            min_date = convert_date(date[0])
    for date in weather_data:
        if not (date):
            continue
        if date[2] == max_temp:
            max_date = convert_date(date[0])

    no_in_list = len(weather_data)

    summary = (f"{no_in_list} Day Overview\n"
              f"  The lowest temperature will be {format_temperature (convert_f_to_c(min_temp))}, and will occur on {min_date}.\n"
              f"  The highest temperature will be {format_temperature (convert_f_to_c(max_temp))}, and will occur on {max_date}.\n"
              f"  The average low this week is {min_average}.\n"
              f"  The average high this week is {max_average}.\n")
    return summary
            

        #min_temperture = format_temperature (convert_f_to_c(day[1]))
        #max_temperature = format_temperature(convert_f_to_c(day[2]))
        #average_low = []
        #verage_high = []
        #summary +=f"---- Minimum Temperture: {min_temperture},{date} \n Maximum Temperature: {max_temperature},{date}\n average low temperature: {average_low}"


def generate_daily_summary(weather_data):

    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    if not weather_data:
        return "No weather data available."
    
    summary = ""

    for day in weather_data:
        date = convert_date (day[0])
        min_temperature = format_temperature (convert_f_to_c(day[1]))
        max_temperature = format_temperature (convert_f_to_c(day[2]))
        summary += f"---- {date} ----\n  Minimum Temperature: {min_temperature}\n  Maximum Temperature: {max_temperature}\n\n"
    return summary

