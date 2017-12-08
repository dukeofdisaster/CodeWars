# Our task is to create a function which takes the given
# seconds and converts them to a human readable time
# such as "1 day and 1 hour" or "1 day, 1 hour and 1 second".
# Note the list format is coma seperated except for the last
# phrase.
#
# What sort of things might we need to know? obviously we'll need
# some conversions for seconds to hours/days/years et cetera but what else?
# Specifically we'll need integer division, which is really "floor" division,
# whereas ceiling and floor relate to rounding of numbers to the next highest
# or next lowest whole integer. It's a common subject covered in discrete
# mathematics courses.
#
# We'll use integer division because we are only interested in whole parts o
#
# The novice solution below is super lengthy. If you've ever read Clean Code
# then the length of this method would be a read flag. While this code is
# effective in that it completes the task, it will need to be refactored.

def format_duration(seconds):
    if seconds == 0:
        return "now"
    secondsTotal = seconds
    minute = 60
    hour = 3600 #seconds in an hour
    day = 86400 #seconds in a day
    year = 31536000 #seconds in a year
    yearCount = seconds // year
    secondsTotal -= (yearCount * year)
    yearWord = "year"
    if yearCount > 1:
        yearWord = "years"

    dayCount = secondsTotal // day
    secondsTotal -= (dayCount * day)
    dayWord = "day"
    if dayCount > 1:
        dayWord = "days"

    hourCount = secondsTotal // hour
    secondsTotal -= (hourCount * hour)
    hourWord = "hour"
    if hourCount > 1:
        hourWord = "hours"

    minuteCount = secondsTotal // minute
    secondsTotal -= (minuteCount * minute)
    minuteWord = "minute"
    if minuteCount > 1:
        minuteWord = "minutes"

    secondWord = "second"
    if secondsTotal > 1:
        secondWord = "seconds"

    totalsArray = [yearCount, dayCount, hourCount, minuteCount, secondsTotal]
    wordsArray = [yearWord, dayWord, hourWord, minuteWord, secondWord]
    combined = zip(totalsArray, wordsArray)
    x = len(combined) -1
    while x > -1 :
        if combined[x][0] == 0:
            del combined[x]
        x -= 1
    print(combined)
    finalString = ""
    if len(combined) == 5:
        finalString += (str(combined[0][0])+' '+combined[0][1]+', '+str(combined[1][0])+
        ' '+combined[1][1]+ ', '+ str(combined[2][0])+' '+combined[2][1]+', '+
        str(combined[3][0]) + ' '+  combined[3][1] + ' and ' + str(combined[4][0]) +' '+
         combined[4][1])
    elif len(combined) == 4:
        finalString += (str(combined[0][0])+' '+combined[0][1]+', '+str(combined[1][0])+
        ' ' + combined[1][1]+', '+str(combined[2][0])+' '+combined[2][1]+' and '+
        str(combined[3][0])+' '+combined[3][1])
    elif len(combined) == 3:
        finalString += (str(combined[0][0])+' '+combined[0][1]+', '+str(combined[1][0])+
        ' '+combined[1][1]+' and '+str(combined[2][0])+' '+combined[2][1])
    elif len(combined) == 2:
        finalString += (str(combined[0][0])+' '+combined[0][1]+' and '+str(combined[1][0])+
        ' '+combined[1][1])
    else:
        finalString += str(combined[0][0])+' '+combined[0][1]
    return finalString

print(format_duration(0))

# The expert solution is beloew
times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
