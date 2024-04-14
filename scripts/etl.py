from sqlalchemy import types
from copy_to_db import CopyToDb

def main():
    # courses
    courses_dtype_schema = {
        "code_module": types.VARCHAR,
        "code_presentation": types.VARCHAR,
        "module_presentation_length": types.VARCHAR
    }
    coursesInstance = CopyToDb(
        'scripts/data/courses.csv',
        courses_dtype_schema,
        table_name='courses'
        )
    coursesInstance.write_data()

    # assessments
    assessments_dtype_schema = {
        "code_module": types.VARCHAR,
        "code_presentation": types.VARCHAR,
        "id_assessment": types.VARCHAR,
        "assessment_type": types.VARCHAR,
        "date": types.INTEGER,
        "weight": types.FLOAT
    }
    assessmentsInstance = CopyToDb(
        'scripts/data/assessments.csv',
        assessments_dtype_schema,
        table_name='assessments'
        )
    assessmentsInstance.write_data()

    # student assessment
    student_assessment_dtype_schema = {
        "id_assessment": types.VARCHAR,
        "id_student": types.VARCHAR,
        "date_submitted": types.INTEGER,
        "is_banked": types.BOOLEAN,
        "score": types.FLOAT

    }
    studentAssessmentInstance = CopyToDb(
        'scripts/data/studentAssessment.csv',
        student_assessment_dtype_schema,
        table_name='student_assessment'
    )
    studentAssessmentInstance.write_data()

    # student info
    student_info_dtype_schema = {
        "code_module": types.VARCHAR,
        "code_presentation": types.VARCHAR,
        "id_student": types.VARCHAR,
        "gender": types.VARCHAR,
        "region": types.VARCHAR,
        "highest_education": types.VARCHAR,
        "imd_band": types.VARCHAR,
        "age_band": types.VARCHAR,
        "num_of_prev_attempts": types.INTEGER,
        "studied_credits": types.FLOAT,
        "disability": types.VARCHAR,
        "final_result": types.VARCHAR
    }
    studentInfoInstance = CopyToDb(
        'scripts/data/studentInfo.csv',
        student_info_dtype_schema,
        table_name='student_info'
    )
    studentInfoInstance.write_data()

    # student registration
    student_registration_dtype_schema = {
        "code_module": types.VARCHAR,
        "code_presentation": types.VARCHAR,
        "id_student": types.VARCHAR,
        "date_registration": types.INTEGER,
        "date_unregistration": types.FLOAT

    }
    studentRegistrationInstance = CopyToDb(
        'scripts/data/studentRegistration.csv',
        student_registration_dtype_schema,
        table_name='student_registration'
    )
    studentRegistrationInstance.write_data()

    # student vle
    student_vle_dtype_schema = {
        "code_module": types.VARCHAR,
        "code_presentation": types.VARCHAR,
        "id_student": types.VARCHAR,
        "date": types.INTEGER,
        "sum_click": types.FLOAT
    }
    studentVleInstance = CopyToDb(
        'scripts/data/studentVle.csv',
        student_vle_dtype_schema,
        table_name='student_vle'
    )
    studentVleInstance.write_data()

    # vle
    vle_dtype_schema = {
        "id_site": types.VARCHAR,
        "code_module": types.VARCHAR,
        "code_presentation": types.VARCHAR,
        "activity_type": types.VARCHAR,
        "week_from": types.FLOAT,
        "week_to": types.FLOAT,
    }
    vleInstance = CopyToDb(
        'scripts/data/vle.csv',
        vle_dtype_schema,
        table_name='vle'
    )
    vleInstance.write_data()


if __name__=='__main__':
    main()