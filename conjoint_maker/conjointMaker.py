try:
	import sys
	import traceback
	
	# ED'S CONJOINT MAKER
	
	print("Welcome to the conjoint maker!")
	print("PLEASE STUDY YOUR DESIGN FILES AND REFERENCE MATERIALS CAREFULLY BEFORE USING THIS SCRIPT!")
	
	print("")
	numberOfConjoints_raw = ""
	numberOfConjoints = 0
	while( not(numberOfConjoints_raw.lstrip("-").isdigit()) ):
		print("How many conjoints does your project have?")
		numberOfConjoints_raw = input("")
	numberOfConjoints = int(numberOfConjoints_raw)
	
	if numberOfConjoints == 0:
		print("Then why are you here?  (Press enter to exit.)")
		input("")
		sys.exit()
	elif numberOfConjoints < 0:
		print("Yeah, okay.  (Press enter to exit.)")
		input("")
		sys.exit()
#	elif numberOfConjoints != 1:
#		print("Sorry, at this point the program only supports one conjoint per project.  (Press enter to exit.)")
#		input("")
#		sys.exit()
	
	if numberOfConjoints >= 5:
		print("")
		print("If that is really true, then we feel really bad for you.  Go grab a drink, we're gonna be here a while.")	
		print("")
		
	if numberOfConjoints > 1:
		conjointNames = []
		print("The program needs unique names for each conjoint in order to identify each of them.  Please provide them below.")
		print("We strongly recommend you use only capital letters/underscores and that you keep each name as short as possible.")
		print("")
		i = 0
		while i < numberOfConjoints:
			print("Please enter the unique name for conjoint %d:" % (i+1))
			thisConjointName = input("")
			if thisConjointName == "" or thisConjointName[0].isdigit():
				print("Invalid name.")
				i -= 1
			elif thisConjointName in conjointNames:
				print("This name is already used.")
				i -= 1
			else:
				conjointNames.append(thisConjointName)
			i += 1
	elif numberOfConjoints == 1:
		conjointNames = [""]
	
	for conjointIndex in range(numberOfConjoints):
		print("==============================================================")	
		print("NOW STARTING CONJOINT %s" % (conjointNames[conjointIndex]))	
		print("==============================================================")	
		print("")	
		input("Move your design file, named \"design%s.dat\", into the same folder as this script and press enter." % conjointNames[conjointIndex])
		
		designFile = open("design%s.dat" % (conjointNames[conjointIndex]), "r")
		outputFile = open("conjoint.xml", "w" if conjointIndex == 0 else "a")
		
		isFirstLine = True
		
		columnHeaders = []
		
		numCols = 0
		numVersions = 0
		numTasks = 0
		numConcepts = 0
		numAttributes = 0
		minValuesPerAttribute = []
		maxValuesPerAttribute = []
		attributeNames = []
		
		print("Searching file...")
		
		# Search the file for the number of versions, tasks, concepts, attributes
		for eachLine in designFile:
			
			splitLine = eachLine.split("\t")
			
			if isFirstLine:
				columnHeaders = splitLine
				numCols = len(columnHeaders)
				numAttributes = numCols - 3
				
				if numAttributes < 1:
					input("File needs at at least one attribute column.  Press enter to quit.")
					sys.exit()
				else:
					minValuesPerAttribute = [999999999999] * numAttributes
					maxValuesPerAttribute = [-1] * numAttributes
					isFirstLine = False
					continue
					
			
			currentVersion = int(splitLine[0])
			currentTask = int(splitLine[1])
			currentConcept = int(splitLine[2])
			currentAttributeValues = [int(splitLine[i]) for i in range(3, len(splitLine))]
			
			if currentVersion > numVersions:
				numVersions = currentVersion
			if currentTask > numTasks:
				numTasks = currentTask
			if currentConcept > numConcepts:
				numConcepts = currentConcept
				
			for i in range(len(currentAttributeValues)):
				if currentAttributeValues[i] > maxValuesPerAttribute[i]:
					maxValuesPerAttribute[i] = currentAttributeValues[i]
				if currentAttributeValues[i] < minValuesPerAttribute[i]:
					minValuesPerAttribute[i] = currentAttributeValues[i]
					
		designFile.close()
		
		print("")
		print("%d versions, %d tasks, %d concepts, %d attributes found." % (numVersions, numTasks, numConcepts, numAttributes))
		print("")
		
		print("If you have a tab-delimited text file that contains the attribute names and texts, please move it to this folder.")
		print("Then enter its filename and hit enter.  Check the program documentation for info on how this file should be formatted.")
		print("If you don't have one, leave this blank and you can enter the text manually.")
		nameFilename = input("")
		enterManually = False
		
		attributeNames = ["" for i in range(numAttributes)]
		
		if nameFilename == "":
			print("\nEnter the texts manually.\n")
			enterManually = True
		else:
			try:
				nameFile = open(nameFilename, "r")
				currentLine = 0
				attributeTexts = [ [""] * (1 + maxValuesPerAttribute[i]) for i in range(numAttributes) ]
				
				for eachLine in nameFile:
				
					# Strip â€‹ from input
					eachLine = eachLine.replace("â€‹", "")
					
					# Escape & / < / >
					eachLine = eachLine.replace("&", "&amp;")
					eachLine = eachLine.replace("<", "&lt;")
					eachLine = eachLine.replace(">", "&gt;")
				
					if currentLine == 0:
						splitLine = eachLine.split("\t")
						for i in range(numAttributes):
							attributeNames[i] = splitLine[i+1].strip()
					else:
						splitLine = eachLine.split("\t")
						for i in range(numAttributes):
							if splitLine[i+1].strip() != "":
								attributeTexts[i][currentLine] = splitLine[i+1].strip()
					currentLine += 1
				
				nameFile.close()
			
				print("")
				print("Here are the attributes the program has found:")
				print("")
						
				for i in range(numAttributes):
					print("Attribute %d: %s" % (i+1, attributeNames[i]))
					for j in range(len(attributeTexts[i])):
						print("\tValue %d: %s" % (j, attributeTexts[i][j]))
						
				print("")
				print("Does this look right? (y/n)")
				response = input("")
				if len(response) == 0 or response[0].lower() != "y":
					print("All righty then, enter the texts manually.")
					print("")
					enterManually = True
			
			except Exception:
				enterManually = True
				print(traceback.format_exc())
				print("\nAn error occurred while reading the file or the file was not found.  Enter the texts manually.\n")
		
		if enterManually:
			for i in range(numAttributes):
				print("Enter the name of attribute %d:" % (i+1))
				attributeNames[i] = input("")
				attributeNames[i] = attributeNames[i].replace("&", "&amp;")
				attributeNames[i] = attributeNames[i].replace("<", "&lt;")
				attributeNames[i] = attributeNames[i].replace(">", "&gt;")
			
			attributeTexts = [ [""] * (1 + maxValuesPerAttribute[i]) for i in range(numAttributes) ]
			for i in range(len(attributeTexts)):
				
				print("")
				print("Design file values for attribute %d (%s) range from %d to %d." % (i+1, attributeNames[i], minValuesPerAttribute[i], maxValuesPerAttribute[i]))
				print("")
				
				for j in range(minValuesPerAttribute[i], maxValuesPerAttribute[i] + 1):
					print("Enter the text for option %d for attribute %d \"%s\" (leave blank if there is none):" % (j, i+1, attributeNames[i]))
					attributeTexts[i][j] = input("")
					attributeTexts[i][j] = attributeTexts[i][j].replace("&", "&amp;")
					attributeTexts[i][j] = attributeTexts[i][j].replace("<", "&lt;")
					attributeTexts[i][j] = attributeTexts[i][j].replace(">", "&gt;")
		
		
		print("")
		print("Now generating conjoint code...")
		print("")
					
		# Generate output
		outputString = ""
		
		# 1: res tags
		resTagString = "["
		for i in range(len(attributeTexts)):
			resTagString += "["
			for j in range(len(attributeTexts[i])):
				outputString += ("<res label=\"cj%s_att%d_%d\">%s</res>\n" % (conjointNames[conjointIndex], i+1, j, attributeTexts[i][j].strip()))
				resReference = "res.cj%s_att%d_%d" % (conjointNames[conjointIndex], i+1, j)	
				resTagString += resReference
				if j < len(attributeTexts[i]) - 1:
					resTagString += ", "
				else:
					resTagString += "]"
			if i < len(attributeTexts) - 1:
				resTagString += ", "
			else:
				resTagString += "]"
		
		# 2: exec when init block
		outputString += "\n"
		outputString += "<exec when=\"init\">\n"
		outputString += "# =======================================\n"
		outputString += "# INITIALIZE CONJOINT %s\n" % conjointNames[conjointIndex]
		outputString += "# =======================================\n"
		outputString += ("numVersions%s = %d\n" % (conjointNames[conjointIndex], numVersions))
		outputString += ("numTasksPerVersion%s = %d\n" % (conjointNames[conjointIndex], numTasks))
		outputString += ("numConceptsPerTask%s = %d\n" % (conjointNames[conjointIndex], numConcepts))
		outputString += ("numAttributesPerConcept%s = %d\n" % (conjointNames[conjointIndex], numAttributes))
		outputString += "totalSlots%s = numVersions%s * numTasksPerVersion%s * numConceptsPerTask%s * numAttributesPerConcept%s\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "designData%s = [0] * totalSlots%s\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "inputFile%s = open(\"design%s.dat\", \"r\")\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "isFirstLine = True\n"
		outputString += "for eachLine in inputFile%s:\n" % conjointNames[conjointIndex]
		outputString += "\n"
		outputString += "\tif isFirstLine:\n"
		outputString += "\t\tisFirstLine = False\n"
		outputString += "\t\tcontinue\n"
		outputString += "\t\n"
		outputString += "\t# Split each line by tabs\n"
		outputString += "\t# 0: version, 1: task, 2: concept, 3: att1, 4: att2, 5: att3...\n"
		outputString += "\tsplitLine = eachLine.split(\"\\t\")\n"
		outputString += "\t\n"
		outputString += "\tcurrentVersion = int(splitLine[0]) - 1\n"
		outputString += "\tcurrentTask = int(splitLine[1]) - 1\n"
		outputString += "\tcurrentConcept = int(splitLine[2]) - 1\n"
		outputString += "\t\n"
		outputString += "\tbaseArrayIndex = (currentVersion * numTasksPerVersion%s * numConceptsPerTask%s * numAttributesPerConcept%s) + (currentTask * numConceptsPerTask%s * numAttributesPerConcept%s) + (currentConcept * numAttributesPerConcept%s)\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\t\n"
		outputString += "\tfor i in range(numAttributesPerConcept%s):\n" % conjointNames[conjointIndex]
		outputString += "\t\tdesignData%s[baseArrayIndex + i] = int(splitLine[3 + i])\n" % conjointNames[conjointIndex]
		outputString += "\n"
		outputString += "inputFile%s.close()\n" % conjointNames[conjointIndex]
		outputString += "\n"
		outputString += "def getAttribute%s(version, task, concept, attribute):\n" % conjointNames[conjointIndex]
		outputString += "\treturn designData%s[((version - 1) * numTasksPerVersion%s * numConceptsPerTask%s * numAttributesPerConcept%s) + ((task - 1) * numConceptsPerTask%s * numAttributesPerConcept%s) + ((concept - 1) * numAttributesPerConcept%s) + (attribute - 1)]\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex],conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\t\n"
		outputString += "def getAttributeList%s(version, task, concept):\n" % conjointNames[conjointIndex]
		outputString += "\tbaseArrayIndex = ((version - 1) * numTasksPerVersion%s * numConceptsPerTask%s * numAttributesPerConcept%s) + ((task - 1) * numConceptsPerTask%s * numAttributesPerConcept%s) + ((concept - 1) * numAttributesPerConcept%s)\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\treturnArray = []\n"
		outputString += "\tfor i in range(baseArrayIndex, baseArrayIndex + numAttributesPerConcept%s):\n" % conjointNames[conjointIndex]
		outputString += "\t\treturnArray.append(designData%s[i])\n" % conjointNames[conjointIndex]
		outputString += "\treturn returnArray\n"
		outputString += "\t\n"
		outputString += "def getTextAttribute%s(type, attribute):\n" % conjointNames[conjointIndex]
		outputString += ("\tallData%s = %s\n" % (conjointNames[conjointIndex], resTagString))
		outputString += "\t\n"
		outputString += "\treturn allData%s[type][attribute]\n" % conjointNames[conjointIndex]
		outputString += "</exec>\n"
		outputString += "\n"
		
		# 3: Conjoint block
		outputString += "<block label=\"CONJOINT%s_BLOCK\">\n" % conjointNames[conjointIndex]
		outputString += "  <quota label=\"quota_ConjointVersion%s\" overquota=\"noqual\" sheet=\"ConjointVersion%s\"/>\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "  <suspend/>\n"
		outputString += "\n"
		outputString += "  <number \n"
		outputString += "    label=\"HP_versionNumber%s\"\n" % conjointNames[conjointIndex]
		outputString += "    size=\"3\"\n"
		outputString += "    where=\"execute,survey,report\">\n"
		outputString += "      <title>Hidden Question. %s Version Number</title>\n" % conjointNames[conjointIndex]
		outputString += "    <exec>\n"
		outputString += "for i in range(1, numVersions%s + 1):\n" % conjointNames[conjointIndex]
		outputString += ("\tif hasMarker(\"/ConjointVersion" + conjointNames[conjointIndex] + "/cj" + conjointNames[conjointIndex] + "ver_\" + str(i)):\n")
		outputString += "\t\tHP_versionNumber%s.val = i\n" % conjointNames[conjointIndex]
		outputString += "\t\tbreak\n"
		outputString += "\t\t</exec>\n"
		outputString += "\n"
		outputString += "  </number>\n"
		outputString += "\n"
		outputString += "  <suspend/>\n"
		outputString += "\n"
		
		outputString += "  <loop label=\"cjLoop%s\" vars=\"task\">\n" % conjointNames[conjointIndex]
		outputString += "    <block label=\"cjBlock%s\">\n" % conjointNames[conjointIndex]
		outputString += "      <radio \n"
		outputString += "     label=\"CJEXERCISE%s_[loopvar: task]\"\n" % conjointNames[conjointIndex]
		outputString += "     surveyDisplay=\"desktop\">\n"
		outputString += "        <title>ENTER YOUR CONJOINT QUESTION TEXT HERE</title>\n"
		
		conceptColumnList = ["'c%d'" % (i+1) for i in range(numConcepts)]
		conceptColumnString = ", ".join(conceptColumnList)
		
		# Style blocks
		for i in range(numAttributes):
			outputString += "<style label=\"replaceElements%s%d\" cond=\"col.label in [%s]\" name=\"question.element\" rows=\"a%d\"><![CDATA[\n" % (conjointNames[conjointIndex], i+1, conceptColumnString, i+1)
			outputString += "<td style=\"vertical-align:middle;background-color:white\" headers=\"${ec.this.label + \"_\" + ec.col.label if ec.col.label else \"\"}\" class=\"cell nonempty legend col-legend col-legend-left col-legend-basic legend-level-1\"  $(extra)>\n"
			outputString += "${getTextAttribute%s(%d, getAttribute%s(HP_versionNumber%s.val, [loopvar: task], col.index + 1, %d))}</td>\n" % (conjointNames[conjointIndex], i, conjointNames[conjointIndex], conjointNames[conjointIndex], i+1)
			outputString += "]]></style>\n"
		
		# Cols
		for i in range(numConcepts):
			outputString += "        <col label=\"c%d\"><b>Option %d</b></col>\n" % (i+1, i+1)
			
		# Rows
		for i in range(numAttributes):
			outputString += "        <row label=\"a%d\" optional=\"1\"><b>%s</b></row>\n" % (i+1, attributeNames[i])
		
		outputString += "        <row label=\"r1\"/>\n"
		outputString += "      </radio>\n"
		outputString += "\n"	
		outputString += "    </block>\n"
		
		# Looprows
		for i in range(numTasks):
			outputString += "    <looprow label=\"%d\">\n" % (i+1)
			outputString += "	  <loopvar name=\"task\">%d</loopvar>\n" % (i+1)
			outputString += "    </looprow>\n"
			outputString += "\n"
			
		outputString += "  </loop>\n"
		outputString += "\n"
		outputString += "</block>\n"
		outputString += "\n"
		outputString += "<suspend/>\n"
		outputString += "\n"
		outputString += "\n"
		
		outputFile.write(outputString)
		outputFile.close()
		
		definesFile = open("quotaDefines.txt", "w" if conjointIndex == 0 else "a")
		for i in range(numVersions):
			definesFile.write("cj%sver_%d\tplus\tVersion %d\n" % (conjointNames[conjointIndex], i+1, i+1))
		definesFile.close()
		
		conjointQuotaFile = open("quotaConjoint%s.txt" % conjointNames[conjointIndex], "w") 
		conjointQuotaFile.write("# = Conjoint %s Version Quota\n" % conjointNames[conjointIndex])
		for i in range(numVersions):
			conjointQuotaFile.write("cj%sver_%d\tinf\n" % (conjointNames[conjointIndex], i+1))
		conjointQuotaFile.close()
	
	# =======================================================================================================
		
	print("")
	print("Completed all conjoints.  Here follows a summary of the outputted files:")
	print("")
	print("1. conjoint.xml: XML code for the conjoint%s.  Paste the contents of this file into your project's XML." % ("s" if numberOfConjoints > 1 else ""))
	print("2. quotaDefines.txt: Content to paste into the defines tab of your project's quota.xls.")
	
	for q in range(len(conjointNames)):
		print("%d. quotaConjoint%s.txt: Create a new tab in your project's quota.xls called \"ConjointVersion%s\" and" % (3+q, conjointNames[q ], conjointNames[q ]))
		print("   paste the contents of this file into it.")

	print("")
	print("Don't forget to upload your design file%s and updated quota sheet into your project before pasting the conjoint XML!" % ("s" if numberOfConjoints > 1 else ""))
	print("")
	
		
except Exception:
	print(traceback.format_exc())
	
input("Press enter to close.")