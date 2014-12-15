class TextReader:
  """
  Returns a list of entries from file 
  """
  @classmethod
  def extract_list_from_file(self, filename):
    f = open(filename, 'r')
    entries = []
  
    for line in f.readlines():
      #print "reading line %s " % line
      line = line.strip('\n')
      entries.append(line)

    return entries

class CSVReader:
  @classmethod
  def convert_csv_to_resident_list(self, filename):
    """
    Reads csv file to and writes it as a text file containing a list of resident
    data. Each line in the file will represent a resident.
    """
    resident_data = {}
    lines = []
    f = open(filename, 'r')
    
    line_num = 0

    # read csv line by line and strip uneeded headers
    for line in f.readlines():
      # read only starting 8th line
      line_num = line_num + 1
      if line_num >= 8: 
        lines.append(line) 
        #print "reading %s " % line

    # read through line by line of filtered data and "record" into a list of
    # residents
    parser = ResidentDataParser()

    # go through the list of residents and extract needed data
    residents = parser.parse_data(lines)
    
    #for r in residents:
    #  print r.lastname + ", " + r.firstname + ", " + r.primary_pt + ", " + r.primary_ot

    return residents


