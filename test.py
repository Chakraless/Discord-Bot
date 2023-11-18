from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Round the seconds to the nearest whole second
rounded_datetime = current_datetime.replace(second=int(round(current_datetime.second)))

# Extract the time from the rounded datetime
rounded_time = rounded_datetime.time()

print("Original Time:", current_datetime.time())
print("Rounded Time:", rounded_time)
