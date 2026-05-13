from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def getTimeZone(city_name):
    geolocator = Nominatim(user_agent="meeting_app")
    location = geolocator.geocode(city_name)

    if location:
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=location.longiude, lat=location.latitude)
        return timezone_str

    return None

def convertToDateTime(date_str, time_str):
    datetime_str = f"{date_str} {time_str}"

    return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

def convertTime(city1, city2, previous_time):
    tz1_name = getTimeZone(city1)
    tz2_name = getTimeZone(city2)

    tz1 = pytz.timezone(tz1_name)
    tz2 = pytz.timezone(tz2_name)

    localized_time = tz1.localize(previous_time)

    new_time = localized_time.astimezone(tz2)

    return new_time