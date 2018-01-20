#This program is all about reading data, processing it, and then plotting processed results.

import numpy as np
import matplotlib.pyplot as pl

#Read all .csv files into script
monday = np.loadtxt("1_monday.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4))
tuesday = np.loadtxt("2_tuesday.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4))
wednesday = np.loadtxt("3_wednesday.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4))
thursday = np.loadtxt("4_thursday.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4))
friday = np.loadtxt("5_friday.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4))
saturday = np.loadtxt("6_saturday.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4))
sunday = np.loadtxt("7_sunday.csv",delimiter=",",skiprows=1,usecols=(1,2,3,4))


# Empty list created for something to be read in later.
max_temp = [] 
min_temp = []
mean_temp = []


#The max temp of all the days is calculated here and appended to the empty list above
max_temp.append(np.amax(monday[:,0])) 
max_temp.append(np.amax(tuesday[:,0]))
max_temp.append(np.amax(wednesday[:,0]))
max_temp.append(np.amax(thursday[:,0]))
max_temp.append(np.amax(friday[:,0]))
max_temp.append(np.amax(saturday[:,0]))
max_temp.append(np.amax(sunday[:,0]))


#The min temp of all the days is calculated here and appended to the empty list above
min_temp.append(np.amin(monday[:,0]))
min_temp.append(np.amin(tuesday[:,0]))
min_temp.append(np.amin(wednesday[:,0]))
min_temp.append(np.amin(thursday[:,0]))
min_temp.append(np.amin(friday[:,0]))
min_temp.append(np.amin(saturday[:,0]))
min_temp.append(np.amin(sunday[:,0]))


#The average temp of all the days is calculated here and appended to the empty list above
mean_temp.append(np.mean(monday[:,0]))
mean_temp.append(np.mean(tuesday[:,0]))
mean_temp.append(np.mean(wednesday[:,0]))
mean_temp.append(np.mean(thursday[:,0]))
mean_temp.append(np.mean(friday[:,0]))
mean_temp.append(np.mean(saturday[:,0]))
mean_temp.append(np.mean(sunday[:,0]))



#The following part of the code does exactly the same as above, this time only for pressure, wind speed, and heading.
max_pressure = []
min_pressure = []
mean_pressure = []

max_pressure.append(np.amax(monday[:,1]))
max_pressure.append(np.amax(tuesday[:,1]))
max_pressure.append(np.amax(wednesday[:,1]))
max_pressure.append(np.amax(thursday[:,1]))
max_pressure.append(np.amax(friday[:,1]))
max_pressure.append(np.amax(saturday[:,1]))
max_pressure.append(np.amax(sunday[:,1]))

min_pressure.append(np.amin(monday[:,1]))
min_pressure.append(np.amin(tuesday[:,1]))
min_pressure.append(np.amin(wednesday[:,1]))
min_pressure.append(np.amin(thursday[:,1]))
min_pressure.append(np.amin(friday[:,1]))
min_pressure.append(np.amin(saturday[:,1]))
min_pressure.append(np.amin(sunday[:,1]))

mean_pressure.append(np.mean(monday[:,1]))
mean_pressure.append(np.mean(tuesday[:,1]))
mean_pressure.append(np.mean(wednesday[:,1]))
mean_pressure.append(np.mean(thursday[:,1]))
mean_pressure.append(np.mean(friday[:,1]))
mean_pressure.append(np.mean(saturday[:,1]))
mean_pressure.append(np.mean(sunday[:,1]))

max_wind = []
min_wind = []
mean_wind = []

max_wind.append(np.amax(monday[:,2]))
max_wind.append(np.amax(tuesday[:,2]))
max_wind.append(np.amax(wednesday[:,2]))
max_wind.append(np.amax(thursday[:,2]))
max_wind.append(np.amax(friday[:,2]))
max_wind.append(np.amax(saturday[:,2]))
max_wind.append(np.amax(sunday[:,2]))

min_wind.append(np.amin(monday[:,2]))
min_wind.append(np.amin(tuesday[:,2]))
min_wind.append(np.amin(wednesday[:,2]))
min_wind.append(np.amin(thursday[:,2]))
min_wind.append(np.amin(friday[:,2]))
min_wind.append(np.amin(saturday[:,2]))
min_wind.append(np.amin(sunday[:,2]))

mean_wind.append(np.mean(monday[:,2]))
mean_wind.append(np.mean(tuesday[:,2]))
mean_wind.append(np.mean(wednesday[:,2]))
mean_wind.append(np.mean(thursday[:,2]))
mean_wind.append(np.mean(friday[:,2]))
mean_wind.append(np.mean(saturday[:,2]))
mean_wind.append(np.mean(sunday[:,2]))

max_heading = []
min_heading = []
mean_heading = []

max_heading.append(np.amax(monday[:,3]))
max_heading.append(np.amax(tuesday[:,3]))
max_heading.append(np.amax(wednesday[:,3]))
max_heading.append(np.amax(thursday[:,3]))
max_heading.append(np.amax(friday[:,3]))
max_heading.append(np.amax(saturday[:,3]))
max_heading.append(np.amax(sunday[:,3]))

min_heading.append(np.amin(monday[:,3]))
min_heading.append(np.amin(tuesday[:,3]))
min_heading.append(np.amin(wednesday[:,3]))
min_heading.append(np.amin(thursday[:,3]))
min_heading.append(np.amin(friday[:,3]))
min_heading.append(np.amin(saturday[:,3]))
min_heading.append(np.amin(sunday[:,3]))

mean_heading.append(np.mean(monday[:,3]))
mean_heading.append(np.mean(tuesday[:,3]))
mean_heading.append(np.mean(wednesday[:,3]))
mean_heading.append(np.mean(thursday[:,3]))
mean_heading.append(np.mean(friday[:,3]))
mean_heading.append(np.mean(saturday[:,3]))
mean_heading.append(np.mean(sunday[:,3]))


#This is the x-axis of all the plots. It refers to the 7 days of the week.
days = [1,2,3,4,5,6,7]


#The following code is to create the 4 (temp,pressure,windspeed,heading) subplots. 

#Subplot number 1 = Temperature as a functionm of days
pl.subplot(2,2,1)
pl.plot(days,max_temp,"g-")
pl.plot(days,min_temp,"b-")
pl.plot(days,mean_temp,"k-*")
pl.legend(["Max Temp","Min Temp","Avg. Temp"],loc=2)
pl.title("Temperature Info")
pl.xlabel("Week Days")
pl.ylabel("Temperature [${}^o$C]")

#Subplot number 2 = Pressure as a functionm of days
pl.subplot(2,2,2)
pl.plot(days,max_pressure,"g-")
pl.plot(days,min_pressure,"b-")
pl.plot(days,mean_pressure,"k-*")
pl.legend(["Max Pressure","Min Pressure","Avg. Pressure"],loc=2)
pl.title("Pressure Info")
pl.xlabel("Week Days")
pl.ylabel("Pressure [Bar]")

#Subplot number 3 = Wind speed as a functionm of days
pl.subplot(2,2,3)
pl.plot(days,max_wind,"g-")
pl.plot(days,min_wind,"b-")
pl.plot(days,mean_wind,"k-*")
pl.legend(["Max Wind Speed","Min Wind Speed","Avg. Wind Speed"],loc=2)
pl.title("Wind Speed Info")
pl.xlabel("Week Days")
pl.ylabel("Wind Speed [knots]")

#Subplot number 4 = Heading as a functionm of days
pl.subplot(2,2,4)
pl.plot(days,max_heading,"g-")
pl.plot(days,min_heading,"b-")
pl.plot(days,mean_heading,"k-*")
pl.legend(["Max Heading","Min Heading","Avg. Heading"],loc=2)
pl.title("Heading Info")
pl.xlabel("Week Days")
pl.ylabel("Heading [${}^o$ (Degrees)]")


#Shows the plot
pl.show()

