#!/usr/local/bin/python3

import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

hostname = 'md-8.webhostbox.net'
portnum = 465

server = smtplib.SMTP_SSL(hostname, portnum)
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

