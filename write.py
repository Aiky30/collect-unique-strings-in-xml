import xml.etree.ElementTree as ET
import xlrd

seed = "[PATH_TO_FILE][FILENAME].xls"
sourceFile = "[PATH_TO_FILE][FILENAME].xml"; 
outputFile = "[PATH_TO_FILE][FILENAME].xml";

tree = ET.parse(sourceFile)

def findTextInXML(xl_sheet, num_cells, curr_row) :
	
	row = xl_sheet.row(curr_row)
	
	en_cell_value = xl_sheet.cell_value(curr_row, 0)
	fr_cell_value = xl_sheet.cell_value(curr_row, 1)
	
	for tag in tree.iter():
		#print tag
		if en_cell_value == tag.text:
			print fr_cell_value, tag.text
			tag.text = fr_cell_value

def readXLS():
	print "Reading XLS file"
	sourceData = xlrd.open_workbook(seed)
	
	sheet_names = sourceData.sheet_names()
	xl_sheet = sourceData.sheet_by_name(sheet_names[0])
	
	#rows = xl_sheet.row(0)  # 1st row
	
	num_rows = xl_sheet.nrows - 1
	num_cells = xl_sheet.ncols - 1
	
	curr_row = -1
	while curr_row < num_rows:
		curr_row += 1
		
		findTextInXML(xl_sheet, num_cells, curr_row)

		"""
			curr_cell = -1
		while curr_cell < num_cells:
			curr_cell += 1
			# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
			#cell_type = xl_sheet.cell_type(curr_row, curr_cell)
			cell_value = xl_sheet.cell_value(curr_row, curr_cell)
			
			print cell_value
		 Send the row only at this point, you need to read the first column and then go about either mapping the data or replacing it, the second column is for the replace
		"""
	tree.write(outputFile)
	
def main():
	readXLS()
	
main()
