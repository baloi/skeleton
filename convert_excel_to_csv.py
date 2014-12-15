import xlrd
import os
import optparse
import csv

class FileName:

  @classmethod
  def check_file_access(self, filename):
    if not os.path.isfile(filename):
      print '[-] ' + filename + ' does not exist.'
      exit(0)
    if not os.access(filename, os.R_OK):
      print '[-] ' + filename + ' access denied.'
      exit(0)
    return filename

  @classmethod 
  def to_csv(self, filename):
    # split filename by '.' 
    #print ". is indexed at "
    str_split = filename.split('.')

    csv_filename = str_split[0] + '.csv'
    #print 'csv filename = %s ' % csv_filename
    return csv_filename

  @classmethod
  def is_not_excel(self, filename):
    retVal = True

    if filename == None:
      return retVal
 
    str_len = len(filename)
    if str_len <= 4:
      return retVal

    start_index = str_len - 4

    #print "string length %d " % str_len

    file_extension = filename[start_index:str_len]

    #print file_extension
    if file_extension == '.xls':
      retVal = False

    return retVal

def csv_from_excel(excel_file):

  csv_filename = FileName.to_csv(excel_file)
  

  #wb = xlrd.open_workbook('therapy_sched.xls')
  wb = xlrd.open_workbook(excel_file)

  sh = wb.sheet_by_name('Sheet1')

 
  #your_csv_file = open('therapy_sched_csv.csv', 'wb')
  your_csv_file = open(csv_filename, 'wb')

  ##wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

  wr = csv.writer(your_csv_file,quoting=csv.QUOTE_ALL)

  for rownum in xrange(sh.nrows):
    wr.writerow(sh.row_values(rownum))

  your_csv_file.close()

if __name__ == '__main__':
  parser = optparse.OptionParser('usage %prog -f' + ' <excel_file.xls>')
  parser.add_option('-f', dest='excel_file', type='string', help='specify excel file')

  (options, args) = parser.parse_args()

  excel_file = options.excel_file

  #if (excel_file == None) | (is_not_excel(excel_file)):
  if FileName.is_not_excel(excel_file):
    print parser.usage
    exit(0)

  #print "File %s is excel" % excel_file
  
  FileName.check_file_access(excel_file)

  csv_from_excel(excel_file)
