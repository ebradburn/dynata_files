try:
	import sys
	import traceback
	
	# ED'S CONJOINT MAKER - UPDATED 2023 FEB 27
	
	print("Welcome to the conjoint maker!")
	print("PLEASE STUDY YOUR DESIGN FILES AND REFERENCE MATERIALS CAREFULLY BEFORE USING THIS SCRIPT!")
	print("")
	print("/!\\ /!\\ /!\\ WARNING!!!  If you use this script, you are expected at the very least to attempt to understand how the outputted code works!")
	print("Do not expect me to help you fix problems with the outputted code if you have not attempted to fix them yourself first!")
	
	numberOfConjoints = 1
	
	print("")
	print("This program creates a conjoint, one at a time.")
	print("It is recommended that you give your conjoint a unique identifier, even if your project only has one conjoint.")
	print("The unique identifier should ideally be as short as possible.  It can start with a number.  Use only letters and numbers.")
	unique_identifier = input("Enter the unique identifier for this conjoint (leave blank for none - not recommended): ")
	conjointNames = [unique_identifier]
	
	for conjointIndex in range(numberOfConjoints):
		print("")	
		input("Move your design file, named \"design%s.dat\", into the same folder as this script and press enter." % conjointNames[conjointIndex])
		
		designFile = open("design%s.dat" % (conjointNames[conjointIndex]), "r")
		outputFile = open("conjoint%s.xml"  % (conjointNames[conjointIndex]), "w")
		
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
		print("This is usually obtained from the vars_levels sheet of your design excel file, with headers both horizontally and vertically.")
		print("See rawInputs.dat for an example of how this file should be formatted.")
		print("If you don't have one, leave this blank and you can enter the text manually.")
		nameFilename = input("Enter the filename of your attributes file: ")
		enterManually = False
		
		attributeNames = ["" for i in range(numAttributes)]
		
		if nameFilename == "":
			print("\nEnter the texts manually.  Press Ctrl+C to close program.\n")
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
					print("All righty then, enter the texts manually. Press Ctrl+C to close program.")
					print("")
					enterManually = True
			
			except Exception:
				enterManually = True
				print(traceback.format_exc())
				print("\nAn error occurred while reading the file or the file was not found.  Enter the texts manually.   Press Ctrl+C to close program.\n")
		
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
		print("Does this conjoint have a \"none of these\" option? (y/n)")
		none_of_these_answer = input("")
		if none_of_these_answer == 'y' or none_of_these_answer == "Y":
		    none_of_these = True
		else:
		    none_of_these = False
		
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
                
		if none_of_these:
			outputString += "<res label=\"cj%s_none_of_these\">None of these options</res>\n" % (conjointNames[conjointIndex])
		
		# 2: exec when init block
		outputString += "\n"
		outputString += "<exec when=\"init\">\n"
		outputString += "# ===============================================================================================\n"
		outputString += "# CONJOINT COMMON SECTION - All conjoints\n"
		outputString += "# Regardless of the number of conjoints your project has, you only need to transfer this exec block to your survey one time.\n"
		outputString += "# This section contains helper functions that may be useful when editing your conjoint.\n"
		outputString += "# If you need to define a custom function that multiple conjoints use, then do so here.\n"
		outputString += "# ===============================================================================================\n"
		outputString += "\n"
		outputString += "# This function takes a list of strings, gets rid of blank strings, and combines them with a line break in between.\n"
		outputString += "# Useful for situations where you have multiple attributes that are all supposed to be displayed within the same cell.\n"
		outputString += "def combine_attributes(text_attribute_list):\n"
		outputString += "\treturn '&lt;br /&gt;'.join([item for item in text_attribute_list if item != ''])\n"
		outputString += "\n"
		outputString += "# This function looks up the conjoint data dictionary in the first argument, and looks up based on the\n"
		outputString += "# version/task/concept/attribute values given.  This then returns the attribute value.\n"
		outputString += "def quick_att(dict, ver, task, con, att):\n"
		outputString += "\treturn dict[(ver, task, con, att)]\n"
		outputString += "</exec>\n"
		outputString += "\n"
		outputString += "<exec when=\"init\">\n"
		outputString += "# ==================================================\n"
		outputString += "# INITIALIZE CONJOINT %s\t\n" % (conjointNames[conjointIndex])
		outputString += "# ==================================================\n"
		outputString += "num_versions_%s = %d\n" % (conjointNames[conjointIndex], numVersions)
		outputString += "num_tasks_per_version_%s = %d\n" % (conjointNames[conjointIndex], numTasks)
		outputString += "num_concepts_per_task_%s = %d\n" % (conjointNames[conjointIndex], numConcepts)
		outputString += "num_attributes_per_concept_%s = %d\n" % (conjointNames[conjointIndex], numAttributes)
		outputString += "\n"
		outputString += "# Structure of dict is:\n"
		outputString += "# conjoint_data_%s[(version number, task number, concept number, attribute number)] = attribute value\n" % (conjointNames[conjointIndex])
		outputString += "conjoint_data_%s = {}\n" % (conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "# Open design file and read into conjoint_data_%s\n" % (conjointNames[conjointIndex])
		outputString += "input_file_%s = open('design%s.dat', \"r\")\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "for i, line in enumerate(input_file_%s):\n" % (conjointNames[conjointIndex])
		outputString += "\t\n"
		outputString += "\t# Skip headers\n"
		outputString += "\tif i == 0:\n"
		outputString += "\t\tcontinue\n"
		outputString += "\t\t\n"
		outputString += "\t# Split line by tabs and collect version/task/concept/attribute data\n"
		outputString += "\tsplit_line = line.split('\\t')\n"
		outputString += "\tcurrent_version = int(split_line[0].strip())\n"
		outputString += "\tcurrent_task = int(split_line[1].strip())\n"
		outputString += "\tcurrent_concept = int(split_line[2].strip())\n"
		outputString += "\tcurrent_attributes = [int(item.strip()) for item in split_line[3:]]\n"
		outputString += "\t\n"
		outputString += "\t# Load into dictionary\n"
		outputString += "\tfor j, item in enumerate(current_attributes):\n"
		outputString += "\t\tconjoint_data_%s[(current_version, current_task, current_concept, j + 1)] = item\n" % (conjointNames[conjointIndex])
		outputString += "\t\n"
		outputString += "input_file_%s.close()\n" % (conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "# =======================================================================================================\t\n"
		outputString += "# CONJOINT %s-SPECIFIC FUNCTIONS\n" % (conjointNames[conjointIndex])
		outputString += "# Functions that only conjoint %s uses.  If you need to define a function that only this conjoint uses,\n" % (conjointNames[conjointIndex])
		outputString += "# do so here.\n"
		outputString += "# =======================================================================================================\n"
		outputString += "\n"
		outputString += "# This function returns the res tag of the given type and attribute value, allowing for display of text.\n"
		outputString += "def get_text_%s(type, attribute):\n" % (conjointNames[conjointIndex])
		outputString += "\tif hasattr(res, \"cj%s_att\" + str(type) + \"_\" + str(attribute)):\n" % (conjointNames[conjointIndex])
		outputString += "\t\treturn getattr(res, \"cj%s_att\" + str(type) + \"_\" + str(attribute))\n" % (conjointNames[conjointIndex])
		outputString += "\telse:\n"
		outputString += "\t\treturn None\n"
		outputString += "\n"
		outputString += "</exec>\n"
		outputString += "\n"
		
		# 3: Conjoint block
		outputString += "<block label=\"CONJOINT_%s_BLOCK\">\n" % conjointNames[conjointIndex]
		outputString += "  <quota label=\"quota_cj%s\" overquota=\"noqual\" sheet=\"ConjointVersion%s\"/>\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\n"
		outputString += "  <suspend/>\n"
		outputString += "\n"
		outputString += "  <number \n"
		outputString += "    label=\"HP_versionNumber%s\"\n" % conjointNames[conjointIndex]
		outputString += "    size=\"3\"\n"
		outputString += "    where=\"execute,survey,report\">\n"
		outputString += "      <title>Hidden Question. %s Version Number</title>\n" % conjointNames[conjointIndex]
		outputString += "    <exec>\n"
		outputString += "for i in range(1, num_versions_%s + 1):\n" % conjointNames[conjointIndex]
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
		outputString += "\n"
		
		# Time capture, part 1
		outputString += "\t<exec>\n"
		outputString += "p.startTime = timeSpent()\n"
		outputString += "\t</exec>\n"
		outputString += "\n"

		outputString += "\t<suspend/>\n"
		outputString += "\n"
		
		# Attributes capture
		outputString += "\t    <number\n" 
		outputString += "\t  label=\"CJATTRIBUTES%s_[loopvar: task]\"\n" % conjointNames[conjointIndex]
		outputString += "\t  optional=\"1\"\n"
		outputString += "\t  size=\"3\"\n"
		outputString += "\t  translateable=\"0\"\n"
		outputString += "\t  where=\"execute,survey,report\">\n"
		outputString += "\t      <title>Hidden Question.  Attribute values shown for task [loopvar: task].</title>\n"
		outputString += "\t      <exec>\n"
		outputString += "for i, row in enumerate([row.label for row in CJATTRIBUTES%s_[loopvar: task].rows]):\n" % conjointNames[conjointIndex]
		outputString += "\tfor j, col in enumerate([col.label for col in CJATTRIBUTES%s_[loopvar: task].cols]):\n" % conjointNames[conjointIndex]
		outputString += "\t\tCJATTRIBUTES%s_[loopvar: task].attr(row).attr(col).val = quick_att(conjoint_data_%s, HP_versionNumber%s.val, [loopvar: task], j+1, i+1)\n" % (conjointNames[conjointIndex], conjointNames[conjointIndex], conjointNames[conjointIndex])
		outputString += "\t      </exec>\n"
		outputString += "\n"

		for i in range(numConcepts):
			outputString += "\t      <col label=\"c%d\"><b>Concept %d</b></col>\n" % (i+1, i+1)
        
		for i in range(numAttributes):
			outputString += "\t      <row label=\"r%d\">Att %d - %s</row>\n" % (i+1, i+1, attributeNames[i])
		
		outputString += "\t</number>\n"
		outputString += "\n"
		outputString += "\t<suspend/>\n"
		
		# Conjoint exercise question
		outputString += "      <radio \n"
		outputString += "     label=\"CJEXERCISE%s_[loopvar: task]\"\n" % conjointNames[conjointIndex]
		outputString += "     ss:colWidth=\"200px\"\n"
		outputString += "     surveyDisplay=\"desktop\">\n"
		outputString += "        <title>ENTER YOUR CONJOINT QUESTION TEXT HERE</title>\n"
		
		conceptColumnList = ["'c%d'" % (i+1) for i in range(numConcepts)]
		conceptColumnString = ", ".join(conceptColumnList)
		
		# Style blocks
		for i in range(numAttributes):
			outputString += "<style label=\"replaceElements%s_%d\" cond=\"col.label in [%s]\" name=\"question.element\" rows=\"a%d\"><![CDATA[\n" % (conjointNames[conjointIndex], i+1, conceptColumnString, i+1)
			outputString += "<td style=\"vertical-align:middle;background-color:${'#DCE6F1' if col.index % 2 == 0 else 'white'}\" headers=\"${ec.this.label + \"_\" + ec.col.label if ec.col.label else \"\"}\" class=\"cell nonempty legend col-legend col-legend-left col-legend-basic legend-level-1\"  $(extra)>\n"
			outputString += "${get_text_%s(%d, quick_att(conjoint_data_%s, HP_versionNumber%s.val, [loopvar: task], col.index + 1, %d))}</td>\n" % (conjointNames[conjointIndex], i+1, conjointNames[conjointIndex], conjointNames[conjointIndex], i+1)
			outputString += "]]></style>\n"
            
        # Style blocks for "None" column
		if none_of_these:
        
			attribute_rows = ['a' + str(i+1) for i in range(numAttributes)]
			middle_attribute_row = attribute_rows[int(numAttributes / 2)]
			first_style_rows = [item for item in attribute_rows if item != middle_attribute_row]
			
			outputString += "<style label=\"replaceElements%s_NONE1\" cond=\"col.label in ['c%d']\" name=\"question.element\" rows=\"%s\"><![CDATA[\n" % (conjointNames[conjointIndex], numConcepts+1, ','.join(first_style_rows))
			outputString += "<td style=\"vertical-align:middle;background-color:${'#DCE6F1' if col.index % 2 == 0 else 'white'}; border-top: none; border-bottom: none;\" headers=\"${ec.this.label + \"_\" + ec.col.label if ec.col.label else \"\"}\" class=\"cell nonempty legend col-legend col-legend-left col-legend-basic legend-level-1\"  $(extra)>\n"
			outputString += "</td>\n"
			outputString += "]]></style>\n"
			outputString += "<style label=\"replaceElements%s_NONE2\" cond=\"col.label in ['c%d']\" name=\"question.element\" rows=\"%s\"><![CDATA[\n" % (conjointNames[conjointIndex], numConcepts+1, middle_attribute_row)
			outputString += "<td style=\"vertical-align:middle;background-color:${'#DCE6F1' if col.index % 2 == 0 else 'white'}; border-top: none; border-bottom: none;\" headers=\"${ec.this.label + \"_\" + ec.col.label if ec.col.label else \"\"}\" class=\"cell nonempty legend col-legend col-legend-left col-legend-basic legend-level-1\"  $(extra)>\n"
			outputString += "${res.cj%s_none_of_these}</td>\n" % (conjointNames[conjointIndex])
			outputString += "]]></style>\n"
            
        # Style block for javascript
		outputString += "<style name=\"question.after\" wrap=\"ready\">\n"
		outputString += "<![CDATA[\n"    
		outputString += "    $ (\".col-legend-top\").css(\"background-color\", \"#1F497D\");\n"
		outputString += "    $ (\".col-legend-top\").css(\"color\", \"#FFFFFF\");\n"
		outputString += "    $ (\".row-legend-left\").css(\"background-color\", \"#1F497D\");\n"
		outputString += "    $ (\".row-legend-left\").css(\"color\", \"#FFFFFF\");\n"
		outputString += "    $ (\".clickableCell\").css(\"background-color\", \"#1F497D\");\n"
		outputString += "]]></style>\n"
		
		# Cols
		for i in range(numConcepts):
			outputString += "        <col label=\"c%d\" value=\"%d\"><b>Option %d</b></col>\n" % (i+1, i+1, i+1)
		
        # "None of these" column
		if none_of_these:
			outputString += "        <col label=\"c%d\" value=\"%d\"><b>None</b></col>\n" % (numConcepts+1, numConcepts+1)
        
		# Rows
		for i in range(numAttributes):
			outputString += "        <row label=\"a%d\" where=\"notdp\" optional=\"1\"><b>%s</b></row>\n" % (i+1, attributeNames[i])
		
		outputString += "        <row label=\"r1\"/>\n"
		outputString += "      </radio>\n"
		outputString += "\n"	
		outputString += "\t<suspend/>\n"
		outputString += "\n"	
		
		# Time capture, part 2
		outputString += "\t	   <float \n"
		outputString += "\t  label=\"CJTIMER%s_[loopvar: task]\"\n" % conjointNames[conjointIndex]
		outputString += "\t  size=\"15\"\n"
		outputString += "\t  translateable=\"0\"\n"
		outputString += "\t  where=\"execute,survey,report\">\n"
		outputString += "\t      <title>Hidden Question.  Timer for each task in conjoint exercise %s (in seconds).</title>\n" % conjointNames[conjointIndex]
		outputString += "\t      <exec>\n"
		outputString += "CJTIMER%s_[loopvar: task].val = (timeSpent() - p.startTime)\n" % conjointNames[conjointIndex]
		outputString += "\t      </exec>\n"
		outputString += "\t    </float>\n"
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
		
		definesFile = open("quotaDefines%s.txt" % conjointNames[conjointIndex], "w" if conjointIndex == 0 else "a")
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
	print("Completed conjoint.  Here follows a summary of the outputted files:")
	print("")
	print("- quotaDefines%s.txt: Content to paste into the defines tab of your project's quota.xls." % conjointNames[0])
	
	for q in range(len(conjointNames)):
		print("- quotaConjoint%s.txt: Create a new tab in your project's quota.xls called \"ConjointVersion%s\" and" % (conjointNames[q ], conjointNames[q ]))
		print("  paste the contents of this file into it.")

	print("- conjoint%s.xml: XML code for the conjoint%s.  Paste the contents of this file into your project's XML." % (conjointNames[0], "s" if numberOfConjoints > 1 else ""))
	print("")
	print("Be sure to upload your %s and updated quota sheet into your project before pasting the conjoint XML!" % ("design" + conjointNames[0] + ".dat"))
	print("")
	
		
except Exception:
	print(traceback.format_exc())
	
input("Press enter to close.")
