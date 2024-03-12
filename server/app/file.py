from flask import Blueprint,jsonify
from app import flask_app
from flask_login import current_user
from FilesServices.FilesServices import FilesServices
files_bp = Blueprint(
    'files', __name__, url_prefix='/api/files')

@files_bp.route('saveCsvToDb')
def saveCsvToDb():
    try:
        if current_user.is_authenticated:
            fileservice = FilesServices()
            smallCSV = r'C:/Users/patil/Downloads/SampleCSVFile_2kb.csv'
            largeCSV =  r'C:\Users\patil\Downloads\free-7-million-company-dataset\companies_sorted.csv'
        # fileservice.saveToDb(smallCSV)
            fileservice.insert_data_from_csv(largeCSV)
            
            return "Sucessfully saved CSV to DB"
        else:
            msg = f"You are not authorized to use the endpoint"
            return jsonify({'message':msg,'error':"UNAUTHORIZED"}),200
    except BaseException as err:
        msg  = f"Failed to save csv to db .{err}"
        print(msg)
        return msg