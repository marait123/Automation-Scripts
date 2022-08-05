# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='mohammedibrahimgaballah@gmail.com',
    to_emails='mohammed.musa99@eng-st.cu.edu.eg',
    subject='testing the mainling service',
    html_content="""
    <h1>hi mohammed</h1>
    <strong>hi marait very happy to see you </strong>
    <h3> let's do it again </h3>
    """)
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)