monthConversions = {
    1: 'January',
    2: 'February',
    3: 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}
# invalid input will throw an error
print(monthConversions['Aug'])
# invalid input will return NONE
print(monthConversions.get(2))
