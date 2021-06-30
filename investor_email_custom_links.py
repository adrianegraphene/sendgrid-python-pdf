import emailSendsSendGrid
import pdfLinkUpdater
import pandas as pd
from datetime import datetime

investor_emails = pd.ExcelFile("investors.xlsx", engine='openpyxl')  # Excel data import
df_checker = investor_emails.parse("Sheet1")

i = 0
for index, x in df_checker.iterrows():
    first_name = df_checker['Investor'][i].split(" ")[:1][0]
    email = df_checker['Email'][i]
    link = df_checker['Link'][i]
    text = df_checker['Text'][i]
    print("i=%s. Name=%s.  Email=%s. Link=%s Text=%s" % (i, first_name, email, link, text))

    print("creating custom PDF link....")    # This pdf will get its links replaced as according to pdfLinkUpdater.
    pdfLinkUpdater.update_pdf("old.pdf", link)

    print("sending email with custom PDF and text....")
    emailSendsSendGrid.send_variable_message_email_response(email, first_name, text)
    print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    i = i + 1