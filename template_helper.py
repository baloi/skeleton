from pony_model import *


def therapist_residents_to_html(therapist):
  therapist_id = therapist.id

  counter = 1 
  even_or_odd = ""
  retVal = ''

  residents = therapist.residents

  for resident in residents:
  
    if counter % 2 == 0:
      even_or_odd = 'even'
    else:
      even_or_odd = 'odd'


    retVal = retVal + "      <tr class='%s'>" % even_or_odd
    retVal = retVal + "        <td>"
    retVal = retVal + resident.lastname
    retVal = retVal + ", " + resident.firstname
    retVal = retVal + "        </td>"
    retVal = retVal + "      </tr>"
    counter = counter + 1

  return retVal


@db_session
def therapist_to_html(therapist):
  retVal = ''

  retVal = retVal + "<tr><td align='left' bgcolor='8585AD'>"
  retVal = retVal + "<h2>"
  retVal = retVal + therapist.lastname
  retVal = retVal + "</h2>"
  retVal = retVal + "</td></tr>"

  retVal = retVal + "<tr><td>"

  retVal = retVal + "  <table id='residents'>"
  retVal = retVal + "    <tbody>"

  retVal = retVal + therapist_residents_to_html(therapist) 

  retVal = retVal + "    </tbody>"
  retVal = retVal + "  </table>"

  retVal = retVal + "</td></tr>"
  
  return retVal

@db_session
def resident_by_therapist_to_html():
  

  retVal = "<html>"
  retVal = retVal + "<head>"
  retVal = retVal + "  <title>tables</title>"
  retVal = retVal + "  <style type='text/css'>"
  retVal = retVal + "        #residents tbody tr.even td {"
  retVal = retVal + "          background-color: #eee;"
  retVal = retVal + "        }"
  retVal = retVal + "        #residents tbody tr.odd  td {"
  retVal = retVal + "          background-color: #fff;"
  retVal = retVal + "        }"
  retVal = retVal + "  </style>"
  retVal = retVal + "</head>"
  retVal = retVal + "<body>"

  retVal = retVal + "<table id='therapists' border='1'>"

  # print PT's first
  for pt in select(t for t in Therapist if t.discipline == 'PT'):
    retVal = retVal + therapist_to_html(pt)
  
  # now for OT's
  for ot in select(t for t in Therapist if t.discipline == 'OT'):
    retVal = retVal + therapist_to_html(ot)
 
  retVal = retVal + "</table>"
  retVal = retVal + "</body>"
  retVal = retVal + "</html>"

  return retVal
