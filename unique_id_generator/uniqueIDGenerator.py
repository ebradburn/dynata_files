# Last updated 25 June 2019, to enable unique link creation

import random

#####################################################################################
# OUTPUT FILES
# - output1 is a list of the unique IDs.  Use this with "authentication by file" 
#   in Decipher to only allow values from the generated list into your survey.
#   Output file size will be approximately 1 MB for every 12,500 IDs.
# - output2 is the same list, but with a prefix (defined below as prefix) 
#   appended to it.  Use this with a survey URL and variable to create unique links.
# - All output files will be generated in the same folder as this script.  If any
#   of them already exist, they will be overwritten.
#####################################################################################
output1 = open("uids.txt", "w")
output2 = open("unique links.txt", "w")
#####################################################################################

#####################################################################################
# OTHER SETTINGS
# - Test IDs start at 100000001 and are sequential.
# - Actual IDs start at 100000001 + number of test IDs and are random.
# - The same ID will not be generated more than once.
#####################################################################################
numTestIDsNeeded = 0
numActualIDsNeeded = 20
prefix = "https://survey-d.researchnow.com/survey/selfserve/53b/1907476?id="
#####################################################################################

if numTestIDsNeeded > 0:
	for i in range(0, numTestIDsNeeded):
		output2.write(prefix + str(100000001 + i) + "\n")
		output1.write(str(100000001 + i) + "\n")

myRange = xrange(100000001 + numTestIDsNeeded, 999999999)

mySample = random.sample(myRange, numActualIDsNeeded)

for i in mySample:
	output2.write(prefix + str(i) + "\n")
	output1.write(str(i) + "\n")
	