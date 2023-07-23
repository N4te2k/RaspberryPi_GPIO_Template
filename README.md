# RaspberryPi_GPIO_Template

`https://electreeks.de/project/python-gpio-befehle-raspberry-pi/`

## Raspberry Pi OS auf SD-Karte
```https://downloads.raspberrypi.org/imager/imager_latest.exe
https://imgur.com/mOwtRMF
https://imgur.com/u0b1MSB
https://imgur.com/DzVohgF```

## Set up
`https://imgur.com/GDsC3Yt`
`https://imgur.com/ar2ZVjn`
```
pip install aiogram
```
```
# Create a bot instance
bot = Bot(token='Your token goes here')
```
```
# Add group id here
group_id = -123
```

## How to run
When using Raspberry Pi OS Desktop:
- launch your raspberry pi
- set up raspberry pi
- open thonny on raspberry pi
- copy paste the code from github
- install aiogram
- enter your token and group id
- either run in thonny or create cronjob for your saved python file to make sure it runs again after any kind of reboot
