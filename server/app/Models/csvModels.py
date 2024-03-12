from database import db
class CSVData(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name =  db.Column(db.String(10000), nullable = True)
    domain =  db.Column(db.String(10000), nullable = True)
    year_founded =  db.Column(db.String(10000), nullable = True)
    industry =  db.Column(db.String(10000), nullable = True)
    size_range =  db.Column(db.String(10000), nullable = True)
    locality=  db.Column(db.String(10000), nullable = True)
    country =  db.Column(db.String(10000), nullable = True)
    linkedin_url =  db.Column(db.String(10000), nullable = True)
    current_employee_estimate=  db.Column(db.String(10000), nullable = True)
    total_employee_estimate=  db.Column(db.String(10000), nullable = True)