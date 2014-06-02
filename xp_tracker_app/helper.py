""" Helper functions """

def delta_to_time(timedelta):
    """ Converts datetime.timedelta time in seconds to days, hours, minutes """
    days, seconds = timedelta.days, timedelta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return "{}d {}h {}m {}s".format(days, hours, minutes, seconds)