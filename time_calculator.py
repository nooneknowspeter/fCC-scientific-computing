def convert_time_24_format(*, hours, period: str = "PM", convert_to_24: bool = True):
    hours_int = int(hours) if not isinstance(hours, int) else hours

    if convert_to_24:
        if period == "PM" and hours_int != 12:
            return hours_int + 12
        elif period == "AM" and hours_int == 12:
            return 0
        return hours_int
    else:
        if hours_int == 0:
            return 12
        elif hours_int > 12:
            return hours_int - 12
        return hours_int


def add_time(start, duration, day=""):
    days_of_the_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    # parse start time
    start_parts = start.split()
    time_parts = start_parts[0].split(":")
    start_hour, start_minute = int(time_parts[0]), int(time_parts[1])
    start_period = start_parts[1]

    # convert start time to 24-hour format
    start_hour_24 = convert_time_24_format(hours=start_hour, period=start_period)

    # parse duration time
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # calculate new time
    total_minutes = start_minute + duration_minutes
    extra_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    total_hours = start_hour_24 + duration_hours + extra_hours
    days_later = total_hours // 24
    new_hour_24 = total_hours % 24

    # determine new period (am/pm) and convert back to 12-hour format
    new_period = "AM" if new_hour_24 < 12 else "PM"
    new_hour_12 = convert_time_24_format(hours=new_hour_24, convert_to_24=False)

    # format minutes correctly (e.g., '07' instead of '7')
    new_minutes = f"{new_minutes:02}"

    # determine the day of the week (if provided)
    new_day = ""
    if day:
        day_index = days_of_the_week.index(day.capitalize())
        new_day = days_of_the_week[(day_index + days_later) % 7]

    # construct final result string
    result = f"{new_hour_12}:{new_minutes} {new_period}"

    if new_day:
        result += f", {new_day}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result


# test cases
if __name__ == "__main__":
    current_time = "8:16 PM"
    duration = "466:02"
    day = "tuesday"

    print(add_time(start=current_time, duration=duration, day=day))
