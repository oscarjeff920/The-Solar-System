def time_converter(seconds, **to_seconds):
    """time converter function either converts seconds into larger denominations
    or it calculates how many seconds in a specified number of years, months, millenia... etc"""
    denominations = dict(universe_age = 4.34548152e+17, 
                         earth_age = 1.749237768e+17, 
                         millennia = 31557600000,
                         centuries = 3155760000, decades = 315576000,
                         years = 31557600, months = 2419200, 
                         weeks = 604800, days = 86400, 
                         hours = 3600, minutes = 60, seconds = 1) 
    
    """to convert seconds into the following denominations fill in only 'seconds' argument. So for 3600 seconds enter,
    time_converter(3600)"""
    if seconds != 0:
        time = {}

        for n in denominations:
            
            if n == "seconds":
                time[n] = round(seconds, 2)
            else:
                seconds /= denominations[n]
                time[n] = int(seconds)
                seconds = denominations[n] * (seconds - time[n])
        return time
    
        """to find the number of seconds in a number of years, months, weeks etc enter '0' in the seconds argument of the function
        then state the quantity of the other denomination, so for 15 years and 2 weeks you would run the function as follows;
        time_converter(0, years = 15, weeks = 2)"""
    else:
        answer = 0
        
        for n in to_seconds:
            for denom in denominations:
                if denom.lower() == n.lower():
                    answer += to_seconds[n] * denominations[denom]
        return answer

