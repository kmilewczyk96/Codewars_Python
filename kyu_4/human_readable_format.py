########################################################################################################################
# Your task in order to complete this Kata is to write a function which formats a duration,
# given as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#   format_duration(62)    # returns "1 minute and 2 seconds"
#   format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
#
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
#
# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc.
# In general, a positive integer and one of the valid units of time, separated by a space.
# The unit of time is used in plural if the integer is greater than 1.
# The components are separated by a comma and a space (", ").
# Except the last component, which is separated by " and ", just like it would be written in English.
# A more significant units of time will occur before than a least significant one.
# Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
# A component will not appear at all if its value happens to be zero.
# Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
# A unit of time must be used "as much as possible".
# It means that the function should not return 61 seconds, but 1 minute and 1 second instead.
# Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
########################################################################################################################
def format_duration(seconds):
    if seconds:
        result = []

        years = seconds // 31536000
        seconds -= years * 31536000
        days = seconds // 86400
        seconds -= days * 86400
        hours = seconds // 3600
        seconds -= hours * 3600
        minutes = seconds // 60
        seconds -= minutes * 60

        time_ = {
            0: 'year',
            1: 'day',
            2: 'hour',
            3: 'minute',
            4: 'second'
        }

        formatted = [years, days, hours, minutes, seconds]
        for pos, val in enumerate(formatted):
            if val > 1:
                result.append(f'{val} {time_[pos]}s')
                continue
            if val == 1:
                result.append(f'{val} {time_[pos]}')

        if len(result) > 1:
            return ', '.join(result[:-1]) + f' and {result[-1]}'

        return result[0]

    return 'now'


if __name__ == '__main__':
    print(format_duration(0),
          format_duration(12),
          format_duration(61),
          format_duration(3601),
          format_duration(122313121),
          sep='\n')
