def hashtime(e, s="Error"):
    try:import smtplib, email;from email.mime.text import MIMEText;
    except Exception, e:pass;
    try:
        e_mail = #your email goes here
        pass_word = #your password goes here
        
        msg = MIMEText(e, "html")
        msg['From'] = e_mail
        msg['To'] = e_mail
        msg['Subject'] = s
        msg['Content-Type'] = "text/html; charset=UTF-8"
        
        #uncomment if your email server's use ssl
        #s = smtplib.SMTP_SSL("smtp.gmail.com", 465) #you will need to find your email smtp settings this is gmail's
        
        #uncomment if your email server's user tls 
        #s = smtpblib.SMTP("smtp.gmail.com", 587) #you will need to find your email smtp settings this is gmail's
        #s.starttls()
        
        s.login(e_mail, pass_word)
        s.sendmail(e_mail, [e_mail], msg.as_string())
        s.quit()
    except Exception, e:pass