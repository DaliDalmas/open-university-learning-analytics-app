from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Assessments(Base):
    __tablename__ = 'assessments'

    index = Column(String, primary_key=True)
    code_module = Column(String)
    code_presentation = Column(String)
    id_assessment = Column(String)
    assessment_type = Column(String)
    date = Column(Integer)
    weight = Column(Float)


class StudentAssessment(Base):
    __tablename__ = 'student_assessment'

    index = Column(String, primary_key=True)
    id_assessment = Column(String)
    id_student = Column(String)
    date_submitted = Column(Integer)
    is_banked = Column(Boolean)
    score = Column(Float)


class Courses(Base):
    __tablename__ = 'courses'

    index = Column(String, primary_key=True)
    code_module = Column(String)
    code_presentation = Column(String)
    module_presentation_length = Column(String)


class StudentInfo(Base):
    __tablename__ = 'student_info'

    index = Column(String, primary_key=True)
    code_module = Column(String)
    code_presentation = Column(String)
    id_student = Column(String)
    gender = Column(String)
    region = Column(String)
    highest_education = Column(String)
    imd_band = Column(String)
    age_band = Column(String)
    num_of_prev_attempts = Column(Integer)
    studied_credits = Column(Float)
    disability = Column(String)
    final_result = Column(String)


class StudentRegistration(Base):
    __tablename__ = 'student_registration'

    index = Column(String, primary_key=True)
    code_module = Column(String)
    code_presentation = Column(String)
    id_student = Column(String)
    date_registration = Column(Integer)
    date_unregistration = Column(Float)


class StudentVle(Base):
    __tablename__ = 'student_vle'

    index = Column(String, primary_key=True)
    code_module = Column(String)
    code_presentation = Column(String)
    id_student = Column(String)
    date = Column(Integer)
    sum_click = Column(Float)


class Vle(Base):
    __tablename__ = 'vle'

    index = Column(String, primary_key=True)
    id_site = Column(String)
    code_module = Column(String)
    code_presentation = Column(String)
    activity_type = Column(String)
    week_from = Column(Float)
    week_to = Column(Float)
