import xml.etree.ElementTree as ET
import xlwt

sourceFile = "[PATH_TO_FILE][FILENAME].xml"; 
outputFile = "[PATH_TO_FILE][FILENAME].xls";

tree = ET.parse(sourceFile)
#root = tree.getroot()

uniqueMap = []

def isUnique(strItem):
	
	seenString = False;
	for item in uniqueMap:
		if strItem == item:
			#print "duplicate: "+item.encode('utf-8')
			seenString=True
	
	if seenString == False:
		uniqueMap.append(strItem);

def writeToTxtFile():
	print "Writing to TXT file"
	file = open(outputFile, "w")

	for item in uniqueMap:
		#print item.encode('utf-8')+'\n'
		file.write(item.encode('utf-8')+'\n')

	file.close()

def writeToXslFile():
	
	print "Writing to XLS file"
	
	langDoc = xlwt.Workbook()
	langSheet = langDoc.add_sheet('Language Translations')
	
	langSheet.write(0, 0, 'English')
	langSheet.write(0, 1, 'French')
	
	i=1
	for item in uniqueMap:
		#print item
		#langSheet.write(i, 0, i)
		langSheet.write(i, 0, item)
		i+=1

	langDoc.save(outputFile)

def main():

	for tag in tree.iter():
		if not len(tag) and tag.text != None:
			#print (tag.tag, tag.text)
			isUnique(tag.text)

	writeToXslFile()
	#writeToTxtFile()

main()
