# # import numpy as np 
# # import pandas as pd
# # import psycopg2

# # conn= psycopg2.connect(
# #     host='localhost',
# #     database='payroll',
# #     user='postgres',
# #     password='musk@n2003'
# # )
# # cur=conn.cursor()
# # main="insert into employee (id,name,mobile_number,blood_group) values(%s,%s,%s,%s)"
# # val=[(1,'khushi jain',6264217404,'B+'),
# #     (2,'atharv jain',6268451652,'AB+')]
# # cur.executemany(main,val)
# # cur.execute("SELECT * from employee")
# # result=.fetchall()cur
# # print(result)

# # conn.commit()
# # cur.close()
# # conn.close()






# import numpy as np 
# import pandas as pd
# import psycopg2

# conn= psycopg2.connect(
#     host='localhost',
#     database='company',
#     user='postgres',
#     password='musk@n2003'
# )
# rf=pd.read_csv(r'C:\Users\ASUS\Downloads\account_add_account (1).csv')
# df=pd.DataFrame(rf)
# print(df)
# table_name = 'Company_data'
# df2=df.iloc[3]
# elements = df2.tolist()
# # print(type(elements))
# loc = list(df.columns)
# columns=[]
# for i in range(len(elements)):
#     k=(loc[i],type(elements[i]))
#     columns.append(k)
# print(columns)   
    
# create_table_query = f"CREATE TABLE {table_name} ("
# for column in columns:
#     create_table_query += f"{column[0]} {column[1]}, "
# create_table_query = create_table_query.rstrip(', ') + ")"

# cur = conn.cursor()
# cur.execute(create_table_query)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()



# import numpy as np 
# import pandas as pd
# import psycopg2
# import base64

# conn= psycopg2.connect(
#     host='localhost',
#     database='add_account',
#     user='postgres',
#     password='musk@n2003'
# )
# rf=pd.read_csv(r'C:\Users\ASUS\Downloads\account_add_account (1).csv')
# df=pd.DataFrame(rf)
# print(df)
# cur=conn.cursor()
# cur.execute("truncate account cascade")
# with open(pdf_path, 'rb') as f:
#         pdf_data = f.read()


# main="insert into account (acc_no,ifsc,current_bal,current_due,image) values(%s,%s,%s,%s,%s)"
# data=[] 
# for index, row in df.iterrows():
#     acc_no = row['acc_no']
#     ifsc = row['ifsc']
#     current_bal = row['current_bal']
#     current_due = row['current_due']
#     pdf_path = row['pdf_path']

#     with open(col6, 'rb') as f:
#         pdf_data = f.read()


#     pdf_data_encoded = base64.b64encode(pdf_data)

# print(data)
# x1 = cur.executemany(main,data)
# # print(x1)
# conn.commit()
# cur.execute("SELECT * from account")
# result=cur.fetchall()
# print(result)

import numpy as np
import pandas as pd
import psycopg2
import base64
import pdf

conn = psycopg2.connect(
    host='localhost',
    database='add_account',
    user='postgres',
    password='musk@n2003'
)

cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS account (
        acc_no VARCHAR(20),
        ifsc VARCHAR(20),
        current_bal FLOAT,
        current_due FLOAT,
        pdf_data TEXT
    )
''')
cur.execute("TRUNCATE account CASCADE")

df = pd.read_csv(r'C:\Users\ASUS\Downloads\account_add_account (1).csv')


for _, row in df.iterrows():
    acc_no = row['acc_no']
    ifsc = row['ifsc']
    current_bal = row['current_bal']
    current_due = row['current_due']
    pdf_path = row['pdf_path']

    with open(pdf_path, 'rb') as f:
        pdf_data = f.read()

    cur.execute(
        "INSERT INTO account (acc_no, ifsc, current_bal, current_due, pdf_data) VALUES (%s, %s, %s, %s, %s)",
        (acc_no, ifsc, current_bal, current_due, pdf_data)
    )


conn.commit()

cur.close()
conn.close()
# cur.execute("SELECT * FROM account")
# result = cur.fetchall()
# print(result)



# import pandas as pd
# import psycopg2

# conn = psycopg2.connect(
#     host='localhost',
#     database='add_account',
#     user='postgres',
#     password='musk@n2003'
# )

# df = pd.read_csv(r'C:\Users\ASUS\Downloads\account_add_account (1).csv')
# print(df)

# cur = conn.cursor()
# cur.execute("truncate account cascade")


# main = "INSERT INTO account (acc_no, ifsc, current_bal, current_due, image_link) VALUES (%s, %s, %s, %s, %s)"
# data = df[['acc_no', 'ifsc', 'current_bal', 'current_due', 'image_link']].values.tolist()

# cur.executemany(main, data)
# conn.commit()

# cur.execute("SELECT * FROM account")
# result = cur.fetchall()
# print(result)

