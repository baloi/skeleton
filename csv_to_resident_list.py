from baloi.data_tools import *
from pony_model import *
import template_helper

@db_session
def add_primary_pt(resident, pt_complete_name):
  #print "add_primary_pt"
  if ResidentDataParser.has_entry(pt_complete_name):
    fullname = pt_complete_name.split(" ")
    firstname = fullname[0]
    #print 'PT firstname = %s' %firstname
    lastname = fullname[1]
    resident.primary_pt = Therapist.get(firstname=firstname)
  else:
    print resident.lastname + " has no PT "
  
  return resident

@db_session
def add_primary_ot(resident, ot_complete_name):
  #print "add_primary_pt"
  if ResidentDataParser.has_entry(ot_complete_name):
    fullname = ot_complete_name.split(" ")
    firstname = fullname[0]
    #print "OT = %s" % fullname
    #print 'OT firstname = %s' %firstname
    lastname = fullname[1]
    resident.primary_ot = Therapist.get(firstname=firstname)
  else:
    print resident.lastname + " has no OT "
  
  return resident
 
  
@db_session
def residents_data_to_db(resident_list):
  #print "saving resident data to db" 
  for r in resident_list:
    #display = r.lastname + ', ' + r.firstname + ", " + " "
    #display = display + r.primary_pt + " - " + r.primary_ot
    #print display
    resident = Resident(lastname=r.lastname, firstname=r.firstname, active=True)
    resident = add_primary_pt(resident, r.primary_pt)
    resident = add_primary_ot(resident, r.primary_ot)

def print_residents_from_list(resident_list):
  for r in resident_list:
    line = r.lastname + ", " + r.firstname + ", " + r.primary_pt + ", "
    line = line + r.primary_ot
    print line
 

def main():

  r_list = CSVReader.convert_csv_to_resident_list('therapy_sched.csv')

  #print_residents_from_list(r_list)

  therapists = TextReader.extract_list_from_file('therapists.txt') 

  ConsoleAppDBUtil.store_therapists(therapists)
  #list_therapists()

  residents_data_to_db(r_list) 

  show_residents_by_therapist()
  #print template_helper.resident_by_therapist_to_html()

if __name__ == "__main__":
  main()

