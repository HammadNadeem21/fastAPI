from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4


app = FastAPI()


Data = []

class AddStudent (BaseModel):
    name : str
    email: str
    age: int
    grade: str


# Create
@app.post('/addStudents')
def AddStudents(student: AddStudent):
    
    id = str(uuid4())
    # id = len(Data) + 1

    student = {
        "Id": id,
        "Name": student.name,
        "Email": student.email,
        "Age": student.age,
        "Grade": student.grade
    }

    Data.append(student)

    return {
        "message":"Student Added",
        "Student": student
    }


# Read
@app.get('/getAllStudents')
def getAllStudents():
    return Data


@app.get('/getStudentById/{id}')
def getStudentById(id:str):
    for std in Data:
        if std['Id'] == id:
            return std
        
    return {
        "message": "User not found"
    }


# Update
@app.put('/updateStudent/{student_id}')
def updateStudent(student_id:str, student:AddStudent):
    for std in Data:
        if std['Id'] == student_id:
            std['Name'] = student.name
            std['Email'] = student.email
            std['Age'] = student.age
            std['Grade'] = student.grade
            return{
                "message": "student updated successfuly",
                "updatedStudent": std
            }
        
    return {"message": "student not found"}



# Delete
@app.delete('/deleteStudent/{id}')
def deleteStudent(id:str):
    for std in Data:
        if std['Id'] == id:
            Data.remove(std)
            return {
                "message": "student deleted successfuly",
                "deletedStudent": std
            }
        
    return {"message": "student not found"}