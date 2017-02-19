
#Sorry for the delay in submitting this, Jeff! 
#This little program takes .txt files from an actual MTurk experiment (N.B.: I have IRB approval to share such data on online repositories), 
#renames them with random numbers to conceal the MTurk workers' IP addresses contained in the text file, 
#and spits out a log of the IP-random number pairs for record keeping.
#It may not be the most optimal way to do this, but I think it works.

#from os import listdir, rename
import re, random, glob, os 


#Change directory as needed
os.chdir("/Users/alexia/Desktop/cogs202shared/Regular_expressions/") 

#Generate 100 random numbers (= number of participants here) to use for renaming
randomnumbers = random.sample(range(1, 1000), 100)  

#Initiate a list to log the IP-random number pairs 
log = []

for fl in glob.glob("*.txt"): #Select only .txt files in this folder (ignore this .py file) 
	select_number = random.sample(randomnumbers,1) #selecting a random number from the 100 above
	numberstring = str(select_number) #converting to a string
	newname = numberstring + '.txt' #I imagine I must find a way to unnest these list items
	os.rename(fl, newname) #renaming files with random number. Don't worry about overwriting the file names! Data are backed up! 

	#Now we want to log these changes
	regex = r"((?:\d{1,3}\.){3}\d{1,3})" #This pattern captures the IP format. I realize that there are easier ways to capture it!
	IP = re.findall(regex, fl)
	log += [[IP, numberstring]]


#Opening a textfile to save these changes
logfile = open('Exp1_renaming_log.txt', 'w') 
for pair in log:
	logfile.write("%s\n" % pair) #not the prettiest output (still troubled by quotation marks and square brackets), but good enough for now!



