from email.mime.text import MIMEText

html = """
<h1>Weekly Mutual Fund Summary</h1>

<p>SIP inflows increased this week.</p>
"""

msg = MIMEText(
    html,
    "html"
)

print(
    "HTML Email Report Created"
)