import pandas as pd
import csv
from database import db
from Models.csvModels import CSVData
class FilesServices:
    def __init__(self) -> None:
        pass
    def saveToDb(self,filename):
        try:
            df = pd.read_csv(filename)
            df = df.dropna()
            print(df.columns)
            if not db.engine.has_table(CSVData):
                df.head(0).to_sql(CSVData,con=db.engine,if_exists='replace',index=False  )
            df.to_sql(CSVData, db.engine, if_exists='append', index=False)
            print("Sucess")
        except BaseException as err:
            msg = f"Exception occured in saveToDb. {err}"
            print(msg)
            raise err
    def insert_data_from_csv(self,filename):
        try:
            with open(filename, 'r',encoding="utf8") as csvfile:
                csvreader = csv.reader(csvfile)
                couter = 1
                invalidentried = 0
                next(csvreader)  # Skip header if it exists
                for row in csvreader:
                    if len(row) ==10:
                    # Assuming your CSV columns match the model attributes
                        data = CSVData(
                            name=row[0],
                            domain=row[1],
                            year_founded = row[2],
                            industry = row[3],
                            size_range = row[4].split('+')[0],
                            locality = row[5],
                            country = row[6],
                            linkedin_url = row[7],
                            current_employee_estimate = row[8],
                            total_employee_estimate = row[9],
                            # Add more columns as needed
                        )
                        db.session.add(data)
                        db.session.commit()
                        print(f'\rCurrently saving record No: ({couter}).',end=' ',flush=True)
                        couter=couter+1
                    else:
                        msg = f"{invalidentried}.Invalid entry found."
                        print(msg)
                        continue
                return
        except BaseException as err:
            msg = f"Exception occured in insert_data_from_csv.{err}"
            print(msg)
            raise msg