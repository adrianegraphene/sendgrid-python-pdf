import pandas as pd
import os

investor_emails = pd.ExcelFile("investors.xlsx", engine='openpyxl') #GET EXISTING EMAILS
df_checker = investor_emails.parse("Sheet1")
API_URL = "http://localhost:8088/emailpayments/createInvestorWithoutUser" #local host

i = 0
for index, x in df_checker.iterrows():
    first_name = df_checker['Investor'][i].split(" ")[:1][0]
    email = df_checker['Email'][i]
    link = df_checker['Link'][i]
    print("i=%s. Name=%s. Email=%s. Link=%s" % (i, first_name, email, link))

    string = "curl -X POST \"" + API_URL + "\" -H \"accept: application/json\" -H \"Content-Type: application/json\" -d \"{\\\"emailAddress\\\":\\\"" \
                       + email + "\\\", \\\"name\\\":\\\"" + first_name + "\\\"}\" "
    os.system(string)

    i = i + 1
