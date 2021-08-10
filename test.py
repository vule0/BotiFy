# import re
# volume = 12.5
# string = "--progress-bar-transform:{}%;".format(volume)




# # found = re.search('orm:%;', string).group(1)
# # print(found)
# def truncate(n, decimals=0):
#     multiplier = 10 ** decimals
#     return int(n * multiplier) / multiplier

# extracts the volume (as int) from the html string provided
# start = string.find('orm:') + len('orm:')
# end = string.find('%;')
# substring = int(string[start:end])

# setting up range for volume because we cant get the exact volume 
volume = 15
upper_range = volume + 6
lower_range = volume - 4

error = range(lower_range, upper_range)
print(list(error))