#import fourletterphat as flp 
import requests

#flp.print_number_str("3.141")
#flp.show()

#call to openweather API
ploads = {'q': 'Astoria', 'units': 'imperial', 'appid': 'ae8a8ba77b3d70d40c434468ae4b88eb'}
r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=ploads)

#print(r.url)

#sending get request and saving response as response object
data = r.json()
print(data)

#extract feels like temp
current_temp = round(int(data["main"]["feels_like"]), 1)
print(current_temp)

#min temp
temp_min = round(int(data["main"]["temp_min"]), 1)
print(temp_min)

#max temp
temp_max = round(int(data["main"]["temp_max"]), 1)
print(temp_max)


#formatted temp
print("%s F" %(current_temp))
#flp.show("%s F" %(current_temp))
