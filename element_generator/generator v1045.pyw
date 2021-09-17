from tkinter import *
import re

#==================================================
# TO-DO LIST
#==================================================

# Add checkbox to element generator: evenly space attributes

#==================================================
# FUNCTION DEFINITIONS
#==================================================
def questionGenerate(textarea):
    outputString = ""

    # Generic radio question
    if var_questionGeneratorValue.get() == lst_questionGeneratorOptions[0]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
        
    # Generic checkbox question
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[1]:
        outputString += "<checkbox label=\"Q#\" atleast=\"1\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select all that apply.</comment>\n"
        outputString += "@elements\n"
        outputString += "</checkbox>"
        
    # Generic select question
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[2]:
        outputString += "<select label=\"Q#\" optional=\"0\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "@elements\n"
        outputString += "</select>"
        
    # Generic number question
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[3]:
        outputString += "<number label=\"Q#\" optional=\"0\" size=\"#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter a whole number.</comment>\n"
        outputString += "@elements\n"
        outputString += "</number>"
        
    # Generic text question
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[4]:
        outputString += "<text label=\"Q#\" optional=\"0\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please be as specific as possible.</comment>\n"
        outputString += "@elements\n"
        outputString += "</text>"
        
    # Generic textarea question
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[5]:
        outputString += "<textarea label=\"Q#\" optional=\"0\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please be as specific as possible.</comment>\n"
        outputString += "@elements\n"
        outputString += "</textarea>"
        
    # HTML element
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[6]:
        outputString += "<html label=\"#\">\n"
        outputString += "Place HTML content here\n"
        outputString += "</html>"
        
    # Radio question: Yes/No
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[7]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"r1\" value=\"1\">Yes</row>\n"
        outputString += "<row label=\"r2\" value=\"2\">No</row>\n"
        outputString += "</radio>"
        
    # Radio question: Gender
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[8]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"r1\" value=\"1\">Male</row>\n"
        outputString += "<row label=\"r2\" value=\"2\">Female</row>\n"
        outputString += "</radio>"
        
    # Radio question: Age
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[9]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"r1\" value=\"1\">Under 18</row>\n"
        outputString += "<row label=\"r2\" value=\"2\">18-24</row>\n"
        outputString += "<row label=\"r3\" value=\"3\">25-34</row>\n"
        outputString += "<row label=\"r4\" value=\"4\">35-44</row>\n"
        outputString += "<row label=\"r5\" value=\"5\">45-54</row>\n"
        outputString += "<row label=\"r6\" value=\"6\">55-64</row>\n"
        outputString += "<row label=\"r7\" value=\"7\">65 or older</row>\n"
        outputString += "</radio>"
        
    # Radio question: Income
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[10]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"r1\" value=\"1\">Less than $25,000</row>\n"
        outputString += "<row label=\"r2\" value=\"2\">$25,000 - $49,999</row>\n"
        outputString += "<row label=\"r3\" value=\"3\">$50,000 - $74,999</row>\n"
        outputString += "<row label=\"r4\" value=\"4\">$75,000 - $99,999</row>\n"
        outputString += "<row label=\"r5\" value=\"5\">$100,000 - $149,999</row>\n"
        outputString += "<row label=\"r6\" value=\"6\">$150,000 - $199,999</row>\n"
        outputString += "<row label=\"r7\" value=\"7\">$200,000 or more</row>\n"
        outputString += "<row label=\"r99\" value=\"99\">Prefer not to answer</row>\n"
        outputString += "</radio>"
        
    # Radio question: Ethnicity
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[11]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"r1\" value=\"1\">White or Caucasian</row>\n"
        outputString += "<row label=\"r2\" value=\"2\">Black or African American</row>\n"
        outputString += "<row label=\"r3\" value=\"3\">Asian</row>\n"
        outputString += "<row label=\"r4\" value=\"4\">American Indian, Alaska Native, Native Hawaiian or other Pacific Islander</row>\n"
        outputString += "<row label=\"r98\" value=\"98\">Some other ethnicity</row>\n"
        outputString += "<row label=\"r99\" value=\"99\">Prefer not to answer</row>\n"
        outputString += "</radio>"
        
    # Radio question: US State
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[12]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title/title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"rAL\">Alabama</row>\n"
        outputString += "<row label=\"rAK\">Alaska</row>\n"
        outputString += "<row label=\"rAZ\">Arizona</row>\n"
        outputString += "<row label=\"rAR\">Arkansas</row>\n"
        outputString += "<row label=\"rCA\">California</row>\n"
        outputString += "<row label=\"rCO\">Colorado</row>\n"
        outputString += "<row label=\"rCT\">Connecticut</row>\n"
        outputString += "<row label=\"rDE\">Delaware</row>\n"
        outputString += "<row label=\"rDC\">District of Columbia</row>\n"
        outputString += "<row label=\"rFL\">Florida</row>\n"
        outputString += "<row label=\"rGA\">Georgia</row>\n"
        outputString += "<row label=\"rHI\">Hawaii</row>\n"
        outputString += "<row label=\"rID\">Idaho</row>\n"
        outputString += "<row label=\"rIL\">Illinois</row>\n"
        outputString += "<row label=\"rIN\">Indiana</row>\n"
        outputString += "<row label=\"rIA\">Iowa</row>\n"
        outputString += "<row label=\"rKS\">Kansas</row>\n"
        outputString += "<row label=\"rKY\">Kentucky</row>\n"
        outputString += "<row label=\"rLA\">Louisiana</row>\n"
        outputString += "<row label=\"rME\">Maine</row>\n"
        outputString += "<row label=\"rMD\">Maryland</row>\n"
        outputString += "<row label=\"rMA\">Massachusetts</row>\n"
        outputString += "<row label=\"rMI\">Michigan</row>\n"
        outputString += "<row label=\"rMN\">Minnesota</row>\n"
        outputString += "<row label=\"rMS\">Mississippi</row>\n"
        outputString += "<row label=\"rMO\">Missouri</row>\n"
        outputString += "<row label=\"rMT\">Montana</row>\n"
        outputString += "<row label=\"rNE\">Nebraska</row>\n"
        outputString += "<row label=\"rNV\">Nevada</row>\n"
        outputString += "<row label=\"rNH\">New Hampshire</row>\n"
        outputString += "<row label=\"rNJ\">New Jersey</row>\n"
        outputString += "<row label=\"rNM\">New Mexico</row>\n"
        outputString += "<row label=\"rNY\">New York</row>\n"
        outputString += "<row label=\"rNC\">North Carolina</row>\n"
        outputString += "<row label=\"rND\">North Dakota</row>\n"
        outputString += "<row label=\"rOH\">Ohio</row>\n"
        outputString += "<row label=\"rOK\">Oklahoma</row>\n"
        outputString += "<row label=\"rOR\">Oregon</row>\n"
        outputString += "<row label=\"rPA\">Pennsylvania</row>\n"
        outputString += "<row label=\"rRI\">Rhode Island</row>\n"
        outputString += "<row label=\"rSC\">South Carolina</row>\n"
        outputString += "<row label=\"rSD\">South Dakota</row>\n"
        outputString += "<row label=\"rTN\">Tennessee</row>\n"
        outputString += "<row label=\"rTX\">Texas</row>\n"
        outputString += "<row label=\"rUT\">Utah</row>\n"
        outputString += "<row label=\"rVT\">Vermont</row>\n"
        outputString += "<row label=\"rVA\">Virginia</row>\n"
        outputString += "<row label=\"rWA\">Washington</row>\n"
        outputString += "<row label=\"rWV\">West Virginia</row>\n"
        outputString += "<row label=\"rWI\">Wisconsin</row>\n"
        outputString += "<row label=\"rWY\">Wyoming</row>\n"
        outputString += "</radio>"
        
    # Radio question: US state with region punch
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[13]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"rAL\">Alabama</row>\n"
        outputString += "<row label=\"rAK\">Alaska</row>\n"
        outputString += "<row label=\"rAZ\">Arizona</row>\n"
        outputString += "<row label=\"rAR\">Arkansas</row>\n"
        outputString += "<row label=\"rCA\">California</row>\n"
        outputString += "<row label=\"rCO\">Colorado</row>\n"
        outputString += "<row label=\"rCT\">Connecticut</row>\n"
        outputString += "<row label=\"rDE\">Delaware</row>\n"
        outputString += "<row label=\"rDC\">District of Columbia</row>\n"
        outputString += "<row label=\"rFL\">Florida</row>\n"
        outputString += "<row label=\"rGA\">Georgia</row>\n"
        outputString += "<row label=\"rHI\">Hawaii</row>\n"
        outputString += "<row label=\"rID\">Idaho</row>\n"
        outputString += "<row label=\"rIL\">Illinois</row>\n"
        outputString += "<row label=\"rIN\">Indiana</row>\n"
        outputString += "<row label=\"rIA\">Iowa</row>\n"
        outputString += "<row label=\"rKS\">Kansas</row>\n"
        outputString += "<row label=\"rKY\">Kentucky</row>\n"
        outputString += "<row label=\"rLA\">Louisiana</row>\n"
        outputString += "<row label=\"rME\">Maine</row>\n"
        outputString += "<row label=\"rMD\">Maryland</row>\n"
        outputString += "<row label=\"rMA\">Massachusetts</row>\n"
        outputString += "<row label=\"rMI\">Michigan</row>\n"
        outputString += "<row label=\"rMN\">Minnesota</row>\n"
        outputString += "<row label=\"rMS\">Mississippi</row>\n"
        outputString += "<row label=\"rMO\">Missouri</row>\n"
        outputString += "<row label=\"rMT\">Montana</row>\n"
        outputString += "<row label=\"rNE\">Nebraska</row>\n"
        outputString += "<row label=\"rNV\">Nevada</row>\n"
        outputString += "<row label=\"rNH\">New Hampshire</row>\n"
        outputString += "<row label=\"rNJ\">New Jersey</row>\n"
        outputString += "<row label=\"rNM\">New Mexico</row>\n"
        outputString += "<row label=\"rNY\">New York</row>\n"
        outputString += "<row label=\"rNC\">North Carolina</row>\n"
        outputString += "<row label=\"rND\">North Dakota</row>\n"
        outputString += "<row label=\"rOH\">Ohio</row>\n"
        outputString += "<row label=\"rOK\">Oklahoma</row>\n"
        outputString += "<row label=\"rOR\">Oregon</row>\n"
        outputString += "<row label=\"rPA\">Pennsylvania</row>\n"
        outputString += "<row label=\"rRI\">Rhode Island</row>\n"
        outputString += "<row label=\"rSC\">South Carolina</row>\n"
        outputString += "<row label=\"rSD\">South Dakota</row>\n"
        outputString += "<row label=\"rTN\">Tennessee</row>\n"
        outputString += "<row label=\"rTX\">Texas</row>\n"
        outputString += "<row label=\"rUT\">Utah</row>\n"
        outputString += "<row label=\"rVT\">Vermont</row>\n"
        outputString += "<row label=\"rVA\">Virginia</row>\n"
        outputString += "<row label=\"rWA\">Washington</row>\n"
        outputString += "<row label=\"rWV\">West Virginia</row>\n"
        outputString += "<row label=\"rWI\">Wisconsin</row>\n"
        outputString += "<row label=\"rWY\">Wyoming</row>\n"
        outputString += "</radio>\n\n"
        outputString += "<suspend/>\n\n"
        outputString += "<exec>\n"
        outputString += "myState = Q#.selected.label[-2:]\n\n"
        outputString += "if myState in [\"CT\", \"ME\", \"MA\", \"NH\", \"NJ\", \"NY\", \"PA\", \"RI\", \"VT\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r1.index\n"
        outputString += "elif myState in [\"IL\", \"IN\", \"MI\", \"OH\", \"WI\", \"IA\", \"KS\", \"MN\", \"MO\", \"NE\", \"ND\", \"SD\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r2.index\n"
        outputString += "elif myState in [\"DE\", \"FL\", \"GA\", \"MD\", \"NC\", \"SC\", \"VA\", \"DC\", \"WV\", \"AL\", \"KY\", \"MS\", \"TN\", \"AR\", \"LA\", \"OK\", \"TX\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r3.index\n"
        outputString += "elif myState in [\"AZ\", \"CO\", \"ID\", \"MT\", \"NV\", \"NM\", \"UT\", \"WY\", \"AK\", \"CA\", \"HI\", \"OR\", \"WA\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r4.index\n\n"
        outputString += "if myState in [\"WA\", \"OR\", \"CA\", \"AK\", \"HI\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r1.index\n"
        outputString += "elif myState in [\"MT\", \"ID\", \"WY\", \"CO\", \"UT\", \"NV\", \"AZ\", \"NM\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r2.index\n"
        outputString += "elif myState in [\"ND\", \"MN\", \"SD\", \"NE\", \"IA\", \"KS\", \"MO\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r3.index\n"
        outputString += "elif myState in [\"OK\", \"AR\", \"TX\", \"LA\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r4.index\n"
        outputString += "elif myState in [\"MI\", \"WI\", \"IN\", \"IL\", \"OH\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r5.index\n"
        outputString += "elif myState in [\"KY\", \"TN\", \"MS\", \"AL\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r6.index\n"
        outputString += "elif myState in [\"ME\", \"NH\", \"VT\", \"MA\", \"CT\", \"RI\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r7.index\n"
        outputString += "elif myState in [\"NY\", \"PA\", \"NJ\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r8.index\n"
        outputString += "elif myState in [\"WV\", \"MD\", \"DE\", \"DC\", \"VA\", \"NC\", \"SC\", \"GA\", \"FL\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r9.index\n"
        outputString += "</exec>\n\n"
        outputString += "<radio label=\"HP_region4\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Region4</title>\n"
        outputString += "<row label=\"r1\">Northeast</row>\n"
        outputString += "<row label=\"r2\">Midwest</row>\n"
        outputString += "<row label=\"r3\">South</row>\n"
        outputString += "<row label=\"r4\">West</row>\n"
        outputString += "</radio>\n\n"
        outputString += "<radio label=\"HP_region9\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Region9</title>\n"
        outputString += "<row label=\"r1\">Pacific</row>\n"
        outputString += "<row label=\"r2\">Mountain</row>\n"
        outputString += "<row label=\"r3\">West North Central</row>\n"
        outputString += "<row label=\"r4\">West South Central</row>\n"
        outputString += "<row label=\"r5\">East North Central</row>\n"
        outputString += "<row label=\"r6\">East South Central</row>\n"
        outputString += "<row label=\"r7\">New England</row>\n"
        outputString += "<row label=\"r8\">Mid Atlantic</row>\n"
        outputString += "<row label=\"r9\">South Atlantic</row>\n"
        outputString += "</radio>"
    
    # Radio question: 0-5 scale
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[14]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c0\" value=\"0\">Left Extreme<br/>0</col>\n"
        outputString += "<col label=\"c1\" value=\"1\">1</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">2</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">3</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">4</col>\n"
        outputString += "<col label=\"c5\" value=\"5\">Right Extreme<br/>5</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
        
    # Radio question: 1-5 scale
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[15]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c1\" value=\"1\">Left Extreme<br/>1</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">2</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">3</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">4</col>\n"
        outputString += "<col label=\"c5\" value=\"5\">Right Extreme<br/>5</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
        
    # Radio question: 0-7 scale
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[16]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c0\" value=\"0\">Left Extreme<br/>0</col>\n"
        outputString += "<col label=\"c1\" value=\"1\">1</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">2</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">3</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">4</col>\n"
        outputString += "<col label=\"c5\" value=\"5\">5</col>\n"
        outputString += "<col label=\"c6\" value=\"6\">6</col>\n"
        outputString += "<col label=\"c7\" value=\"7\">Right Extreme<br/>7</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
        
    # Radio question: 1-7 scale
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[17]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c1\" value=\"1\">Left Extreme<br/>1</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">2</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">3</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">4</col>\n"
        outputString += "<col label=\"c5\" value=\"5\">5</col>\n"
        outputString += "<col label=\"c6\" value=\"6\">6</col>\n"
        outputString += "<col label=\"c7\" value=\"7\">Right Extreme<br/>7</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
        
    # Radio question: 0-10 scale
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[18]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c0\" value=\"0\">Left Extreme<br/>0</col>\n"
        outputString += "<col label=\"c1\" value=\"1\">1</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">2</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">3</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">4</col>\n"
        outputString += "<col label=\"c5\" value=\"5\">5</col>\n"
        outputString += "<col label=\"c6\" value=\"6\">6</col>\n"
        outputString += "<col label=\"c7\" value=\"7\">7</col>\n"
        outputString += "<col label=\"c8\" value=\"8\">8</col>\n"
        outputString += "<col label=\"c9\" value=\"9\">9</col>\n"
        outputString += "<col label=\"c10\" value=\"10\">Right Extreme<br/>10</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
        
    # Radio question: 1-10 scale
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[19]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c1\" value=\"1\">Left Extreme<br/>1</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">2</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">3</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">4</col>\n"
        outputString += "<col label=\"c5\" value=\"5\">5</col>\n"
        outputString += "<col label=\"c6\" value=\"6\">6</col>\n"
        outputString += "<col label=\"c7\" value=\"7\">7</col>\n"
        outputString += "<col label=\"c8\" value=\"8\">8</col>\n"
        outputString += "<col label=\"c9\" value=\"9\">9</col>\n"
        outputString += "<col label=\"c10\" value=\"10\">Right Extreme<br/>10</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
        
    # Checkbox question: Ethnicity
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[20]:
        outputString += "<checkbox label=\"Q#\" atleast=\"1\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select all that apply.</comment>\n"
        outputString += "<row label=\"r1\">White or Caucasian</row>\n"
        outputString += "<row label=\"r2\">Black or African American</row>\n"
        outputString += "<row label=\"r3\">Asian</row>\n"
        outputString += "<row label=\"r4\">American Indian, Alaska Native, Native Hawaiian or other Pacific Islander</row>\n"
        outputString += "<row label=\"r5\">Some other ethnicity</row>\n"
        outputString += "<row label=\"r6\" exclusive=\"1\">Prefer not to answer</row>\n"
        outputString += "</checkbox>"
        
    # Select question: US state
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[21]:
        outputString += "<select label=\"Q#\" optional=\"0\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<choice label=\"chAL\">Alabama</choice>\n"
        outputString += "<choice label=\"chAK\">Alaska</choice>\n"
        outputString += "<choice label=\"chAZ\">Arizona</choice>\n"
        outputString += "<choice label=\"chAR\">Arkansas</choice>\n"
        outputString += "<choice label=\"chCA\">California</choice>\n"
        outputString += "<choice label=\"chCO\">Colorado</choice>\n"
        outputString += "<choice label=\"chCT\">Connecticut</choice>\n"
        outputString += "<choice label=\"chDE\">Delaware</choice>\n"
        outputString += "<choice label=\"chDC\">District of Columbia</choice>\n"
        outputString += "<choice label=\"chFL\">Florida</choice>\n"
        outputString += "<choice label=\"chGA\">Georgia</choice>\n"
        outputString += "<choice label=\"chHI\">Hawaii</choice>\n"
        outputString += "<choice label=\"chID\">Idaho</choice>\n"
        outputString += "<choice label=\"chIL\">Illinois</choice>\n"
        outputString += "<choice label=\"chIN\">Indiana</choice>\n"
        outputString += "<choice label=\"chIA\">Iowa</choice>\n"
        outputString += "<choice label=\"chKS\">Kansas</choice>\n"
        outputString += "<choice label=\"chKY\">Kentucky</choice>\n"
        outputString += "<choice label=\"chLA\">Louisiana</choice>\n"
        outputString += "<choice label=\"chME\">Maine</choice>\n"
        outputString += "<choice label=\"chMD\">Maryland</choice>\n"
        outputString += "<choice label=\"chMA\">Massachusetts</choice>\n"
        outputString += "<choice label=\"chMI\">Michigan</choice>\n"
        outputString += "<choice label=\"chMN\">Minnesota</choice>\n"
        outputString += "<choice label=\"chMS\">Mississippi</choice>\n"
        outputString += "<choice label=\"chMO\">Missouri</choice>\n"
        outputString += "<choice label=\"chMT\">Montana</choice>\n"
        outputString += "<choice label=\"chNE\">Nebraska</choice>\n"
        outputString += "<choice label=\"chNV\">Nevada</choice>\n"
        outputString += "<choice label=\"chNH\">New Hampshire</choice>\n"
        outputString += "<choice label=\"chNJ\">New Jersey</choice>\n"
        outputString += "<choice label=\"chNM\">New Mexico</choice>\n"
        outputString += "<choice label=\"chNY\">New York</choice>\n"
        outputString += "<choice label=\"chNC\">North Carolina</choice>\n"
        outputString += "<choice label=\"chND\">North Dakota</choice>\n"
        outputString += "<choice label=\"chOH\">Ohio</choice>\n"
        outputString += "<choice label=\"chOK\">Oklahoma</choice>\n"
        outputString += "<choice label=\"chOR\">Oregon</choice>\n"
        outputString += "<choice label=\"chPA\">Pennsylvania</choice>\n"
        outputString += "<choice label=\"chRI\">Rhode Island</choice>\n"
        outputString += "<choice label=\"chSC\">South Carolina</choice>\n"
        outputString += "<choice label=\"chSD\">South Dakota</choice>\n"
        outputString += "<choice label=\"chTN\">Tennessee</choice>\n"
        outputString += "<choice label=\"chTX\">Texas</choice>\n"
        outputString += "<choice label=\"chUT\">Utah</choice>\n"
        outputString += "<choice label=\"chVT\">Vermont</choice>\n"
        outputString += "<choice label=\"chVA\">Virginia</choice>\n"
        outputString += "<choice label=\"chWA\">Washington</choice>\n"
        outputString += "<choice label=\"chWV\">West Virginia</choice>\n"
        outputString += "<choice label=\"chWI\">Wisconsin</choice>\n"
        outputString += "<choice label=\"chWY\">Wyoming</choice>\n"
        outputString += "</select>"
        
    # Select question: US state with region punch
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[22]:
        outputString += "<select label=\"Q#\" optional=\"0\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<choice label=\"chAL\">Alabama</choice>\n"
        outputString += "<choice label=\"chAK\">Alaska</choice>\n"
        outputString += "<choice label=\"chAZ\">Arizona</choice>\n"
        outputString += "<choice label=\"chAR\">Arkansas</choice>\n"
        outputString += "<choice label=\"chCA\">California</choice>\n"
        outputString += "<choice label=\"chCO\">Colorado</choice>\n"
        outputString += "<choice label=\"chCT\">Connecticut</choice>\n"
        outputString += "<choice label=\"chDE\">Delaware</choice>\n"
        outputString += "<choice label=\"chDC\">District of Columbia</choice>\n"
        outputString += "<choice label=\"chFL\">Florida</choice>\n"
        outputString += "<choice label=\"chGA\">Georgia</choice>\n"
        outputString += "<choice label=\"chHI\">Hawaii</choice>\n"
        outputString += "<choice label=\"chID\">Idaho</choice>\n"
        outputString += "<choice label=\"chIL\">Illinois</choice>\n"
        outputString += "<choice label=\"chIN\">Indiana</choice>\n"
        outputString += "<choice label=\"chIA\">Iowa</choice>\n"
        outputString += "<choice label=\"chKS\">Kansas</choice>\n"
        outputString += "<choice label=\"chKY\">Kentucky</choice>\n"
        outputString += "<choice label=\"chLA\">Louisiana</choice>\n"
        outputString += "<choice label=\"chME\">Maine</choice>\n"
        outputString += "<choice label=\"chMD\">Maryland</choice>\n"
        outputString += "<choice label=\"chMA\">Massachusetts</choice>\n"
        outputString += "<choice label=\"chMI\">Michigan</choice>\n"
        outputString += "<choice label=\"chMN\">Minnesota</choice>\n"
        outputString += "<choice label=\"chMS\">Mississippi</choice>\n"
        outputString += "<choice label=\"chMO\">Missouri</choice>\n"
        outputString += "<choice label=\"chMT\">Montana</choice>\n"
        outputString += "<choice label=\"chNE\">Nebraska</choice>\n"
        outputString += "<choice label=\"chNV\">Nevada</choice>\n"
        outputString += "<choice label=\"chNH\">New Hampshire</choice>\n"
        outputString += "<choice label=\"chNJ\">New Jersey</choice>\n"
        outputString += "<choice label=\"chNM\">New Mexico</choice>\n"
        outputString += "<choice label=\"chNY\">New York</choice>\n"
        outputString += "<choice label=\"chNC\">North Carolina</choice>\n"
        outputString += "<choice label=\"chND\">North Dakota</choice>\n"
        outputString += "<choice label=\"chOH\">Ohio</choice>\n"
        outputString += "<choice label=\"chOK\">Oklahoma</choice>\n"
        outputString += "<choice label=\"chOR\">Oregon</choice>\n"
        outputString += "<choice label=\"chPA\">Pennsylvania</choice>\n"
        outputString += "<choice label=\"chRI\">Rhode Island</choice>\n"
        outputString += "<choice label=\"chSC\">South Carolina</choice>\n"
        outputString += "<choice label=\"chSD\">South Dakota</choice>\n"
        outputString += "<choice label=\"chTN\">Tennessee</choice>\n"
        outputString += "<choice label=\"chTX\">Texas</choice>\n"
        outputString += "<choice label=\"chUT\">Utah</choice>\n"
        outputString += "<choice label=\"chVT\">Vermont</choice>\n"
        outputString += "<choice label=\"chVA\">Virginia</choice>\n"
        outputString += "<choice label=\"chWA\">Washington</choice>\n"
        outputString += "<choice label=\"chWV\">West Virginia</choice>\n"
        outputString += "<choice label=\"chWI\">Wisconsin</choice>\n"
        outputString += "<choice label=\"chWY\">Wyoming</choice>\n"
        outputString += "</select>\n\n"
        outputString += "<suspend/>\n\n"
        outputString += "<exec>\n"
        outputString += "myState = Q#.selected.label[-2:]\n\n"
        outputString += "if myState in [\"CT\", \"ME\", \"MA\", \"NH\", \"NJ\", \"NY\", \"PA\", \"RI\", \"VT\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r1.index\n"
        outputString += "elif myState in [\"IL\", \"IN\", \"MI\", \"OH\", \"WI\", \"IA\", \"KS\", \"MN\", \"MO\", \"NE\", \"ND\", \"SD\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r2.index\n"
        outputString += "elif myState in [\"DE\", \"FL\", \"GA\", \"MD\", \"NC\", \"SC\", \"VA\", \"DC\", \"WV\", \"AL\", \"KY\", \"MS\", \"TN\", \"AR\", \"LA\", \"OK\", \"TX\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r3.index\n"
        outputString += "elif myState in [\"AZ\", \"CO\", \"ID\", \"MT\", \"NV\", \"NM\", \"UT\", \"WY\", \"AK\", \"CA\", \"HI\", \"OR\", \"WA\"]:\n"
        outputString += "    HP_region4.val = HP_region4.r4.index\n\n"
        outputString += "if myState in [\"WA\", \"OR\", \"CA\", \"AK\", \"HI\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r1.index\n"
        outputString += "elif myState in [\"MT\", \"ID\", \"WY\", \"CO\", \"UT\", \"NV\", \"AZ\", \"NM\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r2.index\n"
        outputString += "elif myState in [\"ND\", \"MN\", \"SD\", \"NE\", \"IA\", \"KS\", \"MO\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r3.index\n"
        outputString += "elif myState in [\"OK\", \"AR\", \"TX\", \"LA\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r4.index\n"
        outputString += "elif myState in [\"MI\", \"WI\", \"IN\", \"IL\", \"OH\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r5.index\n"
        outputString += "elif myState in [\"KY\", \"TN\", \"MS\", \"AL\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r6.index\n"
        outputString += "elif myState in [\"ME\", \"NH\", \"VT\", \"MA\", \"CT\", \"RI\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r7.index\n"
        outputString += "elif myState in [\"NY\", \"PA\", \"NJ\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r8.index\n"
        outputString += "elif myState in [\"WV\", \"MD\", \"DE\", \"DC\", \"VA\", \"NC\", \"SC\", \"GA\", \"FL\"]:\n"
        outputString += "    HP_region9.val = HP_region9.r9.index\n"
        outputString += "</exec>\n\n"
        outputString += "<radio label=\"HP_region4\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Region4</title>\n"
        outputString += "<row label=\"r1\">Northeast</row>\n"
        outputString += "<row label=\"r2\">Midwest</row>\n"
        outputString += "<row label=\"r3\">South</row>\n"
        outputString += "<row label=\"r4\">West</row>\n"
        outputString += "</radio>\n\n"
        outputString += "<radio label=\"HP_region9\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Region9</title>\n"
        outputString += "<row label=\"r1\">Pacific</row>\n"
        outputString += "<row label=\"r2\">Mountain</row>\n"
        outputString += "<row label=\"r3\">West North Central</row>\n"
        outputString += "<row label=\"r4\">West South Central</row>\n"
        outputString += "<row label=\"r5\">East North Central</row>\n"
        outputString += "<row label=\"r6\">East South Central</row>\n"
        outputString += "<row label=\"r7\">New England</row>\n"
        outputString += "<row label=\"r8\">Mid Atlantic</row>\n"
        outputString += "<row label=\"r9\">South Atlantic</row>\n"
        outputString += "</radio>"
    
    # Number question: Age
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[23]:
        outputString += "<number label=\"Q#\" optional=\"0\" size=\"3\" verify=\"range(0, 120)\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter a whole number.</comment>\n"
        outputString += "</number>"
        
    # Number question: Age with age group punch
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[24]:
        outputString += "<number label=\"Q#\" optional=\"0\" size=\"3\" verify=\"range(0, 120)\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter a whole number.</comment>\n"
        outputString += "</number>\n\n"
        outputString += "<suspend/>\n\n"
        outputString += "<radio label=\"HP_ageGroup\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Age group</title>\n"
        outputString += "<exec>\n"
        outputString += "if Q#.val in range(0, 18):\n"
        outputString += "    HP_ageGroup.val = HP_ageGroup.r1.index\n"
        outputString += "elif Q#.val in range(18, 25):\n"
        outputString += "    HP_ageGroup.val = HP_ageGroup.r2.index\n"
        outputString += "elif Q#.val in range(25, 35):\n"
        outputString += "    HP_ageGroup.val = HP_ageGroup.r3.index\n"
        outputString += "elif Q#.val in range(35, 45):\n"
        outputString += "    HP_ageGroup.val = HP_ageGroup.r4.index\n"
        outputString += "elif Q#.val in range(45, 55):\n"
        outputString += "    HP_ageGroup.val = HP_ageGroup.r5.index\n"
        outputString += "elif Q#.val in range(55, 65):\n"
        outputString += "    HP_ageGroup.val = HP_ageGroup.r6.index\n"
        outputString += "else:\n"
        outputString += "    HP_ageGroup.val = HP_ageGroup.r7.index\n"
        outputString += "</exec>\n"
        outputString += "<row label=\"r1\">Under 18</row>\n"
        outputString += "<row label=\"r2\">18-24</row>\n"
        outputString += "<row label=\"r3\">25-34</row>\n"
        outputString += "<row label=\"r4\">35-44</row>\n"
        outputString += "<row label=\"r5\">45-54</row>\n"
        outputString += "<row label=\"r6\">55-64</row>\n"
        outputString += "<row label=\"r7\">65 or older</row>\n"
        outputString += "</radio>"
    
    # Text question: Zipcode
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[25]:
        outputString += "<text label=\"Q#\" optional=\"0\" size=\"5\" verify=\"zipcode\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter the 5-digit code.</comment>\n"
        outputString += "</text>"
        
    # Text question: Zipcode with DMA template
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[26]:
        outputString += "<block label=\"DMA_BLOCK\" sst=\"0\">\n"
        outputString += "\n"
        outputString += "<text label=\"Q#\" optional=\"0\" size=\"5\" verify=\"zipcode\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter the 5-digit code.</comment>\n"
        outputString += "</text>\n"
        outputString += "\n"
        outputString += "<suspend/>\n"
        outputString += "\n"
        outputString += "<exec>\n"
        outputString += "p.zipCodeDict = dict(zcode=Q#.val)\n"
        outputString += "</exec>\n"
        outputString += "\n"
        outputString += "<logic label=\"zipCodeAPI\" api:params=\"p.zipCodeDict\" api:url=\"http://speeders.researchnow.com/zipcode/dmalookup.php\" uses=\"api.1\"/>\n"
        outputString += "<exec>\n"
        outputString += "if zipCodeAPI.status == 200:\n"
        outputString += "    try:\n"
        outputString += "        stateAbbreviation = zipCodeAPI.r[0]['STATE_ABV']\n"
        outputString += "        DMAcode = zipCodeAPI.r[0]['DMA_CODE']\n"
        outputString += "        success = True\n"
        outputString += "    except IndexError:\n"
        outputString += "        success = False\n"
        outputString += "else:\n"
        outputString += "    success = False\n"
        outputString += "\n"
        outputString += "if success:\n"
        outputString += "\n"
        outputString += "    # Map state to region4\n"
        outputString += "    if stateAbbreviation in [\"CT\", \"ME\", \"MA\", \"NH\", \"NJ\", \"NY\", \"PA\", \"RI\", \"VT\"]:\n"
        outputString += "        HP_region4.val = HP_region4.r1.index\n"
        outputString += "    elif stateAbbreviation in [\"IL\", \"IN\", \"MI\", \"OH\", \"WI\", \"IA\", \"KS\", \"MN\", \"MO\", \"NE\", \"ND\", \"SD\"]:\n"
        outputString += "        HP_region4.val = HP_region4.r2.index\n"
        outputString += "    elif stateAbbreviation in [\"DE\", \"FL\", \"GA\", \"MD\", \"NC\", \"SC\", \"VA\", \"DC\", \"WV\", \"AL\", \"KY\", \"MS\", \"TN\", \"AR\", \"LA\", \"OK\", \"TX\"]:\n"
        outputString += "        HP_region4.val = HP_region4.r3.index\n"
        outputString += "    elif stateAbbreviation in [\"AZ\", \"CO\", \"ID\", \"MT\", \"NV\", \"NM\", \"UT\", \"WY\", \"AK\", \"CA\", \"HI\", \"OR\", \"WA\"]:\n"
        outputString += "        HP_region4.val = HP_region4.r4.index\n"
        outputString += "    else:\n"
        outputString += "        HP_region4.val = HP_region4.r5.index\n"
        outputString += "        \n"
        outputString += "    # Map state to region9        \n"
        outputString += "    if stateAbbreviation in [\"WA\", \"OR\", \"CA\", \"AK\", \"HI\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r1.index\n"
        outputString += "    elif stateAbbreviation in [\"MT\", \"ID\", \"WY\", \"CO\", \"UT\", \"NV\", \"AZ\", \"NM\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r2.index\n"
        outputString += "    elif stateAbbreviation in [\"ND\", \"MN\", \"SD\", \"NE\", \"IA\", \"KS\", \"MO\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r3.index\n"
        outputString += "    elif stateAbbreviation in [\"OK\", \"AR\", \"TX\", \"LA\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r4.index\n"
        outputString += "    elif stateAbbreviation in [\"MI\", \"WI\", \"IN\", \"IL\", \"OH\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r5.index\n"
        outputString += "    elif stateAbbreviation in [\"KY\", \"TN\", \"MS\", \"AL\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r6.index\n"
        outputString += "    elif stateAbbreviation in [\"ME\", \"NH\", \"VT\", \"MA\", \"CT\", \"RI\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r7.index\n"
        outputString += "    elif stateAbbreviation in [\"NY\", \"PA\", \"NJ\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r8.index\n"
        outputString += "    elif stateAbbreviation in [\"WV\", \"MD\", \"DE\", \"DC\", \"VA\", \"NC\", \"SC\", \"GA\", \"FL\"]:\n"
        outputString += "        HP_region9.val = HP_region9.r9.index\n"
        outputString += "    else:\n"
        outputString += "        HP_region9.val = HP_region9.r10.index\n"
        outputString += "        \n"
        outputString += "    # Punch state/territory\n"
        outputString += "    for eachRow in HP_state.rows:\n"
        outputString += "        if eachRow.label == \"r\" + stateAbbreviation:\n"
        outputString += "            HP_state.val = eachRow.index\n"
        outputString += "            break\n"
        outputString += "            \n"
        outputString += "    # Punch DMA\n"
        outputString += "    for eachRow in HP_DMA.rows:\n"
        outputString += "        if eachRow.label == \"r\" + DMAcode:\n"
        outputString += "            HP_DMA.val = eachRow.index\n"
        outputString += "            break\n"
        outputString += "\n"
        outputString += "else:\n"
        outputString += "    HP_region4.val = HP_region4.r99.index\n"
        outputString += "    HP_region9.val = HP_region9.r99.index\n"
        outputString += "    HP_state.val = HP_state.rXX.index\n"
        outputString += "    HP_DMA.val = HP_DMA.r999.index\n"
        outputString += "</exec>\n"
        outputString += "\n"
        outputString += "<suspend/>\n"
        outputString += "\n"
        outputString += "<radio label=\"HP_region4\" optional=\"1\" translateable=\"0\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Region 4 mapping from the zipcode entered in Q#.</title>\n"
        outputString += "<row label=\"r1\" value=\"1\">Northeast</row>\n"
        outputString += "<row label=\"r2\" value=\"2\">Midwest</row>\n"
        outputString += "<row label=\"r3\" value=\"3\">South</row>\n"
        outputString += "<row label=\"r4\" value=\"4\">West</row>\n"
        outputString += "<row label=\"r5\" value=\"5\">US territory</row>\n"
        outputString += "<row label=\"r99\" value=\"99\">INVALID ZIPCODE OR API FAILURE</row>\n"
        outputString += "</radio>\n"
        outputString += "\n"
        outputString += "<radio label=\"HP_region9\" optional=\"1\" translateable=\"0\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Region 9 mapping from the zipcode entered in Q#.</title>\n"
        outputString += "<row label=\"r1\" value=\"1\">Pacific</row>\n"
        outputString += "<row label=\"r2\" value=\"2\">Mountain</row>\n"
        outputString += "<row label=\"r3\" value=\"3\">WNC</row>\n"
        outputString += "<row label=\"r4\" value=\"4\">WSC</row>\n"
        outputString += "<row label=\"r5\" value=\"5\">ENC</row>\n"
        outputString += "<row label=\"r6\" value=\"6\">ESC</row>\n"
        outputString += "<row label=\"r7\" value=\"7\">NE</row>\n"
        outputString += "<row label=\"r8\" value=\"8\">MA</row>\n"
        outputString += "<row label=\"r9\" value=\"9\">SA</row>\n"
        outputString += "<row label=\"r10\" value=\"10\">US territory</row>\n"
        outputString += "<row label=\"r99\" value=\"99\">INVALID ZIPCODE OR API FAILURE</row>\n"
        outputString += "</radio>\n"
        outputString += "\n"
        outputString += "<radio label=\"HP_state\" multicol:count=\"4\" optional=\"1\" translateable=\"0\" uses=\"multicol.7\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  US state/territory mapping from the zipcode entered in Q#.</title>\n"
        outputString += "<row label=\"rAL\" value=\"1\">Alabama</row>\n"
        outputString += "<row label=\"rAK\" value=\"2\">Alaska</row>\n"
        outputString += "<row label=\"rAZ\" value=\"3\">Arizona</row>\n"
        outputString += "<row label=\"rAR\" value=\"4\">Arkansas</row>\n"
        outputString += "<row label=\"rCA\" value=\"5\">California</row>\n"
        outputString += "<row label=\"rCO\" value=\"6\">Colorado</row>\n"
        outputString += "<row label=\"rCT\" value=\"7\">Connecticut</row>\n"
        outputString += "<row label=\"rDE\" value=\"8\">Delaware</row>\n"
        outputString += "<row label=\"rFL\" value=\"9\">Florida</row>\n"
        outputString += "<row label=\"rGA\" value=\"10\">Georgia</row>\n"
        outputString += "<row label=\"rHI\" value=\"11\">Hawaii</row>\n"
        outputString += "<row label=\"rID\" value=\"12\">Idaho</row>\n"
        outputString += "<row label=\"rIL\" value=\"13\">Illinois</row>\n"
        outputString += "<row label=\"rIN\" value=\"14\">Indiana</row>\n"
        outputString += "<row label=\"rIA\" value=\"15\">Iowa</row>\n"
        outputString += "<row label=\"rKS\" value=\"16\">Kansas</row>\n"
        outputString += "<row label=\"rKY\" value=\"17\">Kentucky</row>\n"
        outputString += "<row label=\"rLA\" value=\"18\">Louisiana</row>\n"
        outputString += "<row label=\"rME\" value=\"19\">Maine</row>\n"
        outputString += "<row label=\"rMD\" value=\"20\">Maryland</row>\n"
        outputString += "<row label=\"rMA\" value=\"21\">Massachusetts</row>\n"
        outputString += "<row label=\"rMI\" value=\"22\">Michigan</row>\n"
        outputString += "<row label=\"rMN\" value=\"23\">Minnesota</row>\n"
        outputString += "<row label=\"rMS\" value=\"24\">Mississippi</row>\n"
        outputString += "<row label=\"rMO\" value=\"25\">Missouri</row>\n"
        outputString += "<row label=\"rMT\" value=\"26\">Montana</row>\n"
        outputString += "<row label=\"rNE\" value=\"27\">Nebraska</row>\n"
        outputString += "<row label=\"rNV\" value=\"28\">Nevada</row>\n"
        outputString += "<row label=\"rNH\" value=\"29\">New Hampshire</row>\n"
        outputString += "<row label=\"rNJ\" value=\"30\">New Jersey</row>\n"
        outputString += "<row label=\"rNM\" value=\"31\">New Mexico</row>\n"
        outputString += "<row label=\"rNY\" value=\"32\">New York</row>\n"
        outputString += "<row label=\"rNC\" value=\"33\">North Carolina</row>\n"
        outputString += "<row label=\"rND\" value=\"34\">North Dakota</row>\n"
        outputString += "<row label=\"rOH\" value=\"35\">Ohio</row>\n"
        outputString += "<row label=\"rOK\" value=\"36\">Oklahoma</row>\n"
        outputString += "<row label=\"rOR\" value=\"37\">Oregon</row>\n"
        outputString += "<row label=\"rPA\" value=\"38\">Pennsylvania</row>\n"
        outputString += "<row label=\"rRI\" value=\"39\">Rhode Island</row>\n"
        outputString += "<row label=\"rSC\" value=\"40\">South Carolina</row>\n"
        outputString += "<row label=\"rSD\" value=\"41\">South Dakota</row>\n"
        outputString += "<row label=\"rTN\" value=\"42\">Tennessee</row>\n"
        outputString += "<row label=\"rTX\" value=\"43\">Texas</row>\n"
        outputString += "<row label=\"rUT\" value=\"44\">Utah</row>\n"
        outputString += "<row label=\"rVT\" value=\"45\">Vermont</row>\n"
        outputString += "<row label=\"rVA\" value=\"46\">Virginia</row>\n"
        outputString += "<row label=\"rWA\" value=\"47\">Washington</row>\n"
        outputString += "<row label=\"rWV\" value=\"48\">West Virginia</row>\n"
        outputString += "<row label=\"rWI\" value=\"49\">Wisconsin</row>\n"
        outputString += "<row label=\"rWY\" value=\"50\">Wyoming</row>\n"
        outputString += "<row label=\"rAS\" value=\"51\">American Samoa</row>\n"
        outputString += "<row label=\"rDC\" value=\"52\">District of Columbia</row>\n"
        outputString += "<row label=\"rFM\" value=\"53\">Federated States of Micronesia</row>\n"
        outputString += "<row label=\"rGU\" value=\"54\">Guam</row>\n"
        outputString += "<row label=\"rMH\" value=\"55\">Marshall Islands</row>\n"
        outputString += "<row label=\"rMP\" value=\"56\">Northern Mariana Islands</row>\n"
        outputString += "<row label=\"rPW\" value=\"57\">Palau</row>\n"
        outputString += "<row label=\"rPR\" value=\"58\">Puerto Rico</row>\n"
        outputString += "<row label=\"rVI\" value=\"59\">Virgin Islands</row>\n"
        outputString += "<row label=\"rXX\" value=\"99\">INVALID ZIPCODE OR API FAILURE</row>\n"
        outputString += "</radio>\n"
        outputString += "\n"
        outputString += "<radio label=\"HP_DMA\" multicol:count=\"4\" optional=\"1\" uses=\"multicol.7\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  DMA mapping from the zipcode entered in Q#.</title>\n"
        outputString += "<row label=\"r662\" value=\"662\">662 Abilene-Sweetwater, TX</row>\n"
        outputString += "<row label=\"r525\" value=\"525\">525 Albany, GA</row>\n"
        outputString += "<row label=\"r532\" value=\"532\">532 Albany-Schenectady-Troy, NY</row>\n"
        outputString += "<row label=\"r790\" value=\"790\">790 Albuquerque-Santa Fe, NM</row>\n"
        outputString += "<row label=\"r644\" value=\"644\">644 Alexandria, LA</row>\n"
        outputString += "<row label=\"r583\" value=\"583\">583 Alpena, MI</row>\n"
        outputString += "<row label=\"r634\" value=\"634\">634 Amarillo, TX</row>\n"
        outputString += "<row label=\"r743\" value=\"743\">743 Anchorage, AK</row>\n"
        outputString += "<row label=\"r524\" value=\"524\">524 Atlanta, GA</row>\n"
        outputString += "<row label=\"r520\" value=\"520\">520 Augusta, GA</row>\n"
        outputString += "<row label=\"r635\" value=\"635\">635 Austin, TX</row>\n"
        outputString += "<row label=\"r800\" value=\"800\">800 Bakersfield, CA</row>\n"
        outputString += "<row label=\"r512\" value=\"512\">512 Baltimore, MD</row>\n"
        outputString += "<row label=\"r537\" value=\"537\">537 Bangor, ME</row>\n"
        outputString += "<row label=\"r716\" value=\"716\">716 Baton Rouge, LA</row>\n"
        outputString += "<row label=\"r692\" value=\"692\">692 Beaumont-Port Arthur, TX</row>\n"
        outputString += "<row label=\"r821\" value=\"821\">821 Bend, OR</row>\n"
        outputString += "<row label=\"r756\" value=\"756\">756 Billings, MT</row>\n"
        outputString += "<row label=\"r746\" value=\"746\">746 Biloxi-Gulfport, MS</row>\n"
        outputString += "<row label=\"r502\" value=\"502\">502 Binghamton, NY</row>\n"
        outputString += "<row label=\"r630\" value=\"630\">630 Birmingham (Anniston and Tuscaloosa), AL</row>\n"
        outputString += "<row label=\"r559\" value=\"559\">559 Bluefield-Beckley-Oak Hill, WV</row>\n"
        outputString += "<row label=\"r757\" value=\"757\">757 Boise, ID</row>\n"
        outputString += "<row label=\"r506\" value=\"506\">506 Boston, MA (Manchester, NH)</row>\n"
        outputString += "<row label=\"r736\" value=\"736\">736 Bowling Green, KY</row>\n"
        outputString += "<row label=\"r514\" value=\"514\">514 Buffalo, NY</row>\n"
        outputString += "<row label=\"r523\" value=\"523\">523 Burlington, VT-Plattsburgh, NY</row>\n"
        outputString += "<row label=\"r754\" value=\"754\">754 Butte-Bozeman, MT</row>\n"
        outputString += "<row label=\"r767\" value=\"767\">767 Casper-Riverton, WY</row>\n"
        outputString += "<row label=\"r637\" value=\"637\">637 Cedar Rapids-Waterloo-Iowa City and Dubuque, IA</row>\n"
        outputString += "<row label=\"r648\" value=\"648\">648 Champaign and Springfield-Decatur, IL</row>\n"
        outputString += "<row label=\"r519\" value=\"519\">519 Charleston, SC</row>\n"
        outputString += "<row label=\"r564\" value=\"564\">564 Charleston-Huntington, WV</row>\n"
        outputString += "<row label=\"r517\" value=\"517\">517 Charlotte, NC</row>\n"
        outputString += "<row label=\"r584\" value=\"584\">584 Charlottesville, VA</row>\n"
        outputString += "<row label=\"r575\" value=\"575\">575 Chattanooga, TN</row>\n"
        outputString += "<row label=\"r759\" value=\"759\">759 Cheyenne, WY-Scottsbluff, NE</row>\n"
        outputString += "<row label=\"r602\" value=\"602\">602 Chicago, IL</row>\n"
        outputString += "<row label=\"r868\" value=\"868\">868 Chico-Redding, CA</row>\n"
        outputString += "<row label=\"r515\" value=\"515\">515 Cincinnati, OH</row>\n"
        outputString += "<row label=\"r598\" value=\"598\">598 Clarksburg-Weston, WV</row>\n"
        outputString += "<row label=\"r510\" value=\"510\">510 Cleveland-Akron (Canton), OH</row>\n"
        outputString += "<row label=\"r752\" value=\"752\">752 Colorado Springs-Pueblo, CO</row>\n"
        outputString += "<row label=\"r546\" value=\"546\">546 Columbia, SC</row>\n"
        outputString += "<row label=\"r604\" value=\"604\">604 Columbia-Jefferson City, MO</row>\n"
        outputString += "<row label=\"r522\" value=\"522\">522 Columbus, GA</row>\n"
        outputString += "<row label=\"r535\" value=\"535\">535 Columbus, OH</row>\n"
        outputString += "<row label=\"r673\" value=\"673\">673 Columbus-Tupelo-West Point, MS</row>\n"
        outputString += "<row label=\"r600\" value=\"600\">600 Corpus Christi, TX</row>\n"
        outputString += "<row label=\"r623\" value=\"623\">623 Dallas-Ft. Worth, TX</row>\n"
        outputString += "<row label=\"r682\" value=\"682\">682 Davenport, IA-Rock Island-Moline, IL</row>\n"
        outputString += "<row label=\"r542\" value=\"542\">542 Dayton, OH</row>\n"
        outputString += "<row label=\"r751\" value=\"751\">751 Denver, CO</row>\n"
        outputString += "<row label=\"r679\" value=\"679\">679 Des Moines-Ames, IA</row>\n"
        outputString += "<row label=\"r505\" value=\"505\">505 Detroit, MI</row>\n"
        outputString += "<row label=\"r606\" value=\"606\">606 Dothan, AL</row>\n"
        outputString += "<row label=\"r676\" value=\"676\">676 Duluth, MN-Superior, WI</row>\n"
        outputString += "<row label=\"r765\" value=\"765\">765 El Paso, TX</row>\n"
        outputString += "<row label=\"r565\" value=\"565\">565 Elmira, NY</row>\n"
        outputString += "<row label=\"r516\" value=\"516\">516 Erie, PA</row>\n"
        outputString += "<row label=\"r801\" value=\"801\">801 Eugene, OR</row>\n"
        outputString += "<row label=\"r802\" value=\"802\">802 Eureka, CA</row>\n"
        outputString += "<row label=\"r649\" value=\"649\">649 Evansville, IN</row>\n"
        outputString += "<row label=\"r745\" value=\"745\">745 Fairbanks, AK</row>\n"
        outputString += "<row label=\"r724\" value=\"724\">724 Fargo-Valley City, ND</row>\n"
        outputString += "<row label=\"r513\" value=\"513\">513 Flint-Saginaw-Bay City, MI</row>\n"
        outputString += "<row label=\"r866\" value=\"866\">866 Fresno-Visalia, CA</row>\n"
        outputString += "<row label=\"r571\" value=\"571\">571 Ft. Myers-Naples, Fl</row>\n"
        outputString += "<row label=\"r670\" value=\"670\">670 Ft. Smith-Fayetteville-Springdale-Rogers, AR</row>\n"
        outputString += "<row label=\"r509\" value=\"509\">509 Ft. Wayne, IN</row>\n"
        outputString += "<row label=\"r592\" value=\"592\">592 Gainesville, FL</row>\n"
        outputString += "<row label=\"r798\" value=\"798\">798 Glendive, MT</row>\n"
        outputString += "<row label=\"r773\" value=\"773\">773 Grand Junction-Montrose, CO</row>\n"
        outputString += "<row label=\"r563\" value=\"563\">563 Grand Rapids-Kalamazoo-Battle Creek, MI</row>\n"
        outputString += "<row label=\"r755\" value=\"755\">755 Great Falls, MT</row>\n"
        outputString += "<row label=\"r658\" value=\"658\">658 Green Bay-Appleton, WI</row>\n"
        outputString += "<row label=\"r518\" value=\"518\">518 Greensboro-High Point-Winston Salem, NC</row>\n"
        outputString += "<row label=\"r545\" value=\"545\">545 Greenville-New Bern-Washington, NC</row>\n"
        outputString += "<row label=\"r567\" value=\"567\">567 Greenville-Spartanburg, SC-Asheville, NC-Anderson,SC</row>\n"
        outputString += "<row label=\"r647\" value=\"647\">647 Greenwood-Greenville, MS</row>\n"
        outputString += "<row label=\"r636\" value=\"636\">636 Harlingen-Weslaco-Brownsville-McAllen, TX</row>\n"
        outputString += "<row label=\"r566\" value=\"566\">566 Harrisburg-Lancaster-Lebanon-York, PA</row>\n"
        outputString += "<row label=\"r569\" value=\"569\">569 Harrisonburg, VA</row>\n"
        outputString += "<row label=\"r533\" value=\"533\">533 Hartford and New Haven, CT</row>\n"
        outputString += "<row label=\"r710\" value=\"710\">710 Hattiesburg-Laurel, MS</row>\n"
        outputString += "<row label=\"r766\" value=\"766\">766 Helena, MT</row>\n"
        outputString += "<row label=\"r744\" value=\"744\">744 Honolulu, HI</row>\n"
        outputString += "<row label=\"r618\" value=\"618\">618 Houston, TX</row>\n"
        outputString += "<row label=\"r691\" value=\"691\">691 Huntsville-Decatur (Florence), AL</row>\n"
        outputString += "<row label=\"r758\" value=\"758\">758 Idaho Falls-Pocatello, ID</row>\n"
        outputString += "<row label=\"r527\" value=\"527\">527 Indianapolis, IN</row>\n"
        outputString += "<row label=\"r718\" value=\"718\">718 Jackson, MS</row>\n"
        outputString += "<row label=\"r639\" value=\"639\">639 Jackson, TN</row>\n"
        outputString += "<row label=\"r561\" value=\"561\">561 Jacksonville, FL</row>\n"
        outputString += "<row label=\"r574\" value=\"574\">574 Johnstown-Altoona, PA</row>\n"
        outputString += "<row label=\"r734\" value=\"734\">734 Jonesboro, AR</row>\n"
        outputString += "<row label=\"r603\" value=\"603\">603 Joplin, MO-Pittsburg, KS</row>\n"
        outputString += "<row label=\"r747\" value=\"747\">747 Juneau, AK</row>\n"
        outputString += "<row label=\"r616\" value=\"616\">616 Kansas City, MO</row>\n"
        outputString += "<row label=\"r557\" value=\"557\">557 Knoxville, TN</row>\n"
        outputString += "<row label=\"r702\" value=\"702\">702 La Crosse-Eau Claire, WI</row>\n"
        outputString += "<row label=\"r582\" value=\"582\">582 Lafayette, IN</row>\n"
        outputString += "<row label=\"r642\" value=\"642\">642 Lafayette, LA</row>\n"
        outputString += "<row label=\"r643\" value=\"643\">643 Lake Charles, LA</row>\n"
        outputString += "<row label=\"r551\" value=\"551\">551 Lansing, MI</row>\n"
        outputString += "<row label=\"r749\" value=\"749\">749 Laredo, TX</row>\n"
        outputString += "<row label=\"r839\" value=\"839\">839 Las Vegas, NV</row>\n"
        outputString += "<row label=\"r541\" value=\"541\">541 Lexington, KY</row>\n"
        outputString += "<row label=\"r558\" value=\"558\">558 Lima, OH</row>\n"
        outputString += "<row label=\"r722\" value=\"722\">722 Lincoln and Hastings-Kearney, NE</row>\n"
        outputString += "<row label=\"r693\" value=\"693\">693 Little Rock-Pine Bluff, AR</row>\n"
        outputString += "<row label=\"r803\" value=\"803\">803 Los Angeles, CA</row>\n"
        outputString += "<row label=\"r529\" value=\"529\">529 Louisville, KY</row>\n"
        outputString += "<row label=\"r651\" value=\"651\">651 Lubbock, TX</row>\n"
        outputString += "<row label=\"r503\" value=\"503\">503 Macon, GA</row>\n"
        outputString += "<row label=\"r669\" value=\"669\">669 Madison, WI</row>\n"
        outputString += "<row label=\"r737\" value=\"737\">737 Mankato, MN</row>\n"
        outputString += "<row label=\"r553\" value=\"553\">553 Marquette, MI</row>\n"
        outputString += "<row label=\"r813\" value=\"813\">813 Medford-Klamath Falls, OR</row>\n"
        outputString += "<row label=\"r640\" value=\"640\">640 Memphis, TN</row>\n"
        outputString += "<row label=\"r711\" value=\"711\">711 Meridian, MS</row>\n"
        outputString += "<row label=\"r528\" value=\"528\">528 Miami-Fort Lauderdale, FL</row>\n"
        outputString += "<row label=\"r617\" value=\"617\">617 Milwaukee, WI</row>\n"
        outputString += "<row label=\"r613\" value=\"613\">613 Minneapolis-St. Paul, MN</row>\n"
        outputString += "<row label=\"r687\" value=\"687\">687 Minot-Bismarck-Dickinson(Williston), ND</row>\n"
        outputString += "<row label=\"r762\" value=\"762\">762 Missoula, MT</row>\n"
        outputString += "<row label=\"r686\" value=\"686\">686 Mobile, AL-Pensacola (Ft. Walton Beach), FL</row>\n"
        outputString += "<row label=\"r628\" value=\"628\">628 Monroe, LA-El Dorado, AR</row>\n"
        outputString += "<row label=\"r828\" value=\"828\">828 Monterey-Salinas, CA</row>\n"
        outputString += "<row label=\"r698\" value=\"698\">698 Montgomery-Selma, AL</row>\n"
        outputString += "<row label=\"r570\" value=\"570\">570 Myrtle Beach-Florence, SC</row>\n"
        outputString += "<row label=\"r659\" value=\"659\">659 Nashville, TN</row>\n"
        outputString += "<row label=\"r622\" value=\"622\">622 New Orleans, LA</row>\n"
        outputString += "<row label=\"r501\" value=\"501\">501 New York, NY</row>\n"
        outputString += "<row label=\"r544\" value=\"544\">544 Norfolk-Portsmouth-Newport News, VA</row>\n"
        outputString += "<row label=\"r740\" value=\"740\">740 North Platte, NE</row>\n"
        outputString += "<row label=\"r633\" value=\"633\">633 Odessa-Midland, TX</row>\n"
        outputString += "<row label=\"r650\" value=\"650\">650 Oklahoma City, OK</row>\n"
        outputString += "<row label=\"r652\" value=\"652\">652 Omaha, NE</row>\n"
        outputString += "<row label=\"r534\" value=\"534\">534 Orlando-Daytona Beach-Melbourne, FL</row>\n"
        outputString += "<row label=\"r631\" value=\"631\">631 Ottumwa, IA-Kirksville, MO</row>\n"
        outputString += "<row label=\"r632\" value=\"632\">632 Paducah, KY-Cape Girardeau, MO-Harrisburg, IL</row>\n"
        outputString += "<row label=\"r804\" value=\"804\">804 Palm Springs, CA</row>\n"
        outputString += "<row label=\"r656\" value=\"656\">656 Panama City, FL</row>\n"
        outputString += "<row label=\"r597\" value=\"597\">597 Parkersburg, WV</row>\n"
        outputString += "<row label=\"r675\" value=\"675\">675 Peoria-Bloomington, IL</row>\n"
        outputString += "<row label=\"r504\" value=\"504\">504 Philadelphia, PA</row>\n"
        outputString += "<row label=\"r753\" value=\"753\">753 Phoenix, AZ</row>\n"
        outputString += "<row label=\"r508\" value=\"508\">508 Pittsburgh, PA</row>\n"
        outputString += "<row label=\"r820\" value=\"820\">820 Portland, OR</row>\n"
        outputString += "<row label=\"r500\" value=\"500\">500 Portland-Auburn, ME</row>\n"
        outputString += "<row label=\"r552\" value=\"552\">552 Presque Isle, ME</row>\n"
        outputString += "<row label=\"r521\" value=\"521\">521 Providence, RI-New Bedford, MA</row>\n"
        outputString += "<row label=\"r717\" value=\"717\">717 Quincy, IL-Hannibal, MO-Keokuk, IA</row>\n"
        outputString += "<row label=\"r560\" value=\"560\">560 Raleigh-Durham (Fayetteville), NC</row>\n"
        outputString += "<row label=\"r764\" value=\"764\">764 Rapid City, SD</row>\n"
        outputString += "<row label=\"r811\" value=\"811\">811 Reno, NV</row>\n"
        outputString += "<row label=\"r556\" value=\"556\">556 Richmond-Petersburg, VA</row>\n"
        outputString += "<row label=\"r573\" value=\"573\">573 Roanoke-Lynchburg, VA</row>\n"
        outputString += "<row label=\"r538\" value=\"538\">538 Rochester, NY</row>\n"
        outputString += "<row label=\"r611\" value=\"611\">611 Rochester, MN-Mason City, IA-Austin, MN</row>\n"
        outputString += "<row label=\"r610\" value=\"610\">610 Rockford, IL</row>\n"
        outputString += "<row label=\"r862\" value=\"862\">862 Sacramento-Stockton-Modesto, CA</row>\n"
        outputString += "<row label=\"r576\" value=\"576\">576 Salisbury, MD</row>\n"
        outputString += "<row label=\"r770\" value=\"770\">770 Salt Lake City, UT</row>\n"
        outputString += "<row label=\"r661\" value=\"661\">661 San Angelo, TX</row>\n"
        outputString += "<row label=\"r641\" value=\"641\">641 San Antonio, TX</row>\n"
        outputString += "<row label=\"r825\" value=\"825\">825 San Diego, CA</row>\n"
        outputString += "<row label=\"r807\" value=\"807\">807 San Francisco-Oakland-San Jose, CA</row>\n"
        outputString += "<row label=\"r855\" value=\"855\">855 Santa Barbara-Santa Maria-San Luis Obispo, CA</row>\n"
        outputString += "<row label=\"r507\" value=\"507\">507 Savannah, GA</row>\n"
        outputString += "<row label=\"r819\" value=\"819\">819 Seattle-Tacoma, WA</row>\n"
        outputString += "<row label=\"r657\" value=\"657\">657 Sherman, TX-Ada, OK</row>\n"
        outputString += "<row label=\"r612\" value=\"612\">612 Shreveport, LA</row>\n"
        outputString += "<row label=\"r624\" value=\"624\">624 Sioux City, IA</row>\n"
        outputString += "<row label=\"r725\" value=\"725\">725 Sioux Falls (Mitchell), SD</row>\n"
        outputString += "<row label=\"r588\" value=\"588\">588 South Bend-Elkhart, IN</row>\n"
        outputString += "<row label=\"r881\" value=\"881\">881 Spokane, WA</row>\n"
        outputString += "<row label=\"r619\" value=\"619\">619 Springfield, MO</row>\n"
        outputString += "<row label=\"r543\" value=\"543\">543 Springfield-Holyoke, MA</row>\n"
        outputString += "<row label=\"r638\" value=\"638\">638 St. Joseph, MO</row>\n"
        outputString += "<row label=\"r609\" value=\"609\">609 St. Louis, MO</row>\n"
        outputString += "<row label=\"r555\" value=\"555\">555 Syracuse, NY</row>\n"
        outputString += "<row label=\"r530\" value=\"530\">530 Tallahassee, FL-Thomasville, GA</row>\n"
        outputString += "<row label=\"r539\" value=\"539\">539 Tampa-St. Petersburg (Sarasota), FL</row>\n"
        outputString += "<row label=\"r581\" value=\"581\">581 Terre Haute, IN</row>\n"
        outputString += "<row label=\"r547\" value=\"547\">547 Toledo, OH</row>\n"
        outputString += "<row label=\"r605\" value=\"605\">605 Topeka, KS</row>\n"
        outputString += "<row label=\"r540\" value=\"540\">540 Traverse City-Cadillac, MI</row>\n"
        outputString += "<row label=\"r531\" value=\"531\">531 Tri-Cities, TN-VA</row>\n"
        outputString += "<row label=\"r789\" value=\"789\">789 Tucson (Sierra Vista), AZ</row>\n"
        outputString += "<row label=\"r671\" value=\"671\">671 Tulsa, OK</row>\n"
        outputString += "<row label=\"r760\" value=\"760\">760 Twin Falls, ID</row>\n"
        outputString += "<row label=\"r709\" value=\"709\">709 Tyler-Longview(Lufkin and Nacogdoches), TX</row>\n"
        outputString += "<row label=\"r526\" value=\"526\">526 Utica, NY</row>\n"
        outputString += "<row label=\"r626\" value=\"626\">626 Victoria, TX</row>\n"
        outputString += "<row label=\"r625\" value=\"625\">625 Waco-Temple-Bryan, TX</row>\n"
        outputString += "<row label=\"r511\" value=\"511\">511 Washington, DC (Hagerstown, MD)</row>\n"
        outputString += "<row label=\"r549\" value=\"549\">549 Watertown, NY</row>\n"
        outputString += "<row label=\"r705\" value=\"705\">705 Wausau-Rhinelander, WI</row>\n"
        outputString += "<row label=\"r548\" value=\"548\">548 West Palm Beach-Ft. Pierce, FL</row>\n"
        outputString += "<row label=\"r554\" value=\"554\">554 Wheeling, WV-Steubenville, OH</row>\n"
        outputString += "<row label=\"r627\" value=\"627\">627 Wichita Falls, TX-Lawton, OK</row>\n"
        outputString += "<row label=\"r678\" value=\"678\">678 Wichita-Hutchinson, KS Plus</row>\n"
        outputString += "<row label=\"r577\" value=\"577\">577 Wilkes Barre-Scranton, PA</row>\n"
        outputString += "<row label=\"r550\" value=\"550\">550 Wilmington, NC</row>\n"
        outputString += "<row label=\"r810\" value=\"810\">810 Yakima-Pasco-Richland-Kennewick, WA</row>\n"
        outputString += "<row label=\"r536\" value=\"536\">536 Youngstown, OH</row>\n"
        outputString += "<row label=\"r771\" value=\"771\">771 Yuma, AZ-El Centro, CA</row>\n"
        outputString += "<row label=\"r596\" value=\"596\">596 Zanesville, OH</row>\n"
        outputString += "<row label=\"r999\" value=\"999\">INVALID ZIPCODE OR API FAILURE</row>\n"
        outputString += "</radio>\n"
        outputString += "\n"
        outputString += "<suspend/>\n"
        outputString += "\n"
        outputString += "</block>"
    
    # Text question: Phone number
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[27]:
        outputString += "<text label=\"Q#\" optional=\"0\" size=\"10\" verify=\"phoneUS\" pii=\"4\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter the number without dashes; e.g. 5551234567</comment>\n"
        outputString += "</text>"
    
    # Radio question: Education level
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[28]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"r1\">Associate's Degree</row>\n"
        outputString += "<row label=\"r2\">Bachelor's Degree</row>\n"
        outputString += "<row label=\"r3\">Doctoral or Professional Degree (PhD, Ed.D, JD, DVM, DO, MD, DDS, or similar)</row>\n"
        outputString += "<row label=\"r4\">Incomplete Secondary (high school) Education</row>\n"
        outputString += "<row label=\"r5\">Master's Degree</row>\n"
        outputString += "<row label=\"r6\">Secondary (high school) Education</row>\n"
        outputString += "<row label=\"r7\">Some College, University, Technical School or Further Education</row>\n"
        outputString += "<row label=\"r8\">Vocational or Technical Degree</row>\n"
        outputString += "<row label=\"r9\">Prefer not to answer</row>\n"
        outputString += "</radio>"
        
    # Text Question: CA postal code (3 chars.)
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[29]:
        outputString += "<res label=\"Q#errorBadLength\">Please enter only three characters.</res>\n"
        outputString += "<res label=\"Q#errorWrongChars\">Please enter a valid postal code.</res>\n"
        outputString += "\n"
        outputString += "<text label=\"Q#\" optional=\"0\" size=\"3\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter the first 3 characters.</comment>\n"
        outputString += "<validate>\n"
        outputString += "if len(Q#.val) != 3:\n"
        outputString += "    error(res.Q#errorBadLength)\n"
        outputString += "elif not(Q#.val[0].isalpha() and Q#.val[1].isdigit() and Q#.val[2].isalpha()):\n"
        outputString += "    error(res.Q#errorWrongChars)\n"
        outputString += "elif Q#.val[0].lower() in ['d', 'f', 'i', 'o', 'q', 'u', 'w', 'z']:\n"
        outputString += "    error(res.Q#errorWrongChars)\n"
        outputString += "</validate>\n"
        outputString += "</text>"
    
    # Text Question: CA postal code with province punch
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[30]:
        outputString += "<res label=\"Q#errorBadLength\">Please enter only three characters.</res>\n"
        outputString += "<res label=\"Q#errorWrongChars\">Please enter a valid postal code.</res>\n"
        outputString += "\n"
        outputString += "<text label=\"Q#\" optional=\"0\" size=\"3\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter the first 3 characters.</comment>\n"
        outputString += "<validate>\n"
        outputString += "if len(Q#.val) != 3:\n"
        outputString += "    error(res.Q#errorBadLength)\n"
        outputString += "elif not(Q#.val[0].isalpha() and Q#.val[1].isdigit() and Q#.val[2].isalpha()):\n"
        outputString += "    error(res.Q#errorWrongChars)\n"
        outputString += "elif Q#.val[0].lower() in ['d', 'f', 'i', 'o', 'q', 'u', 'w', 'z']:\n"
        outputString += "    error(res.Q#errorWrongChars)\n"
        outputString += "</validate>\n"
        outputString += "</text>\n"
        outputString += "\n"
        outputString += "<suspend/>\n"
        outputString += "\n"
        outputString += "<exec>\n"
        outputString += "firstChar = Q#.val[0].lower()\n"
        outputString += "\n"
        outputString += "if firstChar == \"a\":\n"
        outputString += "    HP_province.val = HP_province.rNL.index\n"
        outputString += "elif firstChar == \"b\":\n"
        outputString += "    HP_province.val = HP_province.rNS.index\n"
        outputString += "elif firstChar == \"c\":\n"
        outputString += "    HP_province.val = HP_province.rPE.index\n"
        outputString += "elif firstChar == \"e\":\n"
        outputString += "    HP_province.val = HP_province.rNB.index\n"
        outputString += "elif firstChar == \"g\" or firstChar == \"h\" or firstChar == \"j\":\n"
        outputString += "    HP_province.val = HP_province.rQC.index\n"
        outputString += "elif firstChar == \"k\" or firstChar == \"l\" or firstChar == \"m\" or firstChar == \"n\" or firstChar == \"p\":\n"
        outputString += "    HP_province.val = HP_province.rON.index\n"
        outputString += "elif firstChar == \"r\":\n"
        outputString += "    HP_province.val = HP_province.rMB.index\n"
        outputString += "elif firstChar == \"s\":\n"
        outputString += "    HP_province.val = HP_province.rSK.index\n"
        outputString += "elif firstChar == \"t\":\n"
        outputString += "    HP_province.val = HP_province.rAB.index\n"
        outputString += "elif firstChar == \"v\":\n"
        outputString += "    HP_province.val = HP_province.rBC.index\n"
        outputString += "elif firstChar == \"x\":\n"
        outputString += "    HP_province.val = HP_province.rNUNT.index\n"
        outputString += "elif firstChar == \"y\":\n"
        outputString += "    HP_province.val = HP_province.rYT.index\n"
        outputString += "</exec>\n"
        outputString += "\n"
        outputString += "<suspend/>\n"
        outputString += "\n"
        outputString += "<radio label=\"HP_province\" where=\"execute,survey,report\">\n"
        outputString += "<title>Hidden Question.  Province taken from postal code.</title>\n"
        outputString += "<row label=\"rAB\">Alberta</row>\n"
        outputString += "<row label=\"rBC\">British Columbia</row>\n"
        outputString += "<row label=\"rMB\">Manitoba</row>\n"
        outputString += "<row label=\"rNB\">New Brunswick</row>\n"
        outputString += "<row label=\"rNL\">Newfoundland and Labrador</row>\n"
        outputString += "<row label=\"rNS\">Nova Scotia</row>\n"
        outputString += "<row label=\"rNUNT\">Nunavut / Northwest Territories</row>\n"
        outputString += "<row label=\"rON\">Ontario</row>\n"
        outputString += "<row label=\"rPE\">Prince Edward Island</row>\n"
        outputString += "<row label=\"rQC\">Quebec</row>\n"
        outputString += "<row label=\"rSK\">Saskatchewan</row>\n"
        outputString += "<row label=\"rYT\">Yukon</row>\n"
        outputString += "</radio>"
    
    # Radio Question: CA province
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[31]:
        outputString += "<radio label=\"Q#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"rAB\">Alberta</row>\n"
        outputString += "<row label=\"rBC\">British Columbia</row>\n"
        outputString += "<row label=\"rMB\">Manitoba</row>\n"
        outputString += "<row label=\"rNB\">New Brunswick</row>\n"
        outputString += "<row label=\"rNL\">Newfoundland and Labrador</row>\n"
        outputString += "<row label=\"rNT\">Northwest Territories</row>\n"
        outputString += "<row label=\"rNS\">Nova Scotia</row>\n"
        outputString += "<row label=\"rNU\">Nunavut</row>\n"
        outputString += "<row label=\"rON\">Ontario</row>\n"
        outputString += "<row label=\"rPE\">Prince Edward Island</row>\n"
        outputString += "<row label=\"rQC\">Quebec</row>\n"
        outputString += "<row label=\"rSK\">Saskatchewan</row>\n"
        outputString += "<row label=\"rYT\">Yukon</row>\n"
        outputString += "</radio>"
    
    # Select Question: CA province
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[32]:
        outputString += "<select label=\"Q#\" optional=\"0\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<choice label=\"chAB\">Alberta</choice>\n"
        outputString += "<choice label=\"chBC\">British Columbia</choice>\n"
        outputString += "<choice label=\"chMB\">Manitoba</choice>\n"
        outputString += "<choice label=\"chNB\">New Brunswick</choice>\n"
        outputString += "<choice label=\"chNL\">Newfoundland and Labrador</choice>\n"
        outputString += "<choice label=\"chNT\">Northwest Territories</choice>\n"
        outputString += "<choice label=\"chNS\">Nova Scotia</choice>\n"
        outputString += "<choice label=\"chNU\">Nunavut</choice>\n"
        outputString += "<choice label=\"chON\">Ontario</choice>\n"
        outputString += "<choice label=\"chPE\">Prince Edward Island</choice>\n"
        outputString += "<choice label=\"chQC\">Quebec</choice>\n"
        outputString += "<choice label=\"chSK\">Saskatchewan</choice>\n"
        outputString += "<choice label=\"chYT\">Yukon</choice>\n"
        outputString += "</select>"
        
    # Radio Question: Level of agreement (4 points)
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[33]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c1\" value=\"1\">Strongly Disagree</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">Disagree</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">Agree</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">Strongly Agree</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
    
    # Radio Question: Level of agreement (5 points)
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[34]:
        outputString += "<radio label=\"Q#\" type=\"rating\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<col label=\"c1\" value=\"1\">Strongly Disagree</col>\n"
        outputString += "<col label=\"c2\" value=\"2\">Disagree</col>\n"
        outputString += "<col label=\"c3\" value=\"3\">Neither Agree nor Disagree</col>\n"
        outputString += "<col label=\"c4\" value=\"4\">Agree</col>\n"
        outputString += "<col label=\"c5\" value=\"5\">Strongly Agree</col>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
    
    # Radio Question: Multicolumn
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[35]:
        outputString += "<radio label=\"Q#\" uses=\"multicol.7\" multicol:count=\"2\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
    
    # Checkbox Question: Multicolumn
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[36]:
        outputString += "<checkbox label=\"Q#\" atleast=\"1\" uses=\"multicol.7\" multicol:count=\"2\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select all that apply.</comment>\n"
        outputString += "@elements\n"
        outputString += "</checkbox>"
    
    # Radio Question: Button select
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[37]:
        outputString += "<radio label=\"Q#\" uses=\"atm1d.8\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "@elements\n"
        outputString += "</radio>"
    
    # Checkbox Question: Button select
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[38]:
        outputString += "<checkbox label=\"Q#\" atleast=\"1\" uses=\"atm1d.8\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select all that apply.</comment>\n"
        outputString += "@elements\n"
        outputString += "</checkbox>"
    
    # Number Question: Autosum
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[39]:
        outputString += "<number label=\"Q#\" optional=\"0\" size=\"#\" uses=\"autosum.5\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "@elements\n"
        outputString += "</number>"
    
    # Number Question: Slider
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[40]:
        outputString += "<number label=\"Q#\" optional=\"0\" size=\"#\" uses=\"slidernumber.5\"  verify=\"range(0,100)\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please drag the slider to the correct value.</comment>\n"
        outputString += "@elements\n"
        outputString += "</number>"
    
    # Select Question: Ranksort
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[41]:
        outputString += "<select label=\"Q#\" optional=\"0\" uses=\"ranksort.4\" minRanks=\"#\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please rank your choices in order.</comment>\n"
        outputString += "@elements\n"
        outputString += "</select>"
        
    # Radio Question: UK region
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[42]:
        outputString += "<radio label=\"Q#\" uses=\"multicol.7\" multicol:count=\"3\" sortRows=\"asc\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please select one.</comment>\n"
        outputString += "<row label=\"rAB\">Aberdeen</row>\n"
        outputString += "<row label=\"rAL\">St Albans</row>\n"
        outputString += "<row label=\"rB\">Birmingham</row>\n"
        outputString += "<row label=\"rBA\">Bath</row>\n"
        outputString += "<row label=\"rBB\">Blackburn</row>\n"
        outputString += "<row label=\"rBD\">Bradford</row>\n"
        outputString += "<row label=\"rBH\">Bournemouth</row>\n"
        outputString += "<row label=\"rBL\">Bolton</row>\n"
        outputString += "<row label=\"rBN\">Brighton</row>\n"
        outputString += "<row label=\"rBR\">Bromley</row>\n"
        outputString += "<row label=\"rBS\">Bristol</row>\n"
        outputString += "<row label=\"rBT\">Belfast</row>\n"
        outputString += "<row label=\"rCA\">Carlisle</row>\n"
        outputString += "<row label=\"rCB\">Cambridge</row>\n"
        outputString += "<row label=\"rCF\">Cardiff</row>\n"
        outputString += "<row label=\"rCH\">Chester</row>\n"
        outputString += "<row label=\"rCM\">Chelmsford</row>\n"
        outputString += "<row label=\"rCO\">Colchester</row>\n"
        outputString += "<row label=\"rCR\">Croydon</row>\n"
        outputString += "<row label=\"rCT\">Canterbury</row>\n"
        outputString += "<row label=\"rCV\">Coventry</row>\n"
        outputString += "<row label=\"rCW\">Crewe</row>\n"
        outputString += "<row label=\"rDA\">Dartford</row>\n"
        outputString += "<row label=\"rDD\">Dundee</row>\n"
        outputString += "<row label=\"rDE\">Derby</row>\n"
        outputString += "<row label=\"rDG\">Dumfries</row>\n"
        outputString += "<row label=\"rDH\">Durham</row>\n"
        outputString += "<row label=\"rDL\">Darlington</row>\n"
        outputString += "<row label=\"rDN\">Doncaster</row>\n"
        outputString += "<row label=\"rDT\">Dorchester</row>\n"
        outputString += "<row label=\"rDY\">Dudley</row>\n"
        outputString += "<row label=\"rE\">East London</row>\n"
        outputString += "<row label=\"rEC\">East Central London</row>\n"
        outputString += "<row label=\"rEH\">Edinburgh</row>\n"
        outputString += "<row label=\"rEN\">Enfield</row>\n"
        outputString += "<row label=\"rEX\">Exeter</row>\n"
        outputString += "<row label=\"rFK\">Falkirk</row>\n"
        outputString += "<row label=\"rFY\">Blackpool</row>\n"
        outputString += "<row label=\"rG\">Glasgow</row>\n"
        outputString += "<row label=\"rGL\">Gloucester</row>\n"
        outputString += "<row label=\"rGU\">Guildford</row>\n"
        outputString += "<row label=\"rHA\">Harrow</row>\n"
        outputString += "<row label=\"rHD\">Huddersfield</row>\n"
        outputString += "<row label=\"rHG\">Harrogate</row>\n"
        outputString += "<row label=\"rHP\">Hemel Hempstead</row>\n"
        outputString += "<row label=\"rHR\">Hereford</row>\n"
        outputString += "<row label=\"rHS\">Outer Hebrides</row>\n"
        outputString += "<row label=\"rHU\">Hull</row>\n"
        outputString += "<row label=\"rHX\">Halifax</row>\n"
        outputString += "<row label=\"rIG\">Ilford</row>\n"
        outputString += "<row label=\"rIP\">Ipswich</row>\n"
        outputString += "<row label=\"rIV\">Inverness</row>\n"
        outputString += "<row label=\"rKA\">Kilmarnock</row>\n"
        outputString += "<row label=\"rKT\">Kingston upon Thames</row>\n"
        outputString += "<row label=\"rKW\">Kirkwall</row>\n"
        outputString += "<row label=\"rKY\">Kirkcaldy</row>\n"
        outputString += "<row label=\"rL\">Liverpool</row>\n"
        outputString += "<row label=\"rLA\">Lancaster</row>\n"
        outputString += "<row label=\"rLD\">Llandrindod Wells</row>\n"
        outputString += "<row label=\"rLE\">Leicester</row>\n"
        outputString += "<row label=\"rLL\">Llandudno</row>\n"
        outputString += "<row label=\"rLN\">Lincoln</row>\n"
        outputString += "<row label=\"rLS\">Leeds</row>\n"
        outputString += "<row label=\"rLU\">Luton</row>\n"
        outputString += "<row label=\"rM\">Manchester</row>\n"
        outputString += "<row label=\"rME\">Rochester</row>\n"
        outputString += "<row label=\"rMK\">Milton Keynes</row>\n"
        outputString += "<row label=\"rML\">Motherwell</row>\n"
        outputString += "<row label=\"rN\">North London</row>\n"
        outputString += "<row label=\"rNE\">Newcastle upon Tyne</row>\n"
        outputString += "<row label=\"rNG\">Nottingham</row>\n"
        outputString += "<row label=\"rNN\">Northampton</row>\n"
        outputString += "<row label=\"rNP\">Newport</row>\n"
        outputString += "<row label=\"rNR\">Norwich</row>\n"
        outputString += "<row label=\"rNW\">North West London</row>\n"
        outputString += "<row label=\"rOL\">Oldham</row>\n"
        outputString += "<row label=\"rOX\">Oxford</row>\n"
        outputString += "<row label=\"rPA\">Paisley</row>\n"
        outputString += "<row label=\"rPE\">Peterborough</row>\n"
        outputString += "<row label=\"rPH\">Perth</row>\n"
        outputString += "<row label=\"rPL\">Plymouth</row>\n"
        outputString += "<row label=\"rPO\">Portsmouth</row>\n"
        outputString += "<row label=\"rPR\">Preston</row>\n"
        outputString += "<row label=\"rRG\">Reading</row>\n"
        outputString += "<row label=\"rRH\">Redhill</row>\n"
        outputString += "<row label=\"rRM\">Romford</row>\n"
        outputString += "<row label=\"rS\">Sheffield</row>\n"
        outputString += "<row label=\"rSA\">Swansea</row>\n"
        outputString += "<row label=\"rSE\">South East London</row>\n"
        outputString += "<row label=\"rSG\">Stevenage</row>\n"
        outputString += "<row label=\"rSK\">Stockport</row>\n"
        outputString += "<row label=\"rSL\">Slough</row>\n"
        outputString += "<row label=\"rSM\">Sutton</row>\n"
        outputString += "<row label=\"rSN\">Swindon</row>\n"
        outputString += "<row label=\"rSO\">Southampton</row>\n"
        outputString += "<row label=\"rSP\">Salisbury</row>\n"
        outputString += "<row label=\"rSR\">Sunderland</row>\n"
        outputString += "<row label=\"rSS\">Southend-on-Sea</row>\n"
        outputString += "<row label=\"rST\">Stoke-on-Trent</row>\n"
        outputString += "<row label=\"rSW\">South West London</row>\n"
        outputString += "<row label=\"rSY\">Shrewsbury</row>\n"
        outputString += "<row label=\"rTA\">Taunton</row>\n"
        outputString += "<row label=\"rTD\">Galashiels</row>\n"
        outputString += "<row label=\"rTF\">Telford</row>\n"
        outputString += "<row label=\"rTN\">Tunbridge Wells</row>\n"
        outputString += "<row label=\"rTQ\">Torquay</row>\n"
        outputString += "<row label=\"rTR\">Truro</row>\n"
        outputString += "<row label=\"rTS\">Cleveland</row>\n"
        outputString += "<row label=\"rTW\">Twickenham</row>\n"
        outputString += "<row label=\"rUB\">Southall</row>\n"
        outputString += "<row label=\"rW\">West London</row>\n"
        outputString += "<row label=\"rWA\">Warrington</row>\n"
        outputString += "<row label=\"rWC\">Western Central London</row>\n"
        outputString += "<row label=\"rWD\">Watford</row>\n"
        outputString += "<row label=\"rWF\">Wakefield</row>\n"
        outputString += "<row label=\"rWN\">Wigan</row>\n"
        outputString += "<row label=\"rWR\">Worcester</row>\n"
        outputString += "<row label=\"rWS\">Walsall</row>\n"
        outputString += "<row label=\"rWV\">Wolverhampton</row>\n"
        outputString += "<row label=\"rYO\">York</row>\n"
        outputString += "<row label=\"rZE\">Lerwick</row>\n"
        outputString += "</radio>"
        
    # Text Question: UK postal code with region punch
    elif var_questionGeneratorValue.get() == lst_questionGeneratorOptions[43]:    
        outputString += "<res label=\"Q#_needFourDigits\">Please enter the first four characters.</res>\n"
        outputString += "<res label=\"Q#_invalidCode\">Please enter a valid postal code.</res>\n"
        outputString += "\n"
        outputString += "<text label=\"Q#\" optional=\"0\"@options>\n"
        outputString += "<title>Question Title</title>\n"
        outputString += "<comment>Please enter the first 4 characters.</comment>\n"
        outputString += "<validate>\n"
        outputString += "if len(Q#.val) != 4:\n"
        outputString += "    error(res.Q#_needFourDigits)\n"
        outputString += "else:\n"
        outputString += "    isValid = Q#.val[0].isalpha() and (Q#.val[1].isalpha() or Q#.val[1].isdigit())\n"
        outputString += "    isOneLetterCode = Q#.val[1].isdigit()\n"
        outputString += "    isLegalRegion = \"r\" + Q#.val[0] in [eachRow.label for eachRow in HP_UKregion.rows] if isOneLetterCode else \"r\" + Q#.val[0:2] in [eachRow.label for eachRow in HP_UKregion.rows]\n"
        outputString += "    if not isLegalRegion:\n"
        outputString += "        error(res.Q#_invalidCode)\n"
        outputString += "</validate>\n"
        outputString += "</text>\n"
        outputString += "\n"
        outputString += "<suspend/>\n"
        outputString += "\n"
        outputString += "<radio label=\"HP_UKregion\" where=\"execute,survey,report\" uses=\"multicol.7\" multicol:count=\"3\">\n"
        outputString += "<title>Hidden Question.  UK region as obtained from Q#.</title>\n"
        outputString += "<exec>\n"
        outputString += "if Q#.val[0].isalpha() and Q#.val[1].isalpha():\n"
        outputString += "    HP_UKregion.val = HP_UKregion.attr(\"r\" + Q#.val[0:2]).index\n"
        outputString += "elif Q#.val[0].isalpha() and Q#.val[1].isdigit():\n"
        outputString += "    HP_UKregion.val = HP_UKregion.attr(\"r\" + Q#.val[0]).index\n"
        outputString += "</exec>\n"
        outputString += "<row label=\"rAB\">Aberdeen</row>\n"
        outputString += "<row label=\"rAL\">St Albans</row>\n"
        outputString += "<row label=\"rB\">Birmingham</row>\n"
        outputString += "<row label=\"rBA\">Bath</row>\n"
        outputString += "<row label=\"rBB\">Blackburn</row>\n"
        outputString += "<row label=\"rBD\">Bradford</row>\n"
        outputString += "<row label=\"rBH\">Bournemouth</row>\n"
        outputString += "<row label=\"rBL\">Bolton</row>\n"
        outputString += "<row label=\"rBN\">Brighton</row>\n"
        outputString += "<row label=\"rBR\">Bromley</row>\n"
        outputString += "<row label=\"rBS\">Bristol</row>\n"
        outputString += "<row label=\"rBT\">Belfast</row>\n"
        outputString += "<row label=\"rCA\">Carlisle</row>\n"
        outputString += "<row label=\"rCB\">Cambridge</row>\n"
        outputString += "<row label=\"rCF\">Cardiff</row>\n"
        outputString += "<row label=\"rCH\">Chester</row>\n"
        outputString += "<row label=\"rCM\">Chelmsford</row>\n"
        outputString += "<row label=\"rCO\">Colchester</row>\n"
        outputString += "<row label=\"rCR\">Croydon</row>\n"
        outputString += "<row label=\"rCT\">Canterbury</row>\n"
        outputString += "<row label=\"rCV\">Coventry</row>\n"
        outputString += "<row label=\"rCW\">Crewe</row>\n"
        outputString += "<row label=\"rDA\">Dartford</row>\n"
        outputString += "<row label=\"rDD\">Dundee</row>\n"
        outputString += "<row label=\"rDE\">Derby</row>\n"
        outputString += "<row label=\"rDG\">Dumfries</row>\n"
        outputString += "<row label=\"rDH\">Durham</row>\n"
        outputString += "<row label=\"rDL\">Darlington</row>\n"
        outputString += "<row label=\"rDN\">Doncaster</row>\n"
        outputString += "<row label=\"rDT\">Dorchester</row>\n"
        outputString += "<row label=\"rDY\">Dudley</row>\n"
        outputString += "<row label=\"rE\">East London</row>\n"
        outputString += "<row label=\"rEC\">East Central London</row>\n"
        outputString += "<row label=\"rEH\">Edinburgh</row>\n"
        outputString += "<row label=\"rEN\">Enfield</row>\n"
        outputString += "<row label=\"rEX\">Exeter</row>\n"
        outputString += "<row label=\"rFK\">Falkirk</row>\n"
        outputString += "<row label=\"rFY\">Blackpool</row>\n"
        outputString += "<row label=\"rG\">Glasgow</row>\n"
        outputString += "<row label=\"rGL\">Gloucester</row>\n"
        outputString += "<row label=\"rGU\">Guildford</row>\n"
        outputString += "<row label=\"rHA\">Harrow</row>\n"
        outputString += "<row label=\"rHD\">Huddersfield</row>\n"
        outputString += "<row label=\"rHG\">Harrogate</row>\n"
        outputString += "<row label=\"rHP\">Hemel Hempstead</row>\n"
        outputString += "<row label=\"rHR\">Hereford</row>\n"
        outputString += "<row label=\"rHS\">Outer Hebrides</row>\n"
        outputString += "<row label=\"rHU\">Hull</row>\n"
        outputString += "<row label=\"rHX\">Halifax</row>\n"
        outputString += "<row label=\"rIG\">Ilford</row>\n"
        outputString += "<row label=\"rIP\">Ipswich</row>\n"
        outputString += "<row label=\"rIV\">Inverness</row>\n"
        outputString += "<row label=\"rKA\">Kilmarnock</row>\n"
        outputString += "<row label=\"rKT\">Kingston upon Thames</row>\n"
        outputString += "<row label=\"rKW\">Kirkwall</row>\n"
        outputString += "<row label=\"rKY\">Kirkcaldy</row>\n"
        outputString += "<row label=\"rL\">Liverpool</row>\n"
        outputString += "<row label=\"rLA\">Lancaster</row>\n"
        outputString += "<row label=\"rLD\">Llandrindod Wells</row>\n"
        outputString += "<row label=\"rLE\">Leicester</row>\n"
        outputString += "<row label=\"rLL\">Llandudno</row>\n"
        outputString += "<row label=\"rLN\">Lincoln</row>\n"
        outputString += "<row label=\"rLS\">Leeds</row>\n"
        outputString += "<row label=\"rLU\">Luton</row>\n"
        outputString += "<row label=\"rM\">Manchester</row>\n"
        outputString += "<row label=\"rME\">Rochester</row>\n"
        outputString += "<row label=\"rMK\">Milton Keynes</row>\n"
        outputString += "<row label=\"rML\">Motherwell</row>\n"
        outputString += "<row label=\"rN\">North London</row>\n"
        outputString += "<row label=\"rNE\">Newcastle upon Tyne</row>\n"
        outputString += "<row label=\"rNG\">Nottingham</row>\n"
        outputString += "<row label=\"rNN\">Northampton</row>\n"
        outputString += "<row label=\"rNP\">Newport</row>\n"
        outputString += "<row label=\"rNR\">Norwich</row>\n"
        outputString += "<row label=\"rNW\">North West London</row>\n"
        outputString += "<row label=\"rOL\">Oldham</row>\n"
        outputString += "<row label=\"rOX\">Oxford</row>\n"
        outputString += "<row label=\"rPA\">Paisley</row>\n"
        outputString += "<row label=\"rPE\">Peterborough</row>\n"
        outputString += "<row label=\"rPH\">Perth</row>\n"
        outputString += "<row label=\"rPL\">Plymouth</row>\n"
        outputString += "<row label=\"rPO\">Portsmouth</row>\n"
        outputString += "<row label=\"rPR\">Preston</row>\n"
        outputString += "<row label=\"rRG\">Reading</row>\n"
        outputString += "<row label=\"rRH\">Redhill</row>\n"
        outputString += "<row label=\"rRM\">Romford</row>\n"
        outputString += "<row label=\"rS\">Sheffield</row>\n"
        outputString += "<row label=\"rSA\">Swansea</row>\n"
        outputString += "<row label=\"rSE\">South East London</row>\n"
        outputString += "<row label=\"rSG\">Stevenage</row>\n"
        outputString += "<row label=\"rSK\">Stockport</row>\n"
        outputString += "<row label=\"rSL\">Slough</row>\n"
        outputString += "<row label=\"rSM\">Sutton</row>\n"
        outputString += "<row label=\"rSN\">Swindon</row>\n"
        outputString += "<row label=\"rSO\">Southampton</row>\n"
        outputString += "<row label=\"rSP\">Salisbury</row>\n"
        outputString += "<row label=\"rSR\">Sunderland</row>\n"
        outputString += "<row label=\"rSS\">Southend-on-Sea</row>\n"
        outputString += "<row label=\"rST\">Stoke-on-Trent</row>\n"
        outputString += "<row label=\"rSW\">South West London</row>\n"
        outputString += "<row label=\"rSY\">Shrewsbury</row>\n"
        outputString += "<row label=\"rTA\">Taunton</row>\n"
        outputString += "<row label=\"rTD\">Galashiels</row>\n"
        outputString += "<row label=\"rTF\">Telford</row>\n"
        outputString += "<row label=\"rTN\">Tunbridge Wells</row>\n"
        outputString += "<row label=\"rTQ\">Torquay</row>\n"
        outputString += "<row label=\"rTR\">Truro</row>\n"
        outputString += "<row label=\"rTS\">Cleveland</row>\n"
        outputString += "<row label=\"rTW\">Twickenham</row>\n"
        outputString += "<row label=\"rUB\">Southall</row>\n"
        outputString += "<row label=\"rW\">West London</row>\n"
        outputString += "<row label=\"rWA\">Warrington</row>\n"
        outputString += "<row label=\"rWC\">Western Central London</row>\n"
        outputString += "<row label=\"rWD\">Watford</row>\n"
        outputString += "<row label=\"rWF\">Wakefield</row>\n"
        outputString += "<row label=\"rWN\">Wigan</row>\n"
        outputString += "<row label=\"rWR\">Worcester</row>\n"
        outputString += "<row label=\"rWS\">Walsall</row>\n"
        outputString += "<row label=\"rWV\">Wolverhampton</row>\n"
        outputString += "<row label=\"rYO\">York</row>\n"
        outputString += "<row label=\"rZE\">Lerwick</row>\n"
        outputString += "</radio>"
        
    else:
        outputString = "This has not been implemented yet."
        
    # If "Include <suspend/> tag at end" is checked.
    if var_questionGeneratorSuspend.get() == 1:
        outputString += "\n\n<suspend/>"
        
    # If "Replace Q# with this label" is checked.
    if var_questionGeneratorReplace.get() == 1:
        outputString = outputString.replace("Q#", var_questionGeneratorReplaceText.get())
        
    # Replace "@options" with where="execute,survey,report" or shuffle="whatever".
    replacementString = ""
    shuffleList = ""
    
    numShuffleOptions = var_questionGeneratorShuffleRows.get() + var_questionGeneratorShuffleCols.get() + var_questionGeneratorShuffleChoices.get() + var_questionGeneratorShuffleGroups.get()
    
    if numShuffleOptions > 0:
        replacementString += "shuffle=\"@shufflelist\" "
    
        if var_questionGeneratorShuffleRows.get() == 1:
            shuffleList += "rows"
            numShuffleOptions -= 1
            if numShuffleOptions > 0:
                shuffleList += ","
                
        if var_questionGeneratorShuffleCols.get() == 1:
            shuffleList += "cols"
            numShuffleOptions -= 1
            if numShuffleOptions > 0:
                shuffleList += ","
                
        if var_questionGeneratorShuffleChoices.get() == 1:
            shuffleList += "choices"
            numShuffleOptions -= 1
            if numShuffleOptions > 0:
                shuffleList += ","
                
        if var_questionGeneratorShuffleGroups.get() == 1:
            shuffleList += "groups"
            numShuffleOptions -= 1
            if numShuffleOptions > 0:
                shuffleList += ","
                
        replacementString = replacementString.replace("@shufflelist", shuffleList)
        
    if var_questionGeneratorHiddenQuestion.get() == 1:
        replacementString += "where=\"execute,survey,report\" "
        
    if var_questionGeneratorUntranslateable.get() == 1:
        replacementString += "translateable=\"0\" "
        
    replacementString = replacementString.strip()
    
    if len(replacementString) > 0:
        replacementString = " " + replacementString
    
    outputString = outputString.replace("@options", replacementString)
    
    # Replace "@elements" with the default text or with the contents of the element output, depending on if the box was checked.
    if var_elementGeneratorCopyOutputToQuestionGenerator.get() == 1:
        outputString = outputString.replace("@elements", txt_elementGeneratorTextOutput.get(1.0, END).strip())
    else:
        outputString = outputString.replace("@elements", "[Replace this line with any elements needed]")
    
    # If the "replace 'Question Title' with this text" box is checked.
    if var_questionGeneratorReplaceTitle.get() == 1:
    
        # Split the contents by tabs, if there are two elements in the result then only use the second one.
        splitInput = var_questionGeneratorTitleReplacement.get().split("    ")
        
        if len(splitInput) == 2:
            outputString = outputString.replace("Question Title", splitInput[1].strip())
        else:
            outputString = outputString.replace("Question Title", var_questionGeneratorTitleReplacement.get().strip())
    
    # Place the resulting text in the output box.
    textarea.delete(1.0, END)
    textarea.insert(END, outputString)
    
    # If "Append all output to this file" is checked:
    if var_questionGeneratorAppendFile.get() == 1:
        writeToFile(var_questionGeneratorFilename.get(), textarea)
        
    # If auto-incrementing.
    if var_questionGeneratorReplace.get() == 1 and var_questionGeneratorAutoIncrement.get() == 1:
        incrementQuestionNumber()
        
def questionGenerateAndCopy(textarea):
    questionGenerate(textarea)
    root.clipboard_clear()
    copyText = textarea.get(1.0, END)
    root.clipboard_append(copyText)
    textarea.insert(1.0, "The below was copied to the clipboard:\n======================================\n")
    
def writeToFile(filename, textarea):
    if filename != "":
        try:
            myfile = open(filename, "a")
            textToWrite = textarea.get(1.0, END)
            myfile.write(textToWrite + "\n\n")
            myfile.close()
            textarea.insert(1.0, "The below was appended to " + filename + ":\n======================================\n")
        except Exception as e:
            textarea.insert(1.0, "Could not open specified file - " + e.strerror + "\n======================================\n")
    else:
        textarea.insert(1.0, "Could not write to file; no filename specified.\n======================================\n")
    
def elementGenerate(inputTextArea, outputTextArea, append=False):
    rawInput = inputTextArea.get(1.0, END)
    rawInput = rawInput.strip()
    elementType = ""
    elementPrefix = ""
    splitInput = []
    outputString = ""
    actionSelected = "Creating"
    
    # Creating.
    if var_elementGeneratorValue.get() in [lst_elementGeneratorOptions[0], lst_elementGeneratorOptions[1], lst_elementGeneratorOptions[2], lst_elementGeneratorOptions[3]]:
        actionSelected = "Creating"
    
    # Converting.
    elif var_elementGeneratorValue.get() in [lst_elementGeneratorOptions[4], lst_elementGeneratorOptions[5], lst_elementGeneratorOptions[6], lst_elementGeneratorOptions[7]]:
        actionSelected = "Converting"
        
    # Swapping.
    elif var_elementGeneratorValue.get() in [lst_elementGeneratorOptions[8]]:
        actionSelected = "Swapping"
    
    
    if actionSelected == "Creating":
    
        # If creating rows.
        if var_elementGeneratorValue.get() == lst_elementGeneratorOptions[0]:
            elementType = "row"
            elementPrefix = "r"
        
        # If creating cols.
        elif var_elementGeneratorValue.get() == lst_elementGeneratorOptions[1]:
            elementType = "col"
            elementPrefix = "c"
        
        # If creating choices.
        elif var_elementGeneratorValue.get() == lst_elementGeneratorOptions[2]:
            elementType = "choice"
            elementPrefix = "ch"
            
        # If creating groups.
        elif var_elementGeneratorValue.get() == lst_elementGeneratorOptions[3]:
            elementType = "group"
            elementPrefix = "g"
        
        # Search for "!NUMLIST!number!number"; if match and first number equal to or less than second number, then replace the string with
        # a number list separated by the specified delimiter
        searchRegex = re.compile("!NUMLIST!\d+!\d+")
        matchRegex = searchRegex.match(rawInput)
        
        if matchRegex != None:
            numListString = matchRegex.group()
            splitNumListString = numListString.split("!")
            firstNumber = int(splitNumListString[2])
            secondNumber = int(splitNumListString[3])
            
            replaceString = ""
            
            for i in range(firstNumber, secondNumber + 1):
                replaceString += str(i)
                
                if i < secondNumber:
                    if var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[0]:
                        replaceString += "\n"
                    elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[1]:
                        replaceString += "    "
                    elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[2]:
                        replaceString += ","
                        
            rawInput = rawInput.replace(numListString, replaceString)
            
        # Search for "!ORDLIST!number!number"; pretty much does the same thing as before but adds "st", "nd", "rd", "th" to the end of the numbers.
        searchRegex = re.compile("!ORDLIST!\d+!\d+")
        matchRegex = searchRegex.match(rawInput)
        
        if matchRegex != None:
            numListString = matchRegex.group()
            splitNumListString = numListString.split("!")
            firstNumber = int(splitNumListString[2])
            secondNumber = int(splitNumListString[3])
            
            replaceString = ""
            
            for i in range(firstNumber, secondNumber + 1):
                replaceString += str(i)
                
                if i % 10 == 1 and i % 100 == 11:
                    replaceString += "th"
                elif i % 10 == 1:
                    replaceString += "st"
                elif i % 10 == 2 and i % 100 == 12:
                    replaceString += "th"
                elif i % 10 == 2:
                    replaceString += "nd"
                elif i % 10 == 3 and i % 100 == 13:
                    replaceString += "th"
                elif i % 10 == 3:
                    replaceString += "rd"
                else:
                    replaceString += "th"
                
                if i < secondNumber:
                    if var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[0]:
                        replaceString += "\n"
                    elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[1]:
                        replaceString += "    "
                    elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[2]:
                        replaceString += ","
                        
            rawInput = rawInput.replace(numListString, replaceString)

        # Replace curved quotes with straight quotes.
        rawInput = rawInput.replace( "\u2018", "'" )
        rawInput = rawInput.replace( "\u2019", "'" )
        rawInput = rawInput.replace( "\u201C", "\"" )
        rawInput = rawInput.replace( "\u201D", "\"" )
        
        # Split based on delimiter.
        if var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[0]:
            splitInput = rawInput.split("\n")
        elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[1]:
            splitInput = rawInput.split("    ")
        elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[2]:
            splitInput = rawInput.split(",")
                
        # Remove leading and trailing whitespace, fix &/</> characters, and split each item in splitInput by tabs and if the length is 2, take only the second part.
        for i in range(0, len(splitInput)):
            splitInput[i] = splitInput[i].strip()
            splitInput[i] = splitInput[i].replace("&", "&amp;")
            splitInput[i] = splitInput[i].replace("<", "&lt;")
            splitInput[i] = splitInput[i].replace(">", "&gt;")
            
            secondSplitInput = splitInput[i].split("    ")
            if len(secondSplitInput) == 2:
                splitInput[i] = secondSplitInput[1].strip()
        
        # Get the starting index number.
        try:
            startingIndex = int(var_elementGeneratorStartingIndex.get())
        except ValueError:
            startingIndex = 1
        
        # Build the output string.
        for j in range(0, len(splitInput)):
            outputString += "<"
            outputString += elementType
            outputString += " label=\""
            outputString += elementPrefix
            
            isOEorExclusive = False
            isOE = False
            isExclusive = False
            
            # If detecting OE.
            if var_elementGeneratorDetectOE.get() == 1:
                lowerCaseInput = splitInput[j].lower()
                if "specify" in lowerCaseInput or "textbox" in lowerCaseInput or "text box" in lowerCaseInput or "fill in" in lowerCaseInput or "fill-in" in lowerCaseInput or "write in" in lowerCaseInput or "write-in" in lowerCaseInput:
                    isOEorExclusive = True
                    isOE = True
                    #
            
            # If detecting exclusive.
            if var_elementGeneratorDetectEXC.get() == 1:
                lowerCaseInput = splitInput[j].lower()
                if "exclusive" in lowerCaseInput or "none of these" in lowerCaseInput or "none of the above" in lowerCaseInput or "prefer not to answer" in lowerCaseInput or "don't know" in lowerCaseInput:
                    isOEorExclusive = True
                    isExclusive = True
                    #
            
            # If the "replace index if OE/exclusive" box is checked.
            if isOEorExclusive and var_elementGeneratorReplaceOpenEndAndExclusiveIndexes.get() == 1:
                if isOE:
                    outputString += "98"
                elif isExclusive:
                    outputString += "99"
            else:
                # If reversing index order.
                if var_elementGeneratorReverseOrder.get() == 1:
                    outputString += str(len(splitInput) + startingIndex - (j + 1))
                else:
                    outputString += str(j + startingIndex)
            
            outputString += "\""
            
            if isOE:
                outputString += " open=\"1\" openSize=\"25\""
            if isExclusive:
                outputString += " exclusive=\"1\""
            
            # If including values.
            if var_elementGeneratorIncludeValues.get() == 1:
                outputString += " value=\""
                
                if isOEorExclusive and var_elementGeneratorReplaceOpenEndAndExclusiveIndexes.get() == 1:
                    if isOE:
                        outputString += "98"
                    elif isExclusive:
                        outputString += "99"
                else:
                    # If reversing index order.
                    if var_elementGeneratorReverseOrder.get() == 1:
                        outputString += str(len(splitInput) + startingIndex - (j + 1))
                    else:
                        outputString += str(j + startingIndex)
                
                outputString += "\""
            
            # If anchoring OEs/exclusives.
            if var_elementGeneratorAnchor.get() == 1 and isOEorExclusive:
                outputString += " randomize=\"0\""
            
            # If removing text within brackets.
            if var_elementGeneratorRemoveBrackets.get() == 1:
                splitInput[j] = re.sub(r"\[.+\]", "", splitInput[j])
            
            splitInput[j] = splitInput[j].strip()
            
            outputString += ">"
            outputString += splitInput[j]
            outputString += "</"
            outputString += elementType
            outputString += ">\n"
    
    elif actionSelected == "Converting":
    
        # If converting to rows.
        if var_elementGeneratorValue.get() == lst_elementGeneratorOptions[4]:
            elementType = "row"
            elementPrefix = "r"
        
        # If converting to cols.
        elif var_elementGeneratorValue.get() == lst_elementGeneratorOptions[5]:
            elementType = "col"
            elementPrefix = "c"
        
        # If converting to choices.
        elif var_elementGeneratorValue.get() == lst_elementGeneratorOptions[6]:
            elementType = "choice"
            elementPrefix = "ch"
            
        # If converting to groups.
        elif var_elementGeneratorValue.get() == lst_elementGeneratorOptions[7]:
            elementType = "group"
            elementPrefix = "g"
            
        # If delimited by lines.
        if var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[0]:
            splitInput = rawInput.split("\n")
        
        # If delimited by tabs.
        elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[1]:
            splitInput = rawInput.split("    ")
        
        # If delimited by commas.
        elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[2]:
            splitInput = rawInput.split(",")
            
        for i in splitInput:
            i = i.replace("<row", "<" + elementType)
            i = i.replace("<col", "<" + elementType)
            i = i.replace("<choice", "<" + elementType)
            i = i.replace("<group", "<" + elementType)
            i = i.replace("</row", "</" + elementType)
            i = i.replace("</col", "</" + elementType)
            i = i.replace("</choice", "</" + elementType)
            i = i.replace("</group", "</" + elementType)
            i = i.replace("label=\"r", "label=\"" + elementPrefix)
            i = i.replace("label=\"c", "label=\"" + elementPrefix)
            i = i.replace("label=\"ch", "label=\"" + elementPrefix)
            i = i.replace("label=\"chh", "label=\"" + elementPrefix)
            i = i.replace("label=\"g", "label=\"" + elementPrefix)
            outputString += (i + "\n")

    elif actionSelected == "Swapping":
    
        # If delimited by lines.
        if var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[0]:
            splitInput = rawInput.split("\n")
        
        # If delimited by tabs.
        elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[1]:
            splitInput = rawInput.split("    ")
        
        # If delimited by commas.
        elif var_elementGeneratorDelimeterValue.get() == lst_elementGeneratorDelimiterOptions[2]:
            splitInput = rawInput.split(",")
        
        typesIncludedL = []
        typesIncludedS = []
        
        for i in splitInput:
            if "<row" in i and "/<row>" and not("r" in typesIncludedS):
                typesIncludedS.append("r")
                typesIncludedL.append("row")
            elif "<col" in i and "/<col>" and not("c" in typesIncludedS):
                typesIncludedS.append("c")
                typesIncludedL.append("col")
            elif "<choice" in i and "/<choice>" and not("ch" in typesIncludedS):
                typesIncludedS.append("ch")
                typesIncludedL.append("choice")
            elif "<group" in i and "/<group>" and not("g" in typesIncludedS):
                typesIncludedS.append("g")
                typesIncludedL.append("group")
                
        if len(typesIncludedL) != 2:
            outputString = "Error: This feature requires exactly 2 types of elements"
            
        else:
            type1 = typesIncludedL[0]
            type2 = typesIncludedL[1]
            type1S = typesIncludedS[0]
            type2S = typesIncludedS[1]
            
            for i in splitInput:
                if ("<" + type1) in i:
                    i = i.replace("<" + type1, "<" + type2)
                    i = i.replace("</" + type1, "</" + type2)
                    i = i.replace("label=\"" + type1S, "label=\"" + type2S)
                elif ("<" + type2) in i:
                    i = i.replace("<" + type2, "<" + type1)
                    i = i.replace("</" + type2, "</" + type1)
                    i = i.replace("label=\"" + type2S, "label=\"" + type1S)
                outputString += (i + "\n")
    
    else:
        outputString = "This feature has not been implemented yet."
    
    outputString = outputString.strip()
    
    if not(append):
        outputTextArea.delete(1.0, END)
    else:
        outputTextArea.insert(END, "\n")
        
    outputTextArea.insert(END, outputString)
    
def elementGenerateAndCopy(inputTextArea, outputTextArea):
    elementGenerate(inputTextArea, outputTextArea)
    root.clipboard_clear()
    copyText = outputTextArea.get(1.0, END)
    root.clipboard_append(copyText)
    outputTextArea.insert(1.0, "The below was copied to the clipboard:\n======================================\n")

def elementClear(inputTextArea):
    inputTextArea.delete(1.0, END)
    
def incrementQuestionNumber(mode="inc"):
    originalString = var_questionGeneratorReplaceText.get()
    originalStringLength = len(originalString)
    modifiedString = ""

    if mode == "inc":    # Increment label.
        
        # Last character is letter
        if originalStringLength == 0:
            modifiedString = "Q1"
            
        elif originalString[-1].isalpha():
            # Last character is 'z' or 'Z': replace last character with 'aa' or 'AA'
            if originalString[-1] == "z":
                modifiedString = originalString[0:originalStringLength - 1] + "aa"
            elif originalString[-1] == "Z":
                modifiedString = originalString[0:originalStringLength - 1] + "AA"
            # Last character isn't 'z' or 'Z': replace last character with next letter
            else:
                modifiedString = originalString[0:originalStringLength - 1] + chr(ord(originalString[-1]) + 1) 
        
        # Last character is number: increment number
        elif originalString[-1].isdigit():
            numberString = originalString[-1]
            myRange = list(range(0, originalStringLength - 1))
            myRange.reverse()
            for i in myRange:
                if originalString[i].isdigit():
                    numberString = originalString[i] + numberString
                else:
                    break
            numberStringAsNumber = int(numberString)
            numberStringAsNumber += 1
            numberStringNew = str(numberStringAsNumber)
            modifiedString = originalString[0:originalStringLength - len(numberString)] + numberStringNew
        
        # Fallback
        else:
            modifiedString = "Q1"
    
    elif mode == "dec":        # Decrement label.
        
        if originalStringLength == 0:
            modifiedString = "Q1"
        
        # Last character is number: find the full number at the end
        elif originalString[-1].isdigit():
        
            numberString = originalString[-1]
            myRange = list(range(0, originalStringLength - 1))
            myRange.reverse()
            for i in myRange:
                if originalString[i].isdigit():
                    numberString = originalString[i] + numberString
                else:
                    break
            numberStringAsNumber = int(numberString)
        
            # Number is zero: Omit the number
            if numberStringAsNumber == 0:
                modifiedString = originalString[:-1]
            
            # Number is not zero: Decrement then replace
            else:
                numberStringAsNumber -= 1
                modifiedString = originalString[:-len(numberString)] + str(numberStringAsNumber)
        
        # Last character is alpha: find the full letter string at the end
        elif originalString[-1].isalpha():
        
            # String ends in "aa"/"AA": replace with "z"/"Z"
            if originalString[-2:] == "aa":
                modifiedString = originalString[:-2] + "z"
            elif originalString[-2:] == "AA":
                modifiedString = originalString[:-2] + "Z"
            
            # String ends in "a"/"A": omit the letter
            elif originalString[-1] == "a" or originalString[-1] == "A":
                modifiedString = originalString[:-1]
            
            # String ends in any other letter: decrement then replace            
            else:
                modifiedString = originalString[:-1] + chr(ord(originalString[-1]) - 1)
        
        # Fallback
        else:
            modifiedString = "Q1"
        
    elif mode == "add":        # Add suffix.
        
        # Last character is letter: append "1"
        if originalStringLength > 0 and originalString[-1].isalpha():
            modifiedString = originalString + "1"
        
        # Last character is number: append "A"
        elif originalStringLength > 0 and originalString[-1].isdigit():
            modifiedString = originalString + "A"
        
        # Fallback.
        else:
            modifiedString = "Q1"
        
    elif mode == "rem":        # Remove suffix.
        
        # Last character is letter: find then remove all letters at end
        if originalStringLength > 0 and originalString[-1].isalpha():
        
            letterString = originalString[-1]
            myRange = list(range(0, originalStringLength - 1))
            myRange.reverse()
            for i in myRange:
                if originalString[i].isalpha():
                    letterString = originalString[i] + letterString
                else:
                    break
            lastStringLength = len(letterString)
            
            modifiedString = originalString[:-lastStringLength]
        
        # Last character is number: find then remove all numbers at end
        elif originalStringLength > 0 and originalString[-1].isdigit():
        
            numberString = originalString[-1]
            myRange = list(range(0, originalStringLength - 1))
            myRange.reverse()
            for i in myRange:
                if originalString[i].isdigit():
                    numberString = originalString[i] + numberString
                else:
                    break
            lastStringLength = len(numberString)
            
            modifiedString = originalString[:-lastStringLength]
        
        # Fallback.
        else:
            modifiedString = "Q1"
    
    var_questionGeneratorReplaceText.set(modifiedString)
    
    
def elementResetDefaults(inputTextArea):
    var_elementGeneratorStartingIndex.set("1")
    var_elementGeneratorIncludeValues.set("1")
    var_elementGeneratorRemoveBrackets.set("1")
    var_elementGeneratorDetectOE.set("1")
    var_elementGeneratorDetectEXC.set("1")
    var_elementGeneratorReverseOrder.set("0")
    var_elementGeneratorAnchor.set("0")
    var_elementGeneratorValue.set(lst_elementGeneratorOptions[0])
    var_elementGeneratorDelimeterValue.set(lst_elementGeneratorDelimiterOptions[0])
    var_elementGeneratorReplaceOpenEndAndExclusiveIndexes.set("1")


    
#==================================================
# RESOURCE DEFINITIONS
#==================================================
str_version = "1.045" 
str_tagline = " \"yeah i'm back\""
str_date = "17 September 2021"
str_titleText = "Ed's Decipher element generator v. " + str_version + str_tagline + " - Python Version - " + str_date
str_titleTextB = "Ed's Decipher element generator v. " + str_version

str_questionGeneratorTitle = "Question Generator"
str_questionGeneratorPrompt = "Select a question type:"
str_questionGeneratorShuffleLabel = "Shuffle:"
str_questionGeneratorShuffleRows = "Rows"
str_questionGeneratorShuffleCols = "Cols"
str_questionGeneratorShuffleChoices = "Choices"
str_questionGeneratorShuffleGroups = "Groups"
str_questionGeneratorHiddenQuestion = "Hidden Question"
str_questionGeneratorUntranslateable = "Untranslateable"
str_questionGeneratorBtnGenerate = "Generate"
str_questionGeneratorBtnGenerateAndCopy = "Generate and Copy to Clipboard"
str_questionGeneratorChkSuspend = "Include <suspend/> tag at end"
str_questionGeneratorChkReplace = "Replace \"Q#\" with this label:"
str_questionGeneratorAppendOutput = "Append all output to this file:"
str_questionGeneratorReplaceTitle = "Replace \"Question Title\" with:"
str_questionGeneratorBrowseFile = "Browse..."
str_questionGeneratorAutoIncrement = "Auto-increment"

str_elementGeneratorTitle = "Element Generator"
str_elementGeneratorPrompt = "Select an element type:"
str_elementGeneratorInput = "Input"
str_elementGeneratorOutput = "Output"
str_elementGeneratorDelimiter = "Delimeter:"
str_elementGeneratorBtnGenerate = "Generate"
str_elementGeneratorBtnAppend = "Append"
str_elementGeneratorBtnGenerateAndCopy = "Generate and Copy to Clipboard"
str_elementGeneratorBtnClear = "Clear"
str_elementGeneratorBtnDefault = "Reset Defaults"
str_elementGeneratorStartingIndex = "Starting index:"
str_elementGeneratorIncludeValues = "Include values"
str_elementGeneratorRemoveBrackets = "Remove text within [] brackets"
str_elementGeneratorReverseOrder = "Reverse index order"
str_elementGeneratorDetectOE = "Detect open end"
str_elementGeneratorDetectEXC = "Detect exclusive"
str_elementGeneratorAnchor = "Anchor OEs/exclusives"
str_elementGeneratorReplaceOpenEndAndExclusiveIndexes = "Replace OE/exclusive indexes and values with 98/99"
str_elementGeneratorCopyOutputToQuestionGenerator = "Copy output contents to question generator"

# IMPORTANT: Add new options at the end of the lists.
lst_questionGeneratorOptions = [
    "Radio: Generic Question",
    "Checkbox: Generic Question",
    "Select: Generic Question",
    "Number: Generic Question",
    "Text: Generic Question",
    "Textarea: Generic Question",
    "HTML: Generic Element",
    "Radio: Yes/No",
    "Radio: Gender",
    "Radio: Age",
    "Radio: Income",
    "Radio: Ethnicity",
    "Radio: US State",
    "Radio: US State with region punch",
    "Radio: 0-5 Scale",
    "Radio: 1-5 Scale",
    "Radio: 0-7 Scale",
    "Radio: 1-7 Scale",
    "Radio: 0-10 Scale",
    "Radio: 1-10 Scale",
    "Checkbox: Ethnicity",
    "Select: US State",
    "Select: US State with region punch",
    "Number: Age",
    "Number: Age with age group punch",
    "Text: Zipcode",
    "Text: Zipcode with DMA template",
    "Text: Phone Number",
    "Radio: Education Level",
    "Text: CA postal code (3 chars.)",
    "Text: CA postal code with province punch",
    "Radio: CA province",
    "Select: CA province",
    "Radio: Level of agreement (4 points)",
    "Radio: Level of agreement (5 points)",
    "Radio: Multicolumn",
    "Checkbox: Multicolumn",
    "Radio: Button select",
    "Checkbox: Button select",
    "Number: Autosum",
    "Number: Slider",
    "Select: Ranksort",
    "Radio: UK region",
    "Text: UK postal code with region punch"
]

lst_elementGeneratorOptions = [
    "Create Rows",
    "Create Columns",
    "Create Choices",
    "Create Groups",
    "Convert to Rows",
    "Convert to Columns",
    "Convert to Choices",
    "Convert to Groups",
    "Swap Element Types"
]

lst_elementGeneratorDelimiterOptions = [
    "Lines",
    "Tabs",
    "Commas"
]

#==================================================
# MAIN CODE
#==================================================

root = Tk()
root.wm_title(str_titleTextB)
root.geometry("1080x830+0+0")

# Intro text.
lbl_titleText = Label(text=str_titleText, justify=LEFT, font="Consolas 10").place(x = 10, y = 10)
    
# Question element generator.
lbl_questionGeneratorTitle = Label(text=str_questionGeneratorTitle, justify=LEFT, font="Consolas 10").place(x = 10, y = 50)
lbl_questionGeneratorPrompt = Label(text=str_questionGeneratorPrompt, justify=LEFT, font="Consolas 10").place(x = 10, y = 70)
var_questionGeneratorValue = StringVar(root)
var_questionGeneratorValue.set(lst_questionGeneratorOptions[0])
#    opt_questionGeneratorOptionSelector = apply(OptionMenu, (root, var_questionGeneratorValue) + tuple(lst_questionGeneratorOptions))
opt_questionGeneratorOptionSelector = OptionMenu(root, var_questionGeneratorValue, *lst_questionGeneratorOptions).place(x = 180, y = 60)

lbl_questionGeneratorShuffleLabel = Label(text=str_questionGeneratorShuffleLabel, justify=LEFT, font="Consolas 10").place(x = 450, y = 70)
var_questionGeneratorShuffleRows = IntVar()
chk_questionGeneratorShuffleRows = Checkbutton(root, text=str_questionGeneratorShuffleRows, variable=var_questionGeneratorShuffleRows, font="Consolas 10").place(x = 515, y = 68)
var_questionGeneratorShuffleCols = IntVar()
chk_questionGeneratorShuffleCols = Checkbutton(root, text=str_questionGeneratorShuffleCols, variable=var_questionGeneratorShuffleCols, font="Consolas 10").place(x = 570, y = 68)
var_questionGeneratorShuffleChoices = IntVar()
chk_questionGeneratorShuffleChoices = Checkbutton(root, text=str_questionGeneratorShuffleChoices, variable=var_questionGeneratorShuffleChoices, font="Consolas 10").place(x = 625, y = 68)
var_questionGeneratorShuffleGroups = IntVar()
chk_questionGeneratorShuffleGroups = Checkbutton(root, text=str_questionGeneratorShuffleGroups, variable=var_questionGeneratorShuffleGroups, font="Consolas 10").place(x = 700, y = 68)
var_questionGeneratorHiddenQuestion = IntVar()
chk_questionGeneratorHiddenQuestion = Checkbutton(root, text=str_questionGeneratorHiddenQuestion, variable=var_questionGeneratorHiddenQuestion, font="Consolas 10").place(x = 785, y = 68)
var_questionGeneratorUntranslateable = IntVar()
chk_questionGeneratorUntranslateable = Checkbutton(root, text=str_questionGeneratorUntranslateable, variable=var_questionGeneratorUntranslateable, font="Consolas 10").place(x = 930, y = 68)


txt_questionGeneratorTextOutput = Text(root, height=16, width=120)
txt_questionGeneratorTextOutput.place(x = 10, y = 150)
btn_questionGeneratorBtnGenerate = Button(root, text=str_questionGeneratorBtnGenerate, command=lambda: questionGenerate(txt_questionGeneratorTextOutput), font="Consolas 10").place(x = 10, y = 90)
btn_questionGeneratorBtnGenerateAndCopy = Button(root, text=str_questionGeneratorBtnGenerateAndCopy, command=lambda: questionGenerateAndCopy(txt_questionGeneratorTextOutput), font="Consolas 10").place(x = 80, y = 90)
var_questionGeneratorSuspend = IntVar()
chk_questionGeneratorSuspend = Checkbutton(root, text=str_questionGeneratorChkSuspend, variable=var_questionGeneratorSuspend, font="Consolas 10").place(x = 310, y = 90)
var_questionGeneratorReplace = IntVar()
chk_questionGeneratorReplace = Checkbutton(root, text=str_questionGeneratorChkReplace, variable=var_questionGeneratorReplace, font="Consolas 10").place(x = 550, y = 90)
var_questionGeneratorReplaceText = StringVar()
var_questionGeneratorReplaceText.set("Q1")
ent_questionGeneratorReplace = Entry(root, width=5, textvariable=var_questionGeneratorReplaceText, font="Consolas 10").place(x = 780, y = 90)

btn_questionGeneratorIncrementLabel = Button(root, text='\u25B2', command=lambda: incrementQuestionNumber("inc"), font="Consolas 10").place(x = 825, y = 88)
btn_questionGeneratorDecrementLabel = Button(root, text='\u25BC', command=lambda: incrementQuestionNumber("dec"), font="Consolas 10").place(x = 850, y = 88)
btn_questionGeneratorAddLabelSuffix = Button(root, text='\u25B6', command=lambda: incrementQuestionNumber("add"), font="Consolas 10").place(x = 875, y = 88)
btn_questionGeneratorRemoveLabelSuffix = Button(root, text='\u25C0', command=lambda: incrementQuestionNumber("rem"), font="Consolas 10").place(x = 903, y = 88)

var_questionGeneratorAutoIncrement = IntVar()
chk_questionGeneratorAutoIncrement = Checkbutton(root, text=str_questionGeneratorAutoIncrement, variable=var_questionGeneratorAutoIncrement, font="Consolas 10").place(x = 930, y = 90)

var_questionGeneratorAppendFile = IntVar()
chk_questionGeneratorAppendFile = Checkbutton(root, text=str_questionGeneratorAppendOutput, variable=var_questionGeneratorAppendFile, font="Consolas 10").place(x = 10, y = 120)
var_questionGeneratorFilename = StringVar()
var_questionGeneratorFilename.set("output.xml")
ent_questionGeneratorFilename = Entry(root, width=20, textvariable=var_questionGeneratorFilename, font="Consolas 10").place(x = 255, y = 120)

var_questionGeneratorReplaceTitle = IntVar()
chk_questionGeneratorReplaceTitle = Checkbutton(root, text=str_questionGeneratorReplaceTitle, variable=var_questionGeneratorReplaceTitle, font="Consolas 10").place(x = 415, y = 120)
var_questionGeneratorTitleReplacement = StringVar()
var_questionGeneratorTitleReplacement.set("")
ent_questionGeneratorTitleReplacement = Entry(root, width=48, textvariable=var_questionGeneratorTitleReplacement, font="Consolas 10").place(x = 655, y = 120)
btn_questionGeneratorTitleReplacementClear = Button(root, text=str_elementGeneratorBtnClear, command=lambda: var_questionGeneratorTitleReplacement.set(""), font="Consolas 10").place(x = 1000, y = 117)

#    # Row/col/choice generator.
lbl_elementGeneratorTitle = Label(text=str_elementGeneratorTitle, justify=LEFT, font="Consolas 10").place(x = 10, y = 420)
lbl_elementGeneratorPrompt = Label(text=str_elementGeneratorPrompt, justify=LEFT, font="Consolas 10").place(x = 10, y = 440)
var_elementGeneratorValue = StringVar(root)
var_elementGeneratorValue.set(lst_elementGeneratorOptions[0])
#opt_elementGeneratorOptionSelector = apply(OptionMenu, (root, var_elementGeneratorValue) + tuple(lst_elementGeneratorOptions)).place(x = 180, y = 430)
opt_elementGeneratorOptionSelector = OptionMenu(root, var_elementGeneratorValue, *lst_elementGeneratorOptions).place(x = 180, y = 430)
#opt_elementGeneratorOptionSelector.config(font=('Consolas',(10)))
btn_elementGeneratorBtnGenerate = Button(root, text=str_elementGeneratorBtnGenerate, command=lambda: elementGenerate(txt_elementGeneratorTextInput, txt_elementGeneratorTextOutput), font="Consolas 10").place(x = 10, y = 460)
txt_elementGeneratorTextInput = Text(root, height=16, width=58)
txt_elementGeneratorTextInput.place(x = 10, y = 550)
txt_elementGeneratorTextOutput = Text(root, height=16, width=58)
txt_elementGeneratorTextOutput.place(x = 510, y = 550)
btn_elementGeneratorBtnGenerateAndCopy = Button(root, text=str_elementGeneratorBtnGenerateAndCopy, command=lambda: elementGenerateAndCopy(txt_elementGeneratorTextInput, txt_elementGeneratorTextOutput), font="Consolas 10").place(x = 80, y = 460)
btn_elementGeneratorBtnAppend = Button(root, text=str_elementGeneratorBtnAppend, command=lambda: elementGenerate(txt_elementGeneratorTextInput, txt_elementGeneratorTextOutput, True), font="Consolas 10").place(x = 305, y = 460)

btn_elementGeneratorBtnClear = Button(root, text=str_elementGeneratorBtnClear, command=lambda: elementClear(txt_elementGeneratorTextInput), font="Consolas 10").place(x = 430, y = 520)
btn_elementGeneratorResetDefaults = Button(root, text=str_elementGeneratorBtnDefault, command=lambda: elementResetDefaults(txt_elementGeneratorTextInput), font="Consolas 10").place(x = 315, y = 520)
lbl_elementGeneratorInput = Label(text=str_elementGeneratorInput, justify=LEFT, font="Consolas 10").place(x = 10, y = 527)
lbl_elementGeneratorInputDelimeter = Label(text=str_elementGeneratorDelimiter, justify=LEFT, font="Consolas 10").place(x = 80, y = 527)
var_elementGeneratorDelimeterValue = StringVar(root)
var_elementGeneratorDelimeterValue.set(lst_elementGeneratorDelimiterOptions[0])
#opt_elementGeneratorDelimeterOptionSelector = apply(OptionMenu, (root, var_elementGeneratorDelimeterValue) + tuple(lst_elementGeneratorDelimiterOptions)).place(x = 160, y = 517)
opt_elementGeneratorDelimeterOptionSelector = OptionMenu(root, var_elementGeneratorDelimeterValue, *lst_elementGeneratorDelimiterOptions).place(x = 160, y = 517)
#opt_elementGeneratorDelimeterOptionSelector.config(font=('Consolas',(10)))

lbl_elementGeneratorOutput = Label(text=str_elementGeneratorOutput, justify=LEFT, font="Consolas 10").place(x = 510, y = 527)
btn_elementGeneratorBtnOutputClear = Button(root, text=str_elementGeneratorBtnClear, command=lambda: elementClear(txt_elementGeneratorTextOutput), font="Consolas 10").place(x = 565, y = 521)
var_elementGeneratorCopyOutputToQuestionGenerator = IntVar()
chk_elementGeneratorCopyOutputToQuestionGenerator = Checkbutton(root, text=str_elementGeneratorCopyOutputToQuestionGenerator, variable=var_elementGeneratorCopyOutputToQuestionGenerator, font="Consolas 10").place(x = 635, y = 525)

postAppendRightShift = 55

lbl_elementGeneratorStartingIndex = Label(text=str_elementGeneratorStartingIndex , justify=LEFT, font="Consolas 10").place(x = 310 + postAppendRightShift, y = 462)
var_elementGeneratorStartingIndex = StringVar()
var_elementGeneratorStartingIndex.set("1")
ent_elementGeneratorStartingIndex = Entry(root, width=4, textvariable=var_elementGeneratorStartingIndex, font="Consolas 10").place(x = 423 + postAppendRightShift, y = 462)
var_elementGeneratorIncludeValues = IntVar()
var_elementGeneratorIncludeValues.set("1")
chk_elementGeneratorIncludeValues = Checkbutton(root, text=str_elementGeneratorIncludeValues, variable=var_elementGeneratorIncludeValues, font="Consolas 10").place(x = 463 + postAppendRightShift, y = 460)
var_elementGeneratorRemoveBrackets = IntVar()
var_elementGeneratorRemoveBrackets.set("1")
chk_elementGeneratorRemoveBrackets = Checkbutton(root, text=str_elementGeneratorRemoveBrackets, variable=var_elementGeneratorRemoveBrackets, font="Consolas 10").place(x = 753 + postAppendRightShift, y = 460)
var_elementGeneratorReverseOrder = IntVar()
chk_elementGeneratorReverseOrder = Checkbutton(root, text=str_elementGeneratorReverseOrder, variable=var_elementGeneratorReverseOrder, font="Consolas 10").place(x = 593 + postAppendRightShift, y = 460)
var_elementGeneratorDetectOE = IntVar()
var_elementGeneratorDetectOE.set("1")
chk_elementGeneratorDetectOE = Checkbutton(root, text=str_elementGeneratorDetectOE, variable=var_elementGeneratorDetectOE, font="Consolas 10").place(x = 10, y = 490)
var_elementGeneratorDetectEXC = IntVar()
var_elementGeneratorDetectEXC.set("1")
chk_elementGeneratorDetectEXC = Checkbutton(root, text=str_elementGeneratorDetectEXC, variable=var_elementGeneratorDetectEXC, font="Consolas 10").place(x = 145, y = 490)
var_elementGeneratorAnchor = IntVar()
chk_elementGeneratorAnchor = Checkbutton(root, text=str_elementGeneratorAnchor, variable=var_elementGeneratorAnchor, font="Consolas 10").place(x = 285, y = 490)
var_elementGeneratorReplaceOpenEndAndExclusiveIndexes = IntVar()
chk_elementGeneratorReplaceOpenEndAndExclusiveIndexes = Checkbutton(root, text=str_elementGeneratorReplaceOpenEndAndExclusiveIndexes, variable=var_elementGeneratorReplaceOpenEndAndExclusiveIndexes, font="Consolas 10").place(x = 465, y = 490)
var_elementGeneratorReplaceOpenEndAndExclusiveIndexes.set("1")

root.mainloop()