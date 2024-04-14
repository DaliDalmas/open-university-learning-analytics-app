from sqlalchemy import types
from copy_to_db import CopyToDb

'''
Explanation of this piece of code from chatgpt
----------------------------------------------
This code is for transferring data from various CSV files into a database. Here's a breakdown:

It starts by defining the structure of the data that will be inserted into the database tables. 
This structure includes the names of the columns and the types of data they contain (like text, numbers, etc.).

Then, it creates instances of a class called CopyToDb for each set of data to be transferred. 
These instances are created with parameters specifying the location of the CSV file containing the data, 
the data structure (defined earlier), and the name of the database table where the data will be stored.

After creating these instances, it calls a method called write_data() on each of them. 
This method reads the data from the CSV file and inserts it into the corresponding database table.

Finally, the code checks if it's being run directly (as opposed to being imported as a module) and if 
so, it calls the main() function to execute the data transfer process.

In simpler terms, it's like setting up different folders (database tables) and copying information 
(data from CSV files) into each folder according to a predefined plan (data structure). The code ensures
 that this copying process is done automatically and efficiently.
'''

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