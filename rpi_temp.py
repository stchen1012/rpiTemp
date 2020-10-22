import fourletterphat as flp 
import requests
import time

#flp.print_number_str("3.141")
#flp.show()

'''
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

'''

'''
#min temp
temp_min = round(int(data["main"]["temp_min"]), 1)
print(temp_min)

#max temp
temp_max = round(int(data["main"]["temp_max"]), 1)
print(temp_max)
'''

#formatted temp

'''
print("%s F" %(current_temp))
flp.print_number_str("%s F" %(current_temp))
flp.show()
'''

while True:
	flp.clear()
	ploads = {'q': 'Long Island City', 'units': 'imperial', 'appid': 'ae8a8ba77b3d70d40c434468ae4b88eb'}
	r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=ploads)
	data = r.json()
	current_temp = round(int(data["main"]["feels_like"]), 1)
	current_condition = (data["weather"][0]["main"])
	print(current_condition)
	if current_condition in ("Thunderstorm", "Drizzle", "Rain"):
        current_condition = "R"
	elif current_condition == "Clear": #sunny
		current_condition = "S"
	elif current_condition == "Snow":
		current_condition = "S."
	elif current_condition == "Clouds":
		current_condition = "C"
    elif current_condition == "Mist":
        current_condition = "M"
    elif current_condition == "Clouds":
        current_condition = "C"
    elif current_condition in ("Haze", "Fog"):
        current_condition = "H"
    elif current_condition in ("Dust"):
        current_condition = "D"
    elif current_condition in ("Tornado"):
        current_condition = "T"
	else: 
		current condition = "F" #Farenheit default
	#str_current_temp = "%s F" %(current_temp)
	str_current_temp = "%s %s" %(current_temp, current_condition)
	flp.print_number_str(str_current_temp)
	flp.show()
	time.sleep(900)


'''
#Auto start .py file on rPi boot
[Unit]
Description=My service
After=network.target

[Service]
ExecStart=/usr/bin/python3 -u flp.py
WorkingDirectory=/home/pi         
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
'''

'''
#commands to start test service
sudo systemctl start  myscript.service

#stop
sudo systemctl stop test myscript.service

#enable script
sudo systemctl enable  myscript.service

#website
raspberrypi.org/documentation/linux/usage/systemd.md
'''
