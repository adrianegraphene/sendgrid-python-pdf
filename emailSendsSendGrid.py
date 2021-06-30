import base64
import sendgrid
from sendgrid.helpers.mail import *
import os

SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
EMAIL = os.environ['EMAIL']
EMAIL_TWO = os.environ['EMAIL_TWO']
NAME = os.environ['NAME']


def send_variable_message_email_response(email, name, text):
    print("sending SendGrid email.....")
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    # from_email = Email(NAME + "<" + EMAIL + ">") # FOR REGULAR EMAIL RESPONSES
    from_email = Email(NAME + "<" + EMAIL_TWO + ">") # FOR PAID EMAIL RESPONSES
    to_email = To(email)
    subject = "Lower CAC through Telecom/Crypto - FynCom Pitch."
    content = Content("text/html", '<html>Hi ' + name +
      ',<br/><br/>' + text + '<br/><br/>'
      # ',<br/><br/>We want to demo our telco/crypto tech on you right now! Just answer this e-mail with anything and get paid.<br/><br/>'
      # 'Our platform allows companies to pay customers to pay attention to a phone call, e-mail or any other form of communication. '
      # 'This helps companies to lower their CAC.<br/><br/>'
      + 'Check out our pitch deck for a personalized example of our tech.<br/><br/>'
      'Best,<br/>' + NAME +'<br/><img src="https://www.fyncom.com/images/FynCom_Logo.png" width="94" height="86" alt="FynCom Logo"></html>')

    with open('FynCom-Pitch-Deck.pdf', 'rb') as f: # PDF attachment here
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()
    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('FynCom-Pitch-Deck.pdf'),
        FileType('application/pdf'),
        Disposition('attachment')
    )

    mail = Mail(from_email, to_email, subject, content)
    # mail.reply_to = ReplyTo(to_email.email, NAME) #Note, this sets the Reply To.... not what we want.
    mail.attachment = attachedFile

    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


#for sending followup emails in a thread - NOT WORKING YET
def send_variable_message_email_response_thread(email, name, text):
    print("sending THREADED SendGrid RESPONSE email.....")
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email(NAME + "<" + EMAIL + ">") # FOR REGULAR EMAIL RESPONSES
    # from_email = Email(NAME + "<" + EMAIL_TWO + ">") # FOR PAID EMAIL RESPONSES
    to_email = To(email)
    subject = "Re: Lower CAC through Telecom/Crypto - FynCom Pitch."
    content = Content("text/html", '<html>Hi 2nd test ' + name +
      ',<br/><br/>' + "This would hopefully look like the 2nd email in a thread. I don't think it does though." +
      ',<br/><br/>We want to demo our telco/crypto tech on you right now! Just answer this e-mail with anything and get paid.<br/><br/>'
      'Our platform allows companies to pay customers to pay attention to a phone call, e-mail or any other form of communication. '
      'This helps companies to lower their CAC.<br/><br/>'
      'Check out our pitch deck.<br/><br/>'
      'Best,<br/>' + NAME +'<br/><img src="https://www.fyncom.com/images/FynCom_Logo.png" width="94" height="86" alt="FynCom Logo"></html>')

    mail = Mail(from_email, to_email, subject, content)
    # NOTE, GMail "Show Original" does not show the variables unless you enclose them in angle brackets.
    #I tried the SendGrid Message ID and the Gmail "Message-ID" - neither works.
    # mail.add_header(Header("References", "<4i9C13cLTVeSwCZLvSLG3Q.filterdrecv-7bc4dfcfd6-8n99s-1-60D57ABD-25.0>"))
    # mail.add_header(Header("In-Reply-To", "<4i9C13cLTVeSwCZLvSLG3Q.filterdrecv-7bc4dfcfd6-8n99s-1-60D57ABD-25.0>"))

    #This is what the internet says we need...
    mail.add_header(Header("References", "<FbhJ5uJ1RBu5QVnsZRw2Zw@geopod-ismtpd-6-0>"))
    mail.add_header(Header("In-Reply-To", "<FbhJ5uJ1RBu5QVnsZRw2Zw@geopod-ismtpd-6-0"))
#########################    # mail.reply_to = ReplyTo(to_email.email, 'Adrian Garcia') #Note, this sets the Reply To.... not what we want.
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)