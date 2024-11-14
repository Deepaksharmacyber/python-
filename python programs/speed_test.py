#This code uses the speedtest library to measure your internet speed. 
# It performs a download and upload speed test and displays the results 
# in Mbps (megabits per second), along with the ping time. 
# Let’s go over each part of the code:


import speedtest as st   #This line imports the speedtest module and 
                         #gives it an alias (st). This module helps us 
                         #measure download speed, upload speed, and ping.

def Speed_Test():   #This line defines a function called Speed_Test, 
                    #which will run the internet speed test when called.

    test = st.Speedtest() #Here, we create an instance of the Speedtest class
                          #(from the speedtest module). This test object has 
                          # methods to measure download speed, upload speed, and ping.
    
    down_speed = test.download() #This line uses the download method of the test object to measure the download speed in bits per second.
    down_speed = round(down_speed / 10**6 , 2)  #This line converts the download speed from bits per second to megabits per second by dividing 10^6 (1 million). 
                                                #The round function then rounds the result to 2 decimal places.
    print('Download speed in Mbps :',down_speed)
    
    up_speed = test.upload()   #Here, we use the upload method of the test object to measure the upload speed in bits per second.
    up_speed = round(up_speed / 10**6 , 2) #Similar to the download speed, this line converts the upload speed to megabits per second and rounds it to 2 decimal places.
    print('Upload speed in Mbps :',up_speed)
    
    ping = test.results.ping  #This line retrieves the ping result (measured in milliseconds), which is stored in the results property of the test object.
    print("Ping :",ping)

Speed_Test()  #This line calls the Speed_Test function