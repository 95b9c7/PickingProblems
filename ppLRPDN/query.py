#!/c/users/atays/vscode/hello_django/djangoenv/Scripts/python
import pyodbc
import pandas as pd

try:
    connection = pyodbc.connect('DSN=AS400-PRODUCTION;'
                                'UID=inqmxc;'
                                'PWD=inqmxc123;'
                                'Connection Timeout=30;'
                                )
    print("Connection Successful")
    cursor = connection.cursor()
    sql_query = """
                SELECT TSCO, TSCODE, TSPN, TSREFN, TSTQTY, TSLOCF, USRPRF, TSDATE, TSTIME, TSRFLG
                FROM B20E386T.KBM400MFG.FKITSAVE FKITSAVE
                WHERE TSREFN = '0691150'
                """
    cursor.execute(sql_query)
    
    columns = [column[0] for column in cursor.description]
    print(columns)
    data = cursor.fetchall()
    rows = cursor.rowcount
    print(rows)
    # Print the first few rows of data to see its structure
    #print("First few rows of data:", data[:5])
    df = pd.DataFrame(data[:5])

    # Display the DataFrame
    print(df)
    cursor.close()
    connection.close()
except pyodbc.Error as e:
    print("Connection Error:", e)
