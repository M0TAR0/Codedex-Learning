# Function that returns the correct emoji for an introduced moon phase or an error message

def moon_phase(phase):
    if phase == "New Moon":
        return "🌑"
    elif phase == "Waxing crescent":
        return "🌒"
    elif phase == "First Quarter":
        return "🌓"
    elif phase == "Waxing Gibbous":
        return "🌔"
    elif phase == "Full Moon":
        return "🌕"
    elif phase == "Waning Gibbous":
        return "🌖"
    elif phase == "Last Quarter":
        return "🌗"
    elif phase == "Wanning Crescent":
        return "🌘"
    else:
        return "Invalid moon phase"
    
answer = moon_phase('New Moon')
print(answer)  

# Output: 🌑