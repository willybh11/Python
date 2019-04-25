from time import gmtime, strftime, sleep
import os

def checkAndUpdate(time, firstloop = False):

	last = time.split(":")[-1]
	time = strftime("%m/%d  |  %H:%M")

	percentage = os.popen("acpi -b | grep -P -o '[0-9]+(?=%)'").read()[:-1]
	# degrees = float(percentage) / 100 * 90

	if (firstloop) or (time.split(":")[-1] != last):
		os.system("""convert -gravity Southeast -pointsize 100 -fill grey40 -font Cantarell-Thin -draw 'text 30,10 "%s" ' ~/Pictures/bg_NMS.jpg ~/Pictures/product.jpg""" %(time))
		os.system("""convert -gravity Southwest -pointsize 100 -fill grey40 -font Cantarell-Thin -draw 'text 30,10 "%s" ' ~/Pictures/product.jpg ~/Pictures/product2.jpg""" %(percentage + "%"))
		# os
		# os.system("""convert -fill '#080c25' -stroke grey40 -draw "ellipse  2560,1520 400,400 %d,%d" ~/Pictures/bg_planets.jpg ~/Pictures/product.jpg""" %(180, 180+degrees))
		# os.system("""convert -gravity Southeast -pointsize 110 -fill grey40 -font Cantarell-Thin -draw ' text 30,100 "%s" ' ~/Pictures/product.jpg ~/Pictures/product2.jpg""" %(time))
		os.system("""gsettings set org.gnome.desktop.background picture-uri "file:///home/willh/Pictures/product2.jpg" """)

	return time
	
time = checkAndUpdate("",True)
last = time
minuteChange = False

while 1:
	time = checkAndUpdate(time)
	if not minuteChange and last != time:
		minuteChange = True
	last = time

	sleep(60) if minuteChange else sleep(1)

# RUN THIS TO RUN IN BACKGROUND
# nohup python bgservice.py &