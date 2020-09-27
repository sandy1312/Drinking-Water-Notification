import time
from plyer import notification #For desktop notification we use plyer import function.
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**Please drink water!!",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men.About 11.5 cups (2.7 liters) of fluids a day for women",
            timeout = 10, #For 10 second it will appear on screen
            app_icon = "E:\Python\Glass-Water.ico" #Drinking icon image
        )
        time.sleep(60*60) #After every 3600 second it will remind
