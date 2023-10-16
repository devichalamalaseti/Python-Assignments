'''You are developing a program that analyzes weather data. Write
a Python function that takes a list of temperature readings for a
specific location and determines the average temperature, highest
temperature, and lowest temperature.
Input: temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21'''

def temperature(temp_read):
    Average_temp=sum(temp_read)/len(temp_read)
    highest_temp=max(temp_read)
    lowest_temp=min(temp_read)
    result={f"Average temperature is {Average_temp},highest temperature is {highest_temp},lowest temperature is {lowest_temp}"}
    return result
temp_read = [25, 28, 21, 24, 27]
result=temperature(temp_read)
print(result)