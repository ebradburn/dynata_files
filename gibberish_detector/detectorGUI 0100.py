from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import easygui
import xlrd
import xlwt
import traceback
import string
import datetime
import time
import math
import _thread
import pkg_resources
from symspellpy.symspellpy import SymSpell, Verbosity

# NOTE TO ANYONE RUNNING THIS SCRIPT:
# You need to install the following python packages before this will run:
# xlrd, xlwt, symspellpy, easygui

# TO-DO LIST:
# - (FEATURE) make the "copy all field names" button work
# - (FEATURE) import/export settings
# - (RELEASE) compile program to .exe

class myGUI(object):

	def __init__(self):
	
		print("Initializing, please wait...")
	
		self.root = Tk()
		self.version = "0.100"
		self.name = "Ed's Gibberish Detector"
		self.root.wm_title("%s v%s" % (self.name, self.version))
		self.root.geometry("1024x768+40+40")
	
		self.STATE_WAITING_FOR_INPUT_FILE_BUTTON_CLICK = 0
		self.STATE_WAITING_FOR_INPUT_FILE_SELECTION = 1
		self.STATE_INITIAL_READ = 2
		self.STATE_WAITING_TO_PROCEED = 5
		self.STATE_DETECTING = 3
		self.STATE_DETECTING_START = 6
		self.STATE_COMPLETED = 4	
		
		self.currentState = self.STATE_WAITING_FOR_INPUT_FILE_BUTTON_CLICK		
		self.currentInputFilename = None
		
		self.framesInCurrentState = 0
		self.timeWhenStarted = 0
		self.timeElapsed = 0
		
		self.isShowingAutoFlagWords = False
		
		self.myWorkbook = None
		
		self.numFields = 0
		self.numRespondents = 0
		self.currentRespondent = 0
		self.numIgnored = 0
		self.totalFieldsToCheck = 0
		self.fieldNames = []
		
		self.fieldNameToIndexDict = {}
		self.indexToFieldNameDict = {}
		self.emphasisDict = {}
		self.gibberishDict = {}
		
		self.scrutinyDict = {}
		self.colorDict = {}
		self.colorList = ["#0000FF", "#0014FF", "#0028FF", "#003DFF", "#0051FF", "#0065FF", "#007AFF", "#008EFF", "#00A3FF", "#00B7FF", "#00CBFF", "#00E0FF", "#00F4FF", "#00FFF4", "#00FFE0", "#00FFCB", "#00FFB7", "#00FFA3", "#00FF8E", "#00FF7A", "#00FF65", "#00FF51", "#00FF3D", "#00FF28", "#00FF14", "#00FF00", "#14FF00", "#28FF00", "#3DFF00", "#51FF00", "#65FF00", "#7AFF00", "#8EFF00", "#A3FF00", "#B7FF00", "#CCFF00", "#E0FF00", "#F4FF00", "#FFF400", "#FFE000", "#FFCC00", "#FFB700", "#FFA300", "#FF8E00", "#FF7A00", "#FF6600", "#FF5100", "#FF3D00", "#FF2800", "#FF1400", "#FF0000"]
		for i in range(101):
			self.scrutinyDict[i] = 0
			self.colorDict[i] = self.colorList[ int(i / 2) ]
		
		self.mySpellChecker = SymSpell(2, 7)
		dictionary_path = "frequency_dictionary_en_82_765.txt"
		bigram_path = "frequency_bigramdictionary_en_243_342.txt"
		self.mySpellChecker.load_dictionary(dictionary_path, term_index=0, count_index=1)
		self.mySpellChecker.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)
		self.suggestion_verbosity = Verbosity.CLOSEST
		
		# Add contractions to dictionary - why weren't these in the dictionary in the first place?
		# self.mySpellChecker.word_frequency.load_words(["I'm", "I'll", "I'd", "I've", "I'd", "you're", "you'll", "you'd", "you've", "you'd", "he's", "he'll", "he'd", "he's", "he'd", "she's", "she'll", "she'd", "she's", "she'd", "it'll", "it'd", "it's", "it'd", "we're", "we'll", "we'd", "we've", "we'd", "they're", "they'll", "they'd", "they've", "they'd", "that's", "that'll", "that'd", "that's", "that'd", "who's", "who'll", "who'd", "who's", "who'd", "what're", "what'll", "what'd", "what's", "what'd", "where's", "where'll", "where'd", "where's", "where'd", "when's", "when'll", "when'd", "when's", "when'd", "why's", "why'll", "why'd", "why's", "why'd", "how's", "how'll", "how'd", "how's", "how'd", "isn't", "aren't", "wasn't", "weren't", "haven't", "hasn't", "hadn't", "won't", "wouldn't", "don't", "doesn't", "didn't", "can't", "couldn't", "shouldn't", "mightn't", "mustn't", "would've", "should've", "could've", "might've", "must've", "o'", "o'clock", "ma'am", "ne'er-do-well", "cat-o'-nine-tails", "jack-o'-lantern", "will-o'-the-wisp"])
	
		self.btn_openInputFile = Button(self.root, text="Open Excel or tab-delimited text data file...", command=lambda: self.openFile())
		self.lbl_currentFilename = Label(self.root)
		self.lbl_initialReadStatus = Label(self.root)
		
		self.btn_copyFieldsToClipboard = Button(self.root, text="Copy all field names to clipboard", command=lambda: self.doNothing())
		
		self.lbl_respondentIdentifier = Label(self.root, text="Respondent identifier:")
		self.var_respondentIdentifier = StringVar()
		self.btn_respondentIdentifier = Button(self.root, text="Explain", command=lambda: self.explain("ident"))
		self.opt_respondentIdentifier = None
		
		self.lbl_excludeTheseFields = Label(self.root, text="Exclude these fields:")
		self.var_excludeTheseFields = StringVar()
		self.btn_excludeTheseFields = Button(self.root, text="Explain", command=lambda: self.explain("exclu"))
		self.txt_excludeTheseFields = Text(self.root, height=6, width=93)
		self.btn_excludeTheseFields_DEFAULT = Button(self.root, text="Defaults", command=lambda: self.resetExcludeFields())
		self.btn_excludeTheseFields_CLEAR = Button(self.root, text="Clear", command=lambda: self.clearExcludeFields())

		self.lbl_ignoreTheseWords = Label(self.root, text="Ignore these words:")
		self.var_ignoreTheseWords = StringVar()
		self.btn_ignoreTheseWords = Button(self.root, text="Explain", command=lambda: self.explain("empha"))
		self.txt_ignoreTheseWords = Text(self.root, height=6, width=93)
		self.btn_ignoreTheseWords_CLEAR = Button(self.root, text="Clear", command=lambda: self.resetEmphasizeFields())

		#self.lbl_emphasisWeight = Label(self.root, text="Emphasis weight:")
		#self.var_emphasisWeight = StringVar()
		#self.btn_emphasisWeight = Button(self.root, text="Explain", command=lambda: self.explain("emphw"))
		#self.ent_emphasisWeight = Entry(self.root, width=5, textvariable=self.var_emphasisWeight)
		#self.btn_emphasisWeightUP = Button(self.root, text='\u25B2', command=lambda: self.incrementField("empup"))
		#self.btn_emphasisWeightDOWN = Button(self.root, text='\u25BC', command=lambda: self.incrementField("empdn"))

		self.lbl_gibberishWeight = Label(self.root, text="Gibberish weight:")
		self.var_gibberishWeight = StringVar()
		self.btn_gibberishWeight = Button(self.root, text="Explain", command=lambda: self.explain("gibbw"))
		self.ent_gibberishWeight = Entry(self.root, width=5, textvariable=self.var_gibberishWeight)
		self.btn_gibberishWeightUP = Button(self.root, text='\u25B2', command=lambda: self.incrementField("gibup"))
		self.btn_gibberishWeightDOWN = Button(self.root, text='\u25BC', command=lambda: self.incrementField("gibdn"))
		
		self.lbl_autoflagWords = Label(self.root, text="Auto-flag words:")
		self.var_autoflagWords = StringVar()
		self.btn_autoflagWords = Button(self.root, text="Explain", command=lambda: self.explain("autof"))
		self.txt_autoflagWords = Text(self.root, height=6, width=93)
		self.btn_autoflagWords_DEFAULT = Button(self.root, text="Defaults", command=lambda: self.resetAutoFlagWords())
		self.btn_autoflagWords_CLEAR = Button(self.root, text="Clear", command=lambda: self.clearAutoFlagWords())
		self.btn_autoflagWords_SHOWHIDE = Button(self.root, text="Show / Hide", command=lambda: self.toggleAutoFlagWords())
		self.lbl_autoflagWordsWarning = Label(self.root, text="WARNING: Content in this field may be considered offensive.  Click the \"Show / Hide\" button to display its contents.")

		self.lbl_calculationMethod = Label(self.root, text="Per-field calculation method:")
		self.lst_calculationMethod = ["By percent of words", "By percent of characters", "Whichever is higher", "Whichever is lower", "Average"]
		self.var_calculationMethod = StringVar()
		self.btn_calculationMethod = Button(self.root, text="Explain", command=lambda: self.explain("calcm"))
		self.opt_calculationMethod = OptionMenu(self.root, self.var_calculationMethod, *self.lst_calculationMethod)

		self.lbl_overallCalculationMethod = Label(self.root, text="Overall calculation method:")
		self.lst_overallCalculationMethod = ["(Highest + Average) / 2", "Highest field", "Average of all fields"]
		self.var_overallCalculationMethod = StringVar()
		self.btn_overallCalculationMethod = Button(self.root, text="Explain", command=lambda: self.explain("ovrcm"))
		self.opt_overallCalculationMethod = OptionMenu(self.root, self.var_overallCalculationMethod, *self.lst_overallCalculationMethod)
		
		self.lbl_maxWordLengthForDistance2 = Label(self.root, text="Levenshtein distance 2 cutoff:")
		self.var_maxWordLengthForDistance2 = StringVar()
		self.btn_maxWordLengthForDistance2 = Button(self.root, text="Explain", command=lambda: self.explain("mxdst"))
		self.ent_maxWordLengthForDistance2 = Entry(self.root, width=5, textvariable=self.var_maxWordLengthForDistance2)
		self.btn_maxWordLengthForDistance2UP = Button(self.root, text='\u25B2', command=lambda: self.incrementField("levup"))
		self.btn_maxWordLengthForDistance2DOWN = Button(self.root, text='\u25BC', command=lambda: self.incrementField("levdn"))
		
		self.lbl_longestAllowedLength = Label(self.root, text="Longest allowed word length:")
		self.var_longestAllowedLength = StringVar()
		self.btn_longestAllowedLength = Button(self.root, text="Explain", command=lambda: self.explain("lallo"))
		self.ent_longestAllowedLength = Entry(self.root, width=5, textvariable=self.var_longestAllowedLength)
		self.btn_longestAllowedLengthUP = Button(self.root, text='\u25B2', command=lambda: self.incrementField("lawup"))
		self.btn_longestAllowedLengthDOWN = Button(self.root, text='\u25BC', command=lambda: self.incrementField("lawdn"))
		
		#self.lbl_outputFormat = Label(self.root, text="Output file format:")
		#self.var_outputFormat = IntVar()
		#self.btn_outputFormat = Button(self.root, text="Explain", command=lambda: self.explain("outpt"))		
		
		self.btn_beginChecks = Button(self.root, text="BEGIN CHECKS", width=40, justify="center", fg="#FFFFFF", bg="#1d853c", highlightcolor="#23b04d", command=lambda: self.beginChecks())
		self.prb_checksProgressBar = ttk.Progressbar(self.root, orient=HORIZONTAL, length=400, mode = 'determinate')
		self.lbl_checksProgress = Label(self.root, text="0%")
		self.lbl_checksStatus = Label(self.root, text="Checking respondent 0 of 0...")
		self.lbl_checksTime = Label(self.root, text="")
		
		self.resetEmphasizeFields()
		self.resetAutoFlagWords()
		self.resetExcludeFields()
		#self.var_emphasisWeight.set("3")
		self.var_gibberishWeight.set("10")
		self.var_longestAllowedLength.set("19")
		self.var_maxWordLengthForDistance2.set("7")
		self.var_calculationMethod.set( self.lst_calculationMethod[0] )
		self.var_overallCalculationMethod.set( self.lst_overallCalculationMethod[0] )
		
		self.lastRespondent = 0
		self.barsInGraph = []
		self.graphMaxX = 495
		self.graphMaxY = 250
		self.ULX = 5
		self.ULY = 5
		self.graphCanvas = Canvas(self.root, height=self.graphMaxY, width=self.graphMaxX)
		self.showGraph = True
		self.btn_toggleGraph = Button(self.root, text="Show / Hide Graph", command=lambda: self.toggleGraph())
				
		self.root.after(5, self.everyFrame)
		self.root.mainloop()
		
	def toggleAutoFlagWords(self):
	
		self.isShowingAutoFlagWords = not(self.isShowingAutoFlagWords)
		
	def resetExcludeFields(self):
	
		self.txt_excludeTheseFields.delete(1.0, END)
		self.txt_excludeTheseFields.insert(END, "uuid\trnid\tpid\tpsid\tdate\tstart_date\tmarkers")
		
	def clearExcludeFields(self):
	
		self.txt_excludeTheseFields.delete(1.0, END)
	
	def resetEmphasizeFields(self):
		
		self.txt_ignoreTheseWords.delete(1.0, END)
	
	def resetAutoFlagWords(self):
		
		self.txt_autoflagWords.delete(1.0, END)
		self.txt_autoflagWords.insert(END, "anal\tass\tballsack\tbj\tbong\tcocaine\tcum\tdick\tdp\tffs\tfml\tjackass\tkike\tminge\tmuff\tpaki\tpedo\tpube\trape\tretard\tscat\tschlick\tsemen\tslag\ttard\ttestes\ttits\tvagina\twap\twop\tcokehead\tfoad\tfu©k\tsoab\tanalingus\tanalintruder\tanilingus\tanus\tarsebandit\tarsehole\tarsewipe\tasphyxiophilia\tasshole\tasswipe\tb17ch\tb1tch\tbadword\tballbag\tballsac\tbastard\tbattyboy\tbattyman\tbawbag\tbeastiality\tbeefcurtains\tbellend\tbi7ch\tbitch\tblowjob\tbltch\tboabie\tbollocks\tbollox\tboner\tboobjob\tboobies\tboobs\tbuftie\tbuggery\tbukkake\tbullshit\tbumbandit\tbumchum\tbuttfucker\tbuttplug\tc0k\tcack\tcamelcunt\tcameltoe\tcannabis\tcapper\tcarpetmuncher\tchebs\tchickswithdicks\tchink\tchoad\tclit\tclunge\tclusterfuck\tcocksucker\tcock\tcockend\tcockgoblin\tcockmuncher\tcocknose\tcok\tcoon\tcrackhead\tcrackwhore\tcrap\tcreampie\tcretin\tcumshot\tcumstain\tcunilingus\tcunnilingus\tcuntflaps\tcunt\tcybersex\tdago\tdarkie\tdiaf\tdickcheese\tdickhead\tdicknose\tdike\tdildo\tdipshit\tdoggiestyle\tdoggystyle\tdoublepenetration\tdouchebag\tdouchefag\tdunecoon\tdyke\tejaculate\tfadge\tfag\tfaggot\tfandan\tfap\tfascist\tfcuk\tfeck\tfelatio\tfelch\tfellate\tfellatio\tfeltch\tfeltching\tfenian\tfingerbang\tfingerfuck\tfisting\tfluffer\tfook\tforeskin\tfucc\tfuccd\tfucced\tfuccer\tfucces\tfuccing\tfuccs\tfuckface\tfuck\tfucker\tfucking\tfucktard\tfuckwit\tfuct\tfudgepacker\tfugly\tfuk\tfunbags\tfvck\tgangbang\tgangrape\tganja\tgaylord\tgaytard\tgimp\tgizzum\tgloryhole\tgoatse\tgobshite\tgoddamn\tgoddammit\tgollywog\tgonads\tgooch\tgook\tgoolies\tgypo\tgyppo\thandjob\thard-on\thardon\thentai\thooker\thoormister\tincest\tintercourse\tjackingoff\tjackoff\tjamrag\tjap'seye\tjapseye\tjaysis\tjaysus\tjerkoff\tjerkingoff\tjiggaboo\tjism\tjiz\tjizm\tjizz\tkaffir\tkeech\tklunge\tknackers\tknobend\tknobhead\tknobjockey\tkoon\tkyke\tlardarse\tlardass\tlesbo\tlezbo\tlezzer\tlezzie\tmasterbate\tmasterbation\tmasturbat\tmasturbate\tmasturbating\tmasturbation\tmeatspin\tmilf\tminger\tmofo\tmolest\tmong\tmongoloid\tmotherfucker\tmowdie\tmutha\tnig-nog\tnig\tniga\tnigga\tnigger\tnignog\tnob\tnobhead\tnonce\tnumpty\tnutsack\tomfg\toralsex\torgasm\torgy\tp0rn\tpaedo\tpaedofile\tpaedophile\tpecker\tpederast\tpedofile\tpedophile\tpenis\tphuk\tpikey\tpimp\tpissflaps\tpisshead\tpiss\tponce\tpoofter\tpoon\tpoonanie\tpoontang\tporn\tpr0n\tpron\tpubes\tpunani\tpussy\tqueef\tqueer\traghead\traping\trapist\trentboy\tretarded\trimjob\trimming\tringpiece\trugmuncher\ts1ut\ts1utd\tsandnigger\tschlong\tscrote\tscrotum\tsex\tshag\tshagged\tsheepshagger\tshirtlifter\tshithead\tshit\tshitcunt\tshite\tskank\tslapper\tslut\tsmeg\tsmegma\tsnatch\tsodding\tsodomise\tsodomy\tsonofabitch\tson-of-a-bitch\tspaccer\tspack\tspastic\tspaz\tsperm\tspic\tsplooge\tspunk\tstfu\tstiffy\tstrap-on\tstrapon\tsubnormal\ttaig\tteabagged\tteabagging\ttesticle\ttitwank\ttitties\ttitty\ttosspot\ttosser\ttowelhead\ttrannie\ttranny\ttubgirl\ttugjob\tturdburglar\tturd\ttwat\tvadge\tvag\tvaj\twankshaft\twankstain\twank\twanker\twhore\twindowlicker\twog\tyid")

	def clearAutoFlagWords(self):
		
		self.txt_autoflagWords.delete(1.0, END)
		
	def everyFrame(self):
	
		self.framesInCurrentState += 1
	
		if self.currentState == self.STATE_WAITING_FOR_INPUT_FILE_BUTTON_CLICK:
				
			self.btn_openInputFile.place(x = 10, y = 10)
			self.btn_openInputFile.config(state="normal")
			
			self.lbl_currentFilename.place_forget()
			
			self.lbl_initialReadStatus.place_forget()
			
			self.btn_copyFieldsToClipboard.place_forget()
			
			self.lbl_respondentIdentifier.place_forget()
			self.lbl_excludeTheseFields.place_forget()
			self.lbl_ignoreTheseWords.place_forget()
			#self.lbl_emphasisWeight.place_forget()
			self.lbl_gibberishWeight.place_forget()
			self.lbl_autoflagWords.place_forget()
			self.lbl_calculationMethod.place_forget()
			self.lbl_maxWordLengthForDistance2.place_forget()
			#self.lbl_outputFormat.place_forget()
			
			self.btn_respondentIdentifier.place_forget()
			self.btn_excludeTheseFields.place_forget()
			self.btn_ignoreTheseWords.place_forget()
			#self.btn_emphasisWeight.place_forget()
			self.btn_gibberishWeight.place_forget()
			self.btn_autoflagWords.place_forget()
			self.btn_calculationMethod.place_forget()
			self.btn_maxWordLengthForDistance2.place_forget()
			#self.btn_outputFormat.place_forget()
			
			self.btn_excludeTheseFields_DEFAULT.place_forget()
			self.btn_excludeTheseFields_CLEAR.place_forget()
			self.btn_ignoreTheseWords_CLEAR.place_forget()
			self.btn_autoflagWords_DEFAULT.place_forget()
			self.btn_autoflagWords_CLEAR.place_forget()
			self.btn_autoflagWords_SHOWHIDE.place_forget()
			
			#self.ent_emphasisWeight.place_forget()
			#self.btn_emphasisWeightUP.place_forget()
			#self.btn_emphasisWeightDOWN.place_forget()
			self.ent_gibberishWeight.place_forget()
			self.btn_gibberishWeightUP.place_forget()
			self.btn_gibberishWeightDOWN.place_forget()
			self.ent_maxWordLengthForDistance2.place_forget()
			self.btn_maxWordLengthForDistance2UP.place_forget()
			self.btn_maxWordLengthForDistance2DOWN.place_forget()
			
			self.lbl_overallCalculationMethod.place_forget()
			self.btn_overallCalculationMethod.place_forget()
			self.opt_overallCalculationMethod.place_forget()
			
			self.lbl_longestAllowedLength.place_forget()
			self.btn_longestAllowedLength.place_forget()
			self.ent_longestAllowedLength.place_forget()
			self.btn_longestAllowedLengthUP.place_forget()
			self.btn_longestAllowedLengthDOWN.place_forget()
			
			self.txt_excludeTheseFields.place_forget()
			self.txt_ignoreTheseWords.place_forget()
			self.txt_autoflagWords.place_forget()
			self.lbl_autoflagWordsWarning.place_forget()
			
			self.btn_beginChecks.place_forget()
			self.prb_checksProgressBar.place_forget()
			self.lbl_checksProgress.place_forget()
			self.lbl_checksStatus.place_forget()
			self.lbl_checksTime.place_forget()
			
			if self.opt_respondentIdentifier != None:
				self.opt_respondentIdentifier.place_forget()
			self.opt_calculationMethod.place_forget()
			
			self.btn_toggleGraph.place_forget()
			
		elif self.currentState == self.STATE_WAITING_FOR_INPUT_FILE_SELECTION:
			
			self.btn_openInputFile.place(x = 10, y = 10)
			self.btn_openInputFile.config(state="disabled")
			
			self.lbl_currentFilename.place_forget()
			
			self.lbl_initialReadStatus.place_forget()
			
			self.btn_copyFieldsToClipboard.place_forget()
			
			self.lbl_respondentIdentifier.place_forget()
			self.lbl_excludeTheseFields.place_forget()
			self.lbl_ignoreTheseWords.place_forget()
			#self.lbl_emphasisWeight.place_forget()
			self.lbl_gibberishWeight.place_forget()
			self.lbl_autoflagWords.place_forget()
			self.lbl_calculationMethod.place_forget()
			self.lbl_maxWordLengthForDistance2.place_forget()
			#self.lbl_outputFormat.place_forget()
			
			self.btn_respondentIdentifier.place_forget()
			self.btn_excludeTheseFields.place_forget()
			self.btn_ignoreTheseWords.place_forget()
			#self.btn_emphasisWeight.place_forget()
			self.btn_gibberishWeight.place_forget()
			self.btn_autoflagWords.place_forget()
			self.btn_calculationMethod.place_forget()
			self.btn_maxWordLengthForDistance2.place_forget()
			#self.btn_outputFormat.place_forget()
			
			self.btn_excludeTheseFields_DEFAULT.place_forget()
			self.btn_excludeTheseFields_CLEAR.place_forget()
			self.btn_ignoreTheseWords_CLEAR.place_forget()
			self.btn_autoflagWords_DEFAULT.place_forget()
			self.btn_autoflagWords_CLEAR.place_forget()
			self.btn_autoflagWords_SHOWHIDE.place_forget()
			
			#self.ent_emphasisWeight.place_forget()
			#self.btn_emphasisWeightUP.place_forget()
			#self.btn_emphasisWeightDOWN.place_forget()
			self.ent_gibberishWeight.place_forget()
			self.btn_gibberishWeightUP.place_forget()
			self.btn_gibberishWeightDOWN.place_forget()
			self.ent_maxWordLengthForDistance2.place_forget()
			self.btn_maxWordLengthForDistance2UP.place_forget()
			self.btn_maxWordLengthForDistance2DOWN.place_forget()
			
			self.lbl_overallCalculationMethod.place_forget()
			self.btn_overallCalculationMethod.place_forget()
			self.opt_overallCalculationMethod.place_forget()
			
			self.lbl_longestAllowedLength.place_forget()
			self.btn_longestAllowedLength.place_forget()
			self.ent_longestAllowedLength.place_forget()
			self.btn_longestAllowedLengthUP.place_forget()
			self.btn_longestAllowedLengthDOWN.place_forget()
			
			self.txt_excludeTheseFields.place_forget()
			self.txt_ignoreTheseWords.place_forget()
			self.txt_autoflagWords.place_forget()
			self.lbl_autoflagWordsWarning.place_forget()
			
			self.btn_beginChecks.place_forget()
			self.prb_checksProgressBar.place_forget()
			self.lbl_checksProgress.place_forget()
			self.lbl_checksStatus.place_forget()
			self.lbl_checksTime.place_forget()
			
			if self.opt_respondentIdentifier != None:
				self.opt_respondentIdentifier.place_forget()
			self.opt_calculationMethod.place_forget()
			
			self.btn_toggleGraph.place_forget()
			
		elif self.currentState == self.STATE_INITIAL_READ:
				
			self.btn_openInputFile.place(x = 10, y = 10)
			self.btn_openInputFile.config(state="disabled")
			
			self.lbl_currentFilename.config(text = "Opened file: %s" % self.currentInputFilename)
			self.lbl_currentFilename.place(x = 10, y = 40)
			
			self.lbl_initialReadStatus.config(text = "Reading file; gathering summary information...")
			self.lbl_initialReadStatus.place(x = 10, y = 60)
			
			self.btn_copyFieldsToClipboard.place_forget()
			
			self.lbl_respondentIdentifier.place_forget()
			self.lbl_excludeTheseFields.place_forget()
			self.lbl_ignoreTheseWords.place_forget()
			#self.lbl_emphasisWeight.place_forget()
			self.lbl_gibberishWeight.place_forget()
			self.lbl_autoflagWords.place_forget()
			self.lbl_calculationMethod.place_forget()
			self.lbl_maxWordLengthForDistance2.place_forget()
			#self.lbl_outputFormat.place_forget()
			
			self.btn_respondentIdentifier.place_forget()
			self.btn_excludeTheseFields.place_forget()
			self.btn_ignoreTheseWords.place_forget()
			#self.btn_emphasisWeight.place_forget()
			self.btn_gibberishWeight.place_forget()
			self.btn_autoflagWords.place_forget()
			self.btn_calculationMethod.place_forget()
			self.btn_maxWordLengthForDistance2.place_forget()
			#self.btn_outputFormat.place_forget()
			
			self.btn_excludeTheseFields_DEFAULT.place_forget()
			self.btn_excludeTheseFields_CLEAR.place_forget()
			self.btn_ignoreTheseWords_CLEAR.place_forget()
			self.btn_autoflagWords_DEFAULT.place_forget()
			self.btn_autoflagWords_CLEAR.place_forget()
			self.btn_autoflagWords_SHOWHIDE.place_forget()
			
			#self.ent_emphasisWeight.place_forget()
			#self.btn_emphasisWeightUP.place_forget()
			#self.btn_emphasisWeightDOWN.place_forget()
			self.ent_gibberishWeight.place_forget()
			self.btn_gibberishWeightUP.place_forget()
			self.btn_gibberishWeightDOWN.place_forget()
			self.ent_maxWordLengthForDistance2.place_forget()
			self.btn_maxWordLengthForDistance2UP.place_forget()
			self.btn_maxWordLengthForDistance2DOWN.place_forget()
			
			self.lbl_overallCalculationMethod.place_forget()
			self.btn_overallCalculationMethod.place_forget()
			self.opt_overallCalculationMethod.place_forget()
			
			self.lbl_longestAllowedLength.place_forget()
			self.btn_longestAllowedLength.place_forget()
			self.ent_longestAllowedLength.place_forget()
			self.btn_longestAllowedLengthUP.place_forget()
			self.btn_longestAllowedLengthDOWN.place_forget()
			
			self.txt_excludeTheseFields.place_forget()
			self.txt_ignoreTheseWords.place_forget()
			self.txt_autoflagWords.place_forget()
			self.lbl_autoflagWordsWarning.place_forget()
			
			self.btn_beginChecks.place_forget()
			self.prb_checksProgressBar.place_forget()
			self.lbl_checksProgress.place_forget()
			self.lbl_checksStatus.place_forget()
			self.lbl_checksTime.place_forget()
			
			if self.opt_respondentIdentifier != None:
				self.opt_respondentIdentifier.place_forget()
			self.opt_calculationMethod.place_forget()
			
			self.btn_toggleGraph.place_forget()
			
			self.initialRead()
		
		elif self.currentState == self.STATE_WAITING_TO_PROCEED:
				
			self.btn_openInputFile.place(x = 10, y = 10)
			self.btn_openInputFile.config(state="normal")
			
			self.lbl_currentFilename.place(x = 10, y = 40)
			
			self.lbl_initialReadStatus.config(text = "Initial scan complete.  %d respondents, %d fields." % (self.numRespondents, self.numFields))
			self.lbl_initialReadStatus.place(x = 10, y = 60)
			
			self.btn_copyFieldsToClipboard.place(x = 10, y = 80)
			
			baseY = 120
			modY = 115
			incY = 36
			
			self.lbl_respondentIdentifier.place(x = 70, y = baseY + incY*0)
			self.lbl_excludeTheseFields.place(x = 70, y = baseY + incY*1)
			self.lbl_ignoreTheseWords.place(x = 70, y = baseY + incY*4)
			#self.lbl_emphasisWeight.place(x = 70, y = baseY + incY*7)
			self.lbl_gibberishWeight.place(x = 70, y = baseY + incY*7)
			self.lbl_autoflagWords.place(x = 70, y = baseY + incY*8)
			self.lbl_calculationMethod.place(x = 70, y = baseY + incY*11)
			self.lbl_maxWordLengthForDistance2.place(x = 70, y = baseY + incY*13)
			#self.lbl_outputFormat.place(x = 70, y = baseY + incY*13)
			
			self.btn_respondentIdentifier.place(x = 10, y = modY + incY*0)
			self.btn_excludeTheseFields.place(x = 10, y = modY + incY*1)
			self.btn_ignoreTheseWords.place(x = 10, y = modY + incY*4)
			#self.btn_emphasisWeight.place(x = 10, y = modY + incY*7)
			self.btn_gibberishWeight.place(x = 10, y = modY + incY*7)
			self.btn_autoflagWords.place(x = 10, y = modY + incY*8)
			self.btn_calculationMethod.place(x = 10, y = modY + incY*11)
			self.btn_maxWordLengthForDistance2.place(x = 10, y = modY + incY*13)
			#self.btn_outputFormat.place(x = 10, y = modY + incY*13)
			
			self.btn_excludeTheseFields_CLEAR.place(x = 70, y = modY + incY*2)
			self.btn_excludeTheseFields_DEFAULT.place(x = 110, y = modY + incY*2)
			self.btn_ignoreTheseWords_CLEAR.place(x = 70, y = modY + incY*5)
			self.btn_autoflagWords_CLEAR.place(x = 70, y = modY + incY*9)
			self.btn_autoflagWords_DEFAULT.place(x = 110, y = modY + incY*9)
			self.btn_autoflagWords_SHOWHIDE.place(x = 70, y = modY + incY*9.75)
			
			#self.ent_emphasisWeight.place(x = 270, y = baseY + incY*7)
			#self.btn_emphasisWeightUP.place(x = 250, y = modY + incY*7)
			#self.btn_emphasisWeightDOWN.place(x = 300, y = modY + incY*7)
			self.ent_gibberishWeight.place(x = 270, y = baseY + incY*7)
			self.btn_gibberishWeightUP.place(x = 250, y = modY + incY*7)
			self.btn_gibberishWeightDOWN.place(x = 300, y = modY + incY*7)
			self.ent_maxWordLengthForDistance2.place(x = 270, y = baseY + incY*13)
			self.btn_maxWordLengthForDistance2UP.place(x = 250, y = modY + incY*13)
			self.btn_maxWordLengthForDistance2DOWN.place(x = 300, y = modY + incY*13)
			
			self.lbl_overallCalculationMethod.place(x = 70, y = baseY + incY*12)
			self.btn_overallCalculationMethod.place(x = 10, y = modY + incY*12)
			self.opt_overallCalculationMethod.place(x = 250, y = modY + incY*12)
			
			self.lbl_longestAllowedLength.place(x = 70, y = baseY + incY*14)
			self.btn_longestAllowedLength.place(x = 10, y = modY + incY*14)
			self.ent_longestAllowedLength.place(x = 270, y = baseY + incY*14)
			self.btn_longestAllowedLengthUP.place(x = 250, y = modY + incY*14)
			self.btn_longestAllowedLengthDOWN.place(x = 300, y = modY + incY*14)
			
			self.btn_beginChecks.place(x = 10, y = modY + incY*15)
			
			if not(self.isShowingAutoFlagWords):
				self.txt_autoflagWords.place_forget()
				self.lbl_autoflagWordsWarning.place(x = 250, y = baseY + incY*8)
			else:
				self.lbl_autoflagWordsWarning.place_forget()
				self.txt_autoflagWords.place(x = 250, y = modY + incY*8)
			self.opt_calculationMethod.place(x = 250, y = modY + incY*11)
			
			self.txt_excludeTheseFields.place(x = 250, y = modY + incY*1)
			self.txt_ignoreTheseWords.place(x = 250, y = modY + incY*4)
			#self.txt_autoflagWords.place(x = 250, y = modY + incY*8)
			
		
			if self.opt_respondentIdentifier == None:
				self.opt_respondentIdentifier = OptionMenu(self.root, self.var_respondentIdentifier, *self.fieldNames)
				self.var_respondentIdentifier.set(self.fieldNames[0])
			
			if self.opt_respondentIdentifier != None:
				self.opt_respondentIdentifier.place(x = 250, y = modY + incY*0)
				
			self.btn_toggleGraph.place_forget()	
		
		elif self.currentState == self.STATE_DETECTING_START:
		
			self.btn_openInputFile.place(x = 10, y = 10)
			self.btn_openInputFile.config(state="disabled")
			
			self.lbl_currentFilename.place(x = 10, y = 40)
			
			self.lbl_initialReadStatus.config(text = "Initial scan complete.  %d respondents, %d fields." % (self.numRespondents, self.numFields))
			self.lbl_initialReadStatus.place(x = 10, y = 60)
			
			self.btn_copyFieldsToClipboard.place(x = 10, y = 80)
			
			baseY = 120
			modY = 115
			incY = 36
			
			self.lbl_respondentIdentifier.place(x = 70, y = baseY + incY*0)
			self.lbl_excludeTheseFields.place(x = 70, y = baseY + incY*1)
			self.lbl_ignoreTheseWords.place(x = 70, y = baseY + incY*4)
			#self.lbl_emphasisWeight.place(x = 70, y = baseY + incY*7)
			self.lbl_gibberishWeight.place(x = 70, y = baseY + incY*7)
			self.lbl_autoflagWords.place(x = 70, y = baseY + incY*8)
			self.lbl_calculationMethod.place(x = 70, y = baseY + incY*11)
			self.lbl_maxWordLengthForDistance2.place(x = 70, y = baseY + incY*13)
			#self.lbl_outputFormat.place(x = 70, y = baseY + incY*13)
			
			self.btn_respondentIdentifier.place(x = 10, y = modY + incY*0)
			self.btn_excludeTheseFields.place(x = 10, y = modY + incY*1)
			self.btn_ignoreTheseWords.place(x = 10, y = modY + incY*4)
			#self.btn_emphasisWeight.place(x = 10, y = modY + incY*7)
			self.btn_gibberishWeight.place(x = 10, y = modY + incY*7)
			self.btn_autoflagWords.place(x = 10, y = modY + incY*8)
			self.btn_calculationMethod.place(x = 10, y = modY + incY*11)
			self.btn_maxWordLengthForDistance2.place(x = 10, y = modY + incY*13)
			#self.btn_outputFormat.place(x = 10, y = modY + incY*13)
			
			self.btn_excludeTheseFields_CLEAR.place(x = 70, y = modY + incY*2)
			self.btn_excludeTheseFields_CLEAR.config(state="disabled")
			self.btn_excludeTheseFields_DEFAULT.place(x = 110, y = modY + incY*2)
			self.btn_excludeTheseFields_DEFAULT.config(state="disabled")
			self.btn_ignoreTheseWords_CLEAR.place(x = 70, y = modY + incY*5)
			self.btn_ignoreTheseWords_CLEAR.config(state="disabled")
			self.btn_autoflagWords_CLEAR.place(x = 70, y = modY + incY*9)
			self.btn_autoflagWords_CLEAR.config(state="disabled")
			self.btn_autoflagWords_DEFAULT.place(x = 110, y = modY + incY*9)
			self.btn_autoflagWords_DEFAULT.config(state="disabled")
			self.btn_autoflagWords_SHOWHIDE.place(x = 70, y = modY + incY*9.75)
			
			#self.ent_emphasisWeight.place(x = 270, y = baseY + incY*7)
			#self.ent_emphasisWeight.config(state="disabled")
			#self.btn_emphasisWeightUP.place(x = 250, y = modY + incY*7)
			#self.btn_emphasisWeightUP.config(state="disabled")
			#self.btn_emphasisWeightDOWN.place(x = 300, y = modY + incY*7)
			#self.btn_emphasisWeightDOWN.config(state="disabled")
			self.ent_gibberishWeight.place(x = 270, y = baseY + incY*7)
			self.ent_gibberishWeight.config(state="disabled")
			self.btn_gibberishWeightUP.place(x = 250, y = modY + incY*7)
			self.btn_gibberishWeightUP.config(state="disabled")
			self.btn_gibberishWeightDOWN.place(x = 300, y = modY + incY*7)
			self.btn_gibberishWeightDOWN.config(state="disabled")
			self.ent_maxWordLengthForDistance2.place(x = 270, y = baseY + incY*13)
			self.ent_maxWordLengthForDistance2.config(state="disabled")
			self.btn_maxWordLengthForDistance2UP.place(x = 250, y = modY + incY*13)
			self.btn_maxWordLengthForDistance2UP.config(state="disabled")
			self.btn_maxWordLengthForDistance2DOWN.place(x = 300, y = modY + incY*13)
			self.btn_maxWordLengthForDistance2DOWN.config(state="disabled")
			
			self.lbl_overallCalculationMethod.place(x = 70, y = baseY + incY*12)
			self.btn_overallCalculationMethod.place(x = 10, y = modY + incY*12)
			self.opt_overallCalculationMethod.place(x = 250, y = modY + incY*12)
			self.opt_overallCalculationMethod.config(state="disabled")
			
			self.lbl_longestAllowedLength.place(x = 70, y = baseY + incY*14)
			self.btn_longestAllowedLength.place(x = 10, y = modY + incY*14)
			self.ent_longestAllowedLength.place(x = 270, y = baseY + incY*14)
			self.btn_longestAllowedLengthUP.place(x = 250, y = modY + incY*14)
			self.btn_longestAllowedLengthDOWN.place(x = 300, y = modY + incY*14)
			self.ent_longestAllowedLength.config(state="disabled")
			self.btn_longestAllowedLengthUP.config(state="disabled")
			self.btn_longestAllowedLengthDOWN.config(state="disabled")
			
			self.btn_beginChecks.place_forget()
			self.prb_checksProgressBar.place(x = 10, y = modY + incY*15)
			self.lbl_checksProgress.place(x = 410, y = baseY + incY*15)
			self.lbl_checksStatus.place(x = 10, y = baseY + incY*16 - 8)
			self.lbl_checksTime.place(x = 10, y = baseY + incY*17 - 16)
			
			self.btn_toggleGraph.place_forget()
			
			if not(self.isShowingAutoFlagWords):
				self.txt_autoflagWords.place_forget()
				self.lbl_autoflagWordsWarning.place(x = 250, y = baseY + incY*8)
			else:
				self.lbl_autoflagWordsWarning.place_forget()
				self.txt_autoflagWords.place(x = 250, y = modY + incY*8)
				
			self.txt_autoflagWords.config(state="disabled")
			
			self.opt_calculationMethod.place(x = 250, y = modY + incY*11)
			self.opt_calculationMethod.config(state="disabled")
			
			self.txt_excludeTheseFields.place(x = 250, y = modY + incY*1)
			self.txt_excludeTheseFields.config(state="disabled")
			self.txt_ignoreTheseWords.place(x = 250, y = modY + incY*4)
			self.txt_ignoreTheseWords.config(state="disabled")
			
			self.opt_respondentIdentifier.place(x = 250, y = modY + incY*0)
			self.opt_respondentIdentifier.config(state="disabled")
			
			self.currentState = self.STATE_DETECTING
			
		elif self.currentState == self.STATE_DETECTING:
			
			self.prb_checksProgressBar['value'] = (100.0 * self.currentRespondent) / self.numRespondents
			self.lbl_checksProgress.config(text="%d%%" % int((100.0 * self.currentRespondent) / self.numRespondents))
			self.lbl_checksStatus.config(text="Checking respondent %d of %d..." % (self.currentRespondent, self.numRespondents))
			self.lbl_checksTime.config(text="Time elapsed: %s, time remaining: %s" % (self.formatTime(self.timeElapsed), self.estimateTimeRemaining(self.currentRespondent, self.numRespondents, self.timeElapsed)))
			
			self.timeElapsed = time.time() - self.timeWhenStarted
			
			if self.currentRespondent > self.numRespondents:
			#if self.currentRespondent > self.numRespondents or self.currentRespondent > 1000:
				self.currentState = self.STATE_COMPLETED
				self.getProperNouns()
				self.outputResultsAsExcel()
				self.lbl_checksProgress.config(text="100%")
				self.lbl_checksStatus.config(text="Completed.  Check %s for scrutiny scores." % ("[Report] " + self.currentOutputFilename + ".xls") )
				self.lbl_checksTime.config(text="Time elapsed: %s" % self.formatTime(self.timeElapsed))
			
		self.root.after(17, self.everyFrame)

	def openFile(self):
	
		self.currentState = self.STATE_WAITING_FOR_INPUT_FILE_SELECTION
		self.framesInCurrentState = 0
		
		self.currentInputFilename = easygui.fileopenbox()
		
		if self.currentInputFilename != None:
			
			self.currentOutputFilename = self.currentInputFilename
			splitByFolder = self.currentOutputFilename.split("\\")
			self.currentOutputFilename = splitByFolder[ len(splitByFolder) - 1 ]
			
			splitOutputFilename = self.currentOutputFilename.split(".")
			
			# Remove file extension and name the output file
			if len(splitOutputFilename) >= 2:
				splitOutputFilename.remove( splitOutputFilename[len(splitOutputFilename) - 1] )
				self.currentOutputFilename = "_".join(splitOutputFilename)
				
			self.currentState = self.STATE_INITIAL_READ
			self.framesInCurrentState = 0			
		else:
			self.currentOutputFilename = None
		
			self.currentState = self.STATE_WAITING_FOR_INPUT_FILE_BUTTON_CLICK
			self.framesInCurrentState = 0
			
	def initialRead(self):
	
		try:
			self.numFields = 0
			self.numRespondents = 0
			self.numIgnored = 0
			self.totalFieldsToCheck = 0
			self.fieldNames = []
			
			fileExtension = self.currentInputFilename.split(".")[1]

			if fileExtension == "xls" or fileExtension == "xlsx":
			
				self.myWorkbook = xlrd.open_workbook(self.currentInputFilename)
				mySheet = self.myWorkbook.sheet_by_index(0)
				
				for eachColIndex in range(mySheet.ncols):
					self.fieldNames.append(mySheet.cell(0, eachColIndex).value)
				self.numFields = len(self.fieldNames)
				
				for i in range(self.numFields):
					self.fieldNameToIndexDict[ self.fieldNames[i] ] = i
					self.indexToFieldNameDict[ i ] = self.fieldNames[i]
					self.emphasisDict[i] = 1

				self.numRespondents = mySheet.nrows - 1
			
			else:
				initialReadInputFile = open(self.currentInputFilename, "r")
					
				isFirstLine = True
					
				for eachLine in initialReadInputFile:
				
					if isFirstLine:
						isFirstLine = False			
						self.fieldNames = eachLine.split("\t")
						self.numFields = len(self.fieldNames)
						
						for i in range(self.numFields):
							self.fieldNameToIndexDict[ self.fieldNames[i] ] = i
							self.indexToFieldNameDict[ i ] = self.fieldNames[i]
							self.emphasisDict[i] = 1
					else:
						self.numRespondents += 1
				
			self.currentState = self.STATE_WAITING_TO_PROCEED
			self.framesInCurrentState = 0
			
		except Exception:
			messagebox.showerror("File Error", "The file you selected is either corrupt or not supported by this program.  Please ensure that your file is either tab-delimited text or Excel format, and that it only contains ASCII characters.\n\n%s" % traceback.format_exc())
			
			#messagebox.showerror("Error Details", traceback.format_exc())
			
			self.currentState = self.STATE_WAITING_FOR_INPUT_FILE_BUTTON_CLICK
			self.framesInCurrentState = 0
			
	def explain(self, requestedExplanation):
		if requestedExplanation == "ident":
			messagebox.showinfo("Explanation", "Unique field that identifies the respondent.  This is usually \"uuid\", but can be other fields such as \"record\", \"rnid\" or \"psid\".")
		elif requestedExplanation == "exclu":
			messagebox.showinfo("Explanation", "Fields to be excluded from the gibberish detection.  Must be a list of field names separated by tabs.  Can be left blank.  Is case-sensitive.  Data fields that are blank, purely numeric, or the respondent identifier will be automatically skipped.")
		elif requestedExplanation == "empha":
			messagebox.showinfo("Explanation", "Words to add to the dictionary.  Must be a list of words separated by tabs.  Can be left blank.  Is not case-sensitive.  Useful for preventing proper nouns or slang terms from being flagged as gibberish.")
		elif requestedExplanation == "emphw":
			messagebox.showinfo("Explanation", "The amount of effect that an emphasized field will have on the scrutiny score, relative to other fields.")
		elif requestedExplanation == "gibbw":
			messagebox.showinfo("Explanation", "How influential a gibberish detection is to the scrutiny score.  The higher this value, the higher an effect a gibberish detection will have on the score.  A value of 1 means an effect equal to that of a misspelled word, and 2 is double the effect.  A value of 0 means that a gibberish detection will not affect the score.  Recommended value is at least 3.")
		elif requestedExplanation == "calcm":
			messagebox.showinfo("Explanation", "Method to use to calculate scrutiny score per field.")  
		elif requestedExplanation == "ovrcm":
			messagebox.showinfo("Explanation", "Method to use to calculate overall scrutiny score.")
		elif requestedExplanation == "autof":
			messagebox.showinfo("Explanation", "Words that, if used, automatically set the overall scrutiny score to 100.  Respondent must use the entire word by itself and spell it correctly for this to work.   Must be a list of lowercase words separated by tabs.  Use this to automatically flag respondents who use words that would surely get them disqualified, such as swear words or ethnic slurs.")
		elif requestedExplanation == "mxdst":
			messagebox.showinfo("Explanation", "Maximum word length (in characters) to use a Levenshtein distance of 2.  Decreasing this value can improve the checking speed but increases the chance that a word that is incorrectly spelled will be flagged as gibberish. Recommended value is between 8 and 12.")  
		elif requestedExplanation == "lallo":
			messagebox.showinfo("Explanation", "Maximum length (in characters) before treating a word as too long to be a word.  Any words longer than this length will automatically be treated as gibberish.  Decreasing this value can improve the checking speed but will cause longer words to be flagged as gibberish, even if they are spelled correctly. Recommended value is at least 19.") 
		elif requestedExplanation == "outpt":
			messagebox.showinfo("Explanation", "File format in which to save output.")
	
	def incrementField(self, request):
	
		#if request == "empup":
		#	self.var_emphasisWeight.set( str( int(self.var_emphasisWeight.get()) + 1 ) if self.var_emphasisWeight.get().isdigit() else "3" )
		#elif request == "empdn":
		#	self.var_emphasisWeight.set( "0" if self.var_emphasisWeight.get() == "0" else str( int(self.var_emphasisWeight.get()) - 1 ) if self.var_emphasisWeight.get().isdigit() else "3" )
		if request == "gibup":
			self.var_gibberishWeight.set( str( int(self.var_gibberishWeight.get()) + 1 ) if self.var_gibberishWeight.get().isdigit() else "4" )
		elif request == "gibdn":
			self.var_gibberishWeight.set( "0" if self.var_gibberishWeight.get() == "0" else str( int(self.var_gibberishWeight.get()) - 1 ) if self.var_gibberishWeight.get().isdigit() else "4" )
		elif request == "levup":
			self.var_maxWordLengthForDistance2.set( str( int(self.var_maxWordLengthForDistance2.get()) + 1 ) if self.var_maxWordLengthForDistance2.get().isdigit() else "9" )
		elif request == "levdn":
			self.var_maxWordLengthForDistance2.set( "3" if self.var_maxWordLengthForDistance2.get() == "3" else str( int(self.var_maxWordLengthForDistance2.get()) - 1 ) if self.var_maxWordLengthForDistance2.get().isdigit() else "9" )
		elif request == "lawup":
			self.var_longestAllowedLength.set( str( int(self.var_longestAllowedLength.get()) + 1 ) if self.var_longestAllowedLength.get().isdigit() else "17" )
		elif request == "lawdn":
			self.var_longestAllowedLength.set( "0" if self.var_gibberishWeight.get() == "0" else str( int(self.var_longestAllowedLength.get()) - 1 ) if self.var_longestAllowedLength.get().isdigit() else "17" )
	 
	def beginChecks(self):
	
		# Load contents of "Ignore these words" into dictionary
		ignoreTheseWords = self.txt_ignoreTheseWords.get(1.0, END).strip().split("\t")
		#self.mySpellChecker.word_frequency.load_words(ignoreTheseWords)
	
		# Place the graph canvas
		self.graphCanvas.place(x = 520, y = 510)
	
		self.currentState = self.STATE_DETECTING_START
		self.currentRespondent = 0
		self.timeWhenStarted = time.time()
		_thread.start_new_thread(self.executeChecksOnOwnThread, (self.numRespondents, None))
		_thread.start_new_thread(self.drawGraphOnOwnThread, (self.numRespondents, None))
		
	def executeChecksOnOwnThread(self, numberOfRespondents, thisIsIgnored):
	
		while self.currentRespondent <= numberOfRespondents:
			self.checkRecord(self.currentRespondent)
			self.currentRespondent += 1
			
	def drawGraphOnOwnThread(self, numberOfRespondents, thisIsIgnored):
	
		# Labels Y axis
		self.graphCanvas.create_text(22, 124, text="Count", font="Small_Fonts 8", anchor="center")
		self.graphCanvas.create_text(30, 226, text="0", font="Small_Fonts 8", anchor="e")
		
		# Labels X axis
		self.graphCanvas.create_text(59, 234, text="1", font="Small_Fonts 8", anchor="e")
		self.graphCanvas.create_text(159, 234, text="25", font="Small_Fonts 8", anchor="e")
		self.graphCanvas.create_text(259, 234, text="50", font="Small_Fonts 8", anchor="e")
		self.graphCanvas.create_text(251, 244, text="Scrutiny score", font="Small_Fonts 8", anchor="center")
		self.graphCanvas.create_text(359, 234, text="75", font="Small_Fonts 8", anchor="e")
		self.graphCanvas.create_text(463, 234, text="100", font="Small_Fonts 8", anchor="e")
		
		# Base of graph
		self.graphCanvas.create_rectangle(self.ULX, self.ULY, self.graphMaxX, self.graphMaxY, outline="black")
		self.graphCanvas.create_line(self.ULX + 35, self.ULY + 20, self.ULX + 35, self.graphMaxY - 25)
		self.graphCanvas.create_line(self.ULX + 35, self.graphMaxY - 25, self.graphMaxX - 25, self.graphMaxY - 25)
	
		self.barsInGraph = [None] * 102
		self.barsInGraph[101] = self.graphCanvas.create_text(30, 31, text="1", font="Small_Fonts 8", anchor="e")
	
		#while True:
		while self.currentRespondent <= self.numRespondents:
			self.redrawGraph()
			time.sleep(0.1)
		
	def checkRecord(self, respondentToCheck):
	
		#print("Checking respondent %d" % respondentToCheck)
	
		ignoreTheseWords = self.txt_ignoreTheseWords.get(1.0, END).strip().split("\t")
	
		allFields = []
		fieldsContributingToScore = []
				
		excludeTheseFields = self.txt_excludeTheseFields.get(1.0, END).strip().split("\t")
		
		autoFlagWords = self.txt_autoflagWords.get(1.0, END).strip().split("\t")
		currentLine = 0
		highestFieldScore = 0
		highestContributorFieldName = ""
		highestContributorFieldValue = ""
		
		if respondentToCheck == 0:
			output1 = open("[Partial results] " + self.currentOutputFilename + ".txt", "w")
			output1.write("Respondent ID\tTotal fields checked\tScrutiny score\tLargest contributor to score\tValue of field\tOther contributing fields\n")
			output1.close()
			return
			
		output1 = open("[Partial results] " + self.currentOutputFilename + ".txt", "a")
		#output1.write(str(excludeTheseFields) + "\n")
		
		fileExtension = self.currentInputFilename.split(".")[1]

		if fileExtension == "xls" or fileExtension == "xlsx":
		
			mySheet = self.myWorkbook.sheet_by_index(0)
			
			for eachColIndex in range(mySheet.ncols):
			
				myValue = mySheet.cell(respondentToCheck, eachColIndex).value
				
				lenMyValue = len(str(myValue))
				
				if str(myValue)[-2:] == ".0":
					myValue = str(myValue)[0:lenMyValue - 2]
				
				allFields.append(str(myValue))
		
		else:
		
			input2 = open(self.currentInputFilename, "r")
		
			for eachLine in input2:
				
				if currentLine != respondentToCheck:
					currentLine += 1
					continue
					
				else:
					allFields = eachLine.split("\t")
					break
				
			input2.close()
			
		automatic100 = False
		auto100fieldName = ""
		auto100triggerWord = ""
		pointsEarned = 0
		pointsPossible = 0
		thisIdentifier = ""
		totalFieldsCheckedForThisRespondent = 0
		
		allMisspelled = []
		allGibberish = []
		allOffensive = []
		totalWords = 0
		
		for i in range( len(allFields) ):
		
			if self.indexToFieldNameDict[i] == self.var_respondentIdentifier.get():
				thisIdentifier = allFields[i]
		
			if self.indexToFieldNameDict[i] in [self.var_respondentIdentifier.get()] or self.indexToFieldNameDict[i] in excludeTheseFields:
				#output1.write("Skipping field %s due to exclusion\n" % self.indexToFieldNameDict[i])
				continue
				
			if allFields[i].strip() == "" or allFields[i].strip().isdigit():
				#output1.write("Skipping field %s due to blank/numeric\n" % self.indexToFieldNameDict[i])
				continue
			
			myInput = allFields[i]
			for eachChar in "!\"#$%&()*+, -./:;<=>?@[\]^_`{|}~”“":
				myInput = myInput.replace(eachChar, " ")
				
			myInput = myInput.replace("’", "'")
			myInput = myInput.replace("â€™", "'")
				
			while "  " in myInput:
				myInput = myInput.replace("  ", " ")
				
			myInputWithoutSpaces = myInput.replace(" ", "")
			numInputChars = len(myInputWithoutSpaces)
			numInputWords = len(myInput.split(" "))
			
			misspelled = []
			gibberish = []
			offensive = []
			
			for eachWord in myInput.split(" "):
			
				#eachWord = "asjdk;ajk;s"
				totalWords += 1
			
				if len(eachWord) > int(self.var_longestAllowedLength.get()):
					gibberish.append(eachWord.lower())
					continue
					
				if eachWord.strip() == "":
					totalWords -= 1
					continue
					
				if any(char.isdigit() for char in eachWord):
					totalWords -= 1
					continue
					
				#self.mySpellChecker.distance = 1 if len(eachWord) > int(self.var_maxWordLengthForDistance2.get()) else 2
				
				suggestions = self.mySpellChecker.lookup(eachWord.lower(), self.suggestion_verbosity, 2)
				suggestionList = [str(eachSuggestion.term) for eachSuggestion in suggestions]
				#print("%s: %s" % (eachWord, str(suggestionList)))
				
				# Autoflag word
				if eachWord.lower() in autoFlagWords:
					offensive.append(eachWord.lower())
					
					if eachWord.lower() not in allOffensive:
						allOffensive.append(eachWord.lower())
					
					automatic100 = True
					highestFieldScore = 100
					highestContributorFieldName = self.fieldNames[i]
					highestContributorFieldValue = myInput
					fieldsContributingToScore.append(self.fieldNames[i])
				
				# Word spelled correctly
				elif eachWord.lower() in suggestionList:
					continue
					
				# Ignored word
				elif eachWord.lower() in ignoreTheseWords:
					continue
				
				# Gibberish
				elif len(suggestionList) == 0:
					gibberish.append(eachWord.lower())
					
					if eachWord.lower() not in allGibberish:
						allGibberish.append(eachWord.lower())
					
					if eachWord.lower() not in self.gibberishDict.keys():
						self.gibberishDict[eachWord.lower()] = 1
					else:
						self.gibberishDict[eachWord.lower()] += 1
				
				# Word spelled wrong
				elif eachWord.lower() not in suggestionList:
					misspelled.append(eachWord.lower())	
					
					if eachWord.lower() not in allMisspelled:
						allMisspelled.append(eachWord.lower())
			
			numIncorrectWords = len(misspelled)
			numGibberishWords = len(gibberish)
			pctIncorrectWords = (100.0 * numIncorrectWords) / numInputWords if numInputWords != 0 else 0
			pctGibberishWords = (100.0 * numGibberishWords) / numInputWords if numInputWords != 0 else 0			
			numIncorrectChars = sum( [len(eachWord) for eachWord in misspelled] )
			numGibberishChars = sum( [len(eachWord) for eachWord in gibberish] )			
			pctIncorrectChars = (100.0 * numIncorrectChars) / numInputChars if numInputChars != 0 else 0
			pctGibberishChars = (100.0 * numGibberishChars) / numInputChars if numInputChars != 0 else 0		
			
			pointsPossible += (100 * self.emphasisDict[i])
			
			pointsByWords = (((pctIncorrectWords) + (pctGibberishWords * int(self.var_gibberishWeight.get()))) / (1 + int(self.var_gibberishWeight.get()))) * self.emphasisDict[i]
			pointsByChars = (((pctIncorrectChars) + (pctGibberishChars * int(self.var_gibberishWeight.get()))) / (1 + int(self.var_gibberishWeight.get()))) * self.emphasisDict[i]
			
			calculationMethod = self.lst_calculationMethod.index(self.var_calculationMethod.get())
			
			pointsEarnedForThisField = 0
			
			if calculationMethod == 0:
				pointsEarnedForThisField = pointsByWords
			elif calculationMethod == 1:
				pointsEarnedForThisField = pointsByChars
			elif calculationMethod == 4:
				pointsEarnedForThisField = (pointsByWords + pointsByChars) / 2
			elif calculationMethod == 2:
				pointsEarnedForThisField = max(pointsByWords, pointsByChars)
			elif calculationMethod == 3:
				pointsEarnedForThisField = min(pointsByWords, pointsByChars)
			else:
				pointsEarnedForThisField = 0
				
			if pointsEarnedForThisField > 0 and self.fieldNames[i] not in fieldsContributingToScore:
				fieldsContributingToScore.append(self.fieldNames[i])
				
			pointsEarned += pointsEarnedForThisField

			if (pointsEarnedForThisField / self.emphasisDict[i]) > highestFieldScore:
				highestFieldScore = (pointsEarnedForThisField / self.emphasisDict[i])
				highestContributorFieldName = self.fieldNames[i]
				highestContributorFieldValue = myInput
				#output1.write("Highest field score set to %d, highest contributor changed to %s\n" % (highestFieldScore, highestContributorFieldName))
				
			totalFieldsCheckedForThisRespondent += 1 
			
		# (Highest + Average) / 2
		if self.lst_overallCalculationMethod.index(self.var_overallCalculationMethod.get()) == 0:
			thisRespondentScrutinyScore = 0 if pointsPossible == 0 else (((pointsEarned * 100) / pointsPossible) + highestFieldScore) / 2
		
		# Highest field
		elif self.lst_overallCalculationMethod.index(self.var_overallCalculationMethod.get()) == 1:
			thisRespondentScrutinyScore = highestFieldScore
		
		# Average of all fields
		elif self.lst_overallCalculationMethod.index(self.var_overallCalculationMethod.get()) == 2:
			thisRespondentScrutinyScore = 0 if pointsPossible == 0 else (pointsEarned * 100) / pointsPossible
			
		adjustedScrutinyScore = min(100, (100 * (math.log10( (thisRespondentScrutinyScore * 10) + 1))) / 3)
		# adjustedScrutinyScore = thisRespondentScrutinyScore
		
		# Auto-100
		if automatic100:
			adjustedScrutinyScore = 100.0
			
		# Minimum 74 score if any gibberish
		if len(allGibberish) > 0:
			adjustedScrutinyScore = max(adjustedScrutinyScore, 74.0)
		
		if fieldsContributingToScore != []:
			fieldsContributingToScore.remove(highestContributorFieldName)
		
		self.scrutinyDict[ int(adjustedScrutinyScore) ] += 1
		
		#print("Attempting to write data for respondent %d (%s)" % (respondentToCheck, thisIdentifier))
		try:
			output1.write( "%s\t%d\t%.2f\t%s\t%s\t%s\t%s\t%s\t%s\t%d\t%d\t%d\t%d\n" % (thisIdentifier, totalFieldsCheckedForThisRespondent, adjustedScrutinyScore, highestContributorFieldName.strip(), highestContributorFieldValue.strip(), ", ".join(fieldsContributingToScore), ", ".join(allMisspelled), ", ".join(allGibberish), ", ".join(allOffensive), totalWords, len(allMisspelled), len(allGibberish), len(allOffensive)) )
		except Exception:
			pass
		output1.close()
		
	def getProperNouns(self):
	
		output3 = open("[Proper nouns] " + self.currentOutputFilename + ".txt", "w")
	
		output3.write("Word\tUses\n")
	
		for eachKey in self.gibberishDict.keys():
			try:
				if self.gibberishDict[eachKey] >= 2:
					output3.write("%s\t%d\n" % (eachKey, self.gibberishDict[eachKey]))
			except Exception:
				pass
		
		output3.close()
		
	def outputResultsAsExcel(self):
	
		# Create the excel file
		myWorkbook = xlwt.Workbook()
		
		# Scrutiny score data sheet
		infoSheet = myWorkbook.add_sheet("Information")
		scrutinyScoreDataSheet = myWorkbook.add_sheet("Scrutiny score data")
		properNounSheet = myWorkbook.add_sheet("Proper nouns")
	
		# Prep column widths
		infoSheet.col(1).width = 256 * 48		# 47.29
		infoSheet.col(2).width = 256 * 48
		scrutinyScoreDataSheet.col(0).width = 256 * 17		# Respondent ID
		scrutinyScoreDataSheet.col(1).width = 256 * 20		# Scrutiny score
		scrutinyScoreDataSheet.col(2).width = 256 * 20		# Total fields checked
		scrutinyScoreDataSheet.col(3).width = 256 * 15		# Total words
		scrutinyScoreDataSheet.col(4).width = 256 * 15		# Num misspelled
		scrutinyScoreDataSheet.col(5).width = 256 * 15		# Num gibberish
		scrutinyScoreDataSheet.col(6).width = 256 * 15		# Num offensive
		scrutinyScoreDataSheet.col(7).width = 256 * 20		# Top contributor
		scrutinyScoreDataSheet.col(8).width = 256 * 56		# Value of field
		scrutinyScoreDataSheet.col(9).width = 256 * 24		# Other contributors
		scrutinyScoreDataSheet.col(10).width = 256 * 42		# Misspelled words
		scrutinyScoreDataSheet.col(11).width = 256 * 42		# Gibberish words
		scrutinyScoreDataSheet.col(12).width = 256 * 42		# Offensive words
		properNounSheet.col(0).width = 256 * 24
		properNounSheet.col(1).width = 256 * 12
		
		# Write to the info sheet
		style = xlwt.easyxf("pattern: pattern solid, fore_color pale_blue;")
		for row in range(1, 9):
			for col in range(1, 9):
				if row == 1 and col == 1:
					text = "This file was automatically generated by Ed's gibberish detector."
				elif row == 3 and col == 1:
					text = "The program accepts a data file in either tab-delimited text or Excel format, and assigns a scrutiny score to each respondent based on the contents of their open-ended responses."
				elif row == 4 and col == 1:
					text = "Please refer to the \"Scrutiny score data\" tab of this document for the scores."
				elif row == 5 and col == 1:
					text = "Scrutiny scores range from 0 to 100; the higher the number, the more closely the respondent should be considered for disqualification."
				elif row == 7 and col == 1:
					text = "WARNING: This document should not be used by itself to identify respondents to disqualify."
				elif row == 8 and col == 1:
					text = "Please consult the program documentation for further notes and explanations."
				else:
					text = ""
					
				infoSheet.write(row, col, text, style)
				
		infoSheet.write(10, 1, "Program name")
		infoSheet.write(10, 2, self.name)
		
		infoSheet.write(11, 1, "Program version")
		infoSheet.write(11, 2, self.version)
	
		infoSheet.write(12, 1, "Time of file creation")
		infoSheet.write(12, 2, str(datetime.datetime.now()))
		
		infoSheet.write(13, 1, "Analysis time")
		infoSheet.write(13, 2, self.formatTime(self.timeElapsed))
		
		infoSheet.write(14, 1, "Number of respondents")
		infoSheet.write(14, 2, self.numRespondents)
		
		infoSheet.write(15, 1, "Number of 0 scores")
		infoSheet.write(15, 2, self.scrutinyDict[0])
		
		infoSheet.write(16, 1, "Number of 100 scores")
		infoSheet.write(16, 2, self.scrutinyDict[100])
		

		# Write to the scrutiny score sheet
		style = xlwt.easyxf("alignment: wrap True;")
		input_results = open("[Partial results] " + self.currentOutputFilename + ".txt", "r")
		isFirstLine = True
		numLinesRead = 0
		
		for eachLine in input_results:
		
			if isFirstLine:
				isFirstLine = False
				numLinesRead = 1
				scrutinyScoreDataSheet.write(0, 0, "Respondent ID")
				scrutinyScoreDataSheet.write(0, 1, "Scrutiny score")
				scrutinyScoreDataSheet.write(0, 2, "Total fields checked")
				scrutinyScoreDataSheet.write(0, 3, "Total words")
				scrutinyScoreDataSheet.write(0, 4, "Num mispelled")
				scrutinyScoreDataSheet.write(0, 5, "Num gibberish")
				scrutinyScoreDataSheet.write(0, 6, "Num offensive")
				scrutinyScoreDataSheet.write(0, 7, "Top contributor")
				scrutinyScoreDataSheet.write(0, 8, "Value of field")
				scrutinyScoreDataSheet.write(0, 9, "Other score contributors")
				scrutinyScoreDataSheet.write(0, 10, "Misspelled words")
				scrutinyScoreDataSheet.write(0, 11, "Gibberish words")
				scrutinyScoreDataSheet.write(0, 12, "Offensive words")
				continue
				
			splitLine = eachLine.split("\t")
			
			# if splitLine[2] == "0.00":
			# 	continue
			
			for i in range( len(splitLine) ):

				""" 
				0 (thisIdentifier, 
				1 totalFieldsCheckedForThisRespondent, 
				2 adjustedScrutinyScore, 
				3 highestContributorFieldName.strip(), 
				4 highestContributorFieldValue.strip(), 
				5 ", ".join(fieldsContributingToScore), 
				6 ", ".join(allMisspelled), 
				7 ", ".join(allGibberish), 
				8 ", ".join(allOffensive), 
				9 totalWords, 
				10 len(allMisspelled), 
				11 len(allGibberish), 
				12 len(allOffensive))
				"""
				
				# Respondent ID
				if i == 0:
					if self.var_respondentIdentifier.get() == "record":
						scrutinyScoreDataSheet.write(numLinesRead, 0, int(splitLine[0]))
					else:
						scrutinyScoreDataSheet.write(numLinesRead, 0, splitLine[0].strip())
				
				# Scrutiny score
				elif i == 1:
					scrutinyScoreDataSheet.write(numLinesRead, 1, float(splitLine[2]))
				
				# Total fields checked
				elif i == 2:
					scrutinyScoreDataSheet.write(numLinesRead, 2, int(splitLine[1]))
					
				# Total words
				elif i == 3:
					scrutinyScoreDataSheet.write(numLinesRead, 3, int(splitLine[9]))
					
				# Number misspelled
				elif i == 4:
					scrutinyScoreDataSheet.write(numLinesRead, 4, int(splitLine[10]))
					
				# Number gibberish
				elif i == 5:
					scrutinyScoreDataSheet.write(numLinesRead, 5, int(splitLine[11]))
					
				# Number offensive
				elif i == 6:
					scrutinyScoreDataSheet.write(numLinesRead, 6, int(splitLine[12]))
					
				# Top contributor
				elif i == 7:
					scrutinyScoreDataSheet.write(numLinesRead, 7, splitLine[3].strip(), style)
					
				# Value of field
				elif i == 8:
					scrutinyScoreDataSheet.write(numLinesRead, 8, splitLine[4].strip(), style)
					
				# Other contributors
				elif i == 9:
					scrutinyScoreDataSheet.write(numLinesRead, 9, splitLine[5].strip(), style)
					
				# Misspelled words
				elif i == 10:
					scrutinyScoreDataSheet.write(numLinesRead, 10, splitLine[6].strip(), style)
					
				# Gibberish words
				elif i == 11:
					scrutinyScoreDataSheet.write(numLinesRead, 11, splitLine[7].strip(), style)
					
				# Offensive words
				elif i == 12:
					scrutinyScoreDataSheet.write(numLinesRead, 12, splitLine[8].strip(), style)	
				
			numLinesRead += 1
		
		input_results.close()
		
		# Write to the proper nouns sheet
		input_nouns = open("[Proper nouns] " + self.currentOutputFilename + ".txt", "r")
		isFirstLine = True
		numLinesRead = 0
		
		for eachLine in input_nouns:
		
			if isFirstLine:
				isFirstLine = False
				numLinesRead = 1
				properNounSheet.write(0, 0, "Word")
				properNounSheet.write(0, 1, "Usage count")
				continue
				
			splitLine = eachLine.split("\t")
			for i in range( len(splitLine) ):
				if i == 0:
					properNounSheet.write(numLinesRead, i, splitLine[i])
				elif i == 1:
					properNounSheet.write(numLinesRead, i, int(splitLine[i]))
			
			numLinesRead += 1
				
		input_nouns.close()
		
		myWorkbook.save("[Report] " + self.currentOutputFilename + ".xls")
		
	def formatTime(self, numSeconds):
	
		numHours = int(numSeconds / 3600)
		numMinutes = int((numSeconds % 3600) / 60)
		numSeconds = int((numSeconds % 3600) % 60)
		
		return "%s:%s:%s" % (str(numHours), "0" + str(numMinutes) if numMinutes < 10 else str(numMinutes), "0" + str(numSeconds) if numSeconds < 10 else str(numSeconds))
	
	def estimateTimeRemaining(self, done, total, elapsed):
	
		percentDone = (1.0 * done) / total
		percentRemaining = 1.0 - percentDone

		if total != 0 and done != 0:
			if int(elapsed * (percentRemaining / percentDone)) < 60:
				return "less than 1 minute"
			else:
				return "about %d minutes" % ((int(elapsed * (percentRemaining / percentDone)) / 60) + 1)
		else:
			return "unknown"
			
	def redrawGraph(self):
	
		highestFrequency = 0
		
		for eachKey in self.scrutinyDict.keys():
			if eachKey == 0:
				continue
			if self.scrutinyDict[eachKey] > highestFrequency:
				highestFrequency = self.scrutinyDict[eachKey]
	
		for i in range(len(self.barsInGraph)):
			if i == 0:
				continue
			elif i == 101:
				self.graphCanvas.delete(self.barsInGraph[i])
				
				self.barsInGraph[i] = self.graphCanvas.create_text(30, 31, text=str(highestFrequency), font="Small_Fonts 8", anchor="e")
			else:
				self.graphCanvas.delete(self.barsInGraph[i])
				
				self.barsInGraph[i] = self.graphCanvas.create_rectangle(self.ULX + 50 + (i * 4), self.graphMaxY - 25, self.ULX + 50 + (i * 4) + 4, self.graphMaxY - 25 - ((200.0 * self.scrutinyDict[i]) / highestFrequency if highestFrequency > 0 else 0), fill=self.colorDict[i] if self.scrutinyDict[i] > 0 else "black", outline="black" if self.scrutinyDict[i] > 0 else "")
		
		#if not(self.showGraph):
		#	return
		
#	def tryToSeparateWords(self, joinedWord):
#	
#		for i in range(1, len(joinedWord) - 1):
#		
#			wordA = joinedWord[0:i]
#			wordB = joinedWord[i:]
#			
#			if wordA in self.mySpellChecker.known([wordA]) and wordB in self.mySpellChecker.known([wordB]):
#				return [wordA, wordB]
#				
#		return [joinedWord]
	
	def toggleGraph(self):
	
		self.showGraph = not(self.showGraph)
	
	def doNothing(self):
		
		messagebox.showinfo("Notice", "This didn't do anything.")
	
if __name__ == "__main__":
	
	try:
		thisGUI = myGUI()
	
	except Exception:
		errfile = open("error.txt", "w")
		errfile.write(traceback.format_exc())
		errfile.close()
		
		input("An error has occurred; please check error.txt for details.  Press Enter to close.")