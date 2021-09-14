def irange(start, stop, step=1):            # This is an inclusive range function, so that I don't have to remember
    if step == 1:                           # that range() leaves out the last value. 
        return range(start, stop+1)         #
    elif step < 0:                          #
        return range(start, stop-1, step)   #
    else:                                   #
        return range(start, stop+1, step)   #

def indeces(somelist):              #returns a list of numbers from 0 to len(somelist), so I can easily iterate with
    return range(len(somelist))     #  reference to the index of each element in the list

def numlen(somenumber):
    return len(str(somenumber))     #returns the number of characters in a number, for formatting purposes

def nicestring(stringinput):
    stringinput=stringinput.lower() #puts the string in all lowercase
    stringinput=stringinput.strip() #removes whitespace from the string
    stringinput=stringinput.translate(None, string.punctuation) #removes all punctuation from the string
    return stringinput
