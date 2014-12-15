from sqlalchemy import Boolean, Column
from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import synonym
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property

Base = declarative_base()

# start Therapist class
class Therapist(Base):
    """A therapist. """
    __tablename__ = 'therapist'

    id = Column(Integer, primary_key=True)
    lastname = Column('lastname', String(200))
    firstname = Column('firstname', String(200))
    designation = Column('designation', String(30))
    discipline = Column('discipline', String(30))
    # should have a type attribute to enable single table inheritance.
    type = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity':'therapist',
        'polymorphic_on':type
    }

    #@hybrid_property
    def is_pt(self):
        if self.discipline == 'PT':
            return True
        else:
            return False

    def is_ot(self):
        if self.discipline == 'OT':
            return True
        else:
            return False

# end Therapist class


# start PhysicalTherapist class
class PhysicalTherapist(Therapist):
    pt_license_number = Column('pt_license_number', String(50))
    __mapper_args__ = {
            'polymorphic_identity': 'physical_therapist'
    }
# end PhysicalTherapist class

# start OccupationalTherapist class
class OccupationalTherapist(Therapist):
    pt_license_number = Column('ot_license_number', String(50))
    __mapper_args__ = {
            'polymorphic_identity': 'occupational_therapist'
    }
# end OccupationalTherapist class

# start Resident class

class Resident(Base):
    """A Resident class"""
    __tablename__='resident'
    id = Column(Integer, primary_key=True)
    lastname = Column(String(50))
    firstname = Column(String(50))
    active = Column(Boolean, default=True)

# end Resident class


# start get_session() method

def get_session(create_tables=False):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite://', echo=True)

    # create session and create database tables
    if create_tables:
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# end get_session() method
