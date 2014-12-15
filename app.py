from flask import Flask
from flask import render_template
#from csv_to_resident_list import *
#@@TODO: sqlalchemy implementation with datatools
from sqlalchemy_model import *

app = Flask(__name__)

@app.route('/')
@db_session
def caseload():
  r_list = CSVReader.convert_csv_to_resident_list(
            'therapy_sched.csv')

  #print_residents_from_list(r_list)

  therapists = TextReader.extract_list_from_file('therapists.txt') 

  ConsoleAppDBUtil.store_therapists(therapists)
  #list_therapists()

  residents_data_to_db(r_list) 

  #@@TODO: uncomment for production
  #show_residents_by_therapist()


  #therapist_caseload = resident_by_therapist_to_html()
  therapist_caseload = template_helper.resident_by_therapist_to_html()
  return render_template('index.html', therapist_caseload=therapist_caseload)

if __name__=='__main__':
  app.debug=True
  app.run()
