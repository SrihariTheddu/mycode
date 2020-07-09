import smtplib
from email.message import EmailMessage
import imghdr
from getpass import getpass
import json


class Connector:
    '''
    EXAMPLE OF CONNECTOR
    conn = Connector()
    conn.server()
    conn.connect(reciever_mail_address)
    conn.mailformat(subject,message,image,docs)
    conn.sendmail()
    
    '''
    def server(self):
        '''
        creates connector by using the Admin mail identity'''
        self.result = False
        self.mail = EmailMessage()
        self.mail['From']=self.auth_mailid
             
    
    #------------------------       
    def connect(self,clientmail):
        '''
        func name : connect
        param     : clientmailid
        process   : connects with clients mail
        returns   : True if connected
        False if not connected
        '''
        self.clientmail = clientmail
        self.mail['To'] = self.clientmail
        
            
        return True
                
     
    #------------------------------
    def mailformat(self,subject,message,image=None,docs=None):
        '''
        func name : mailformat
        params    : subject 
                    Message
                    Image object intilized with None
                    Document Object initilized with None
        processor : creates an structure an mail
        returns   : structed mail with content
        '''
        self.mail['Subject']=subject
        self.mail.set_content(message)
        try:
            with open(image,'rb') as f:
                img = f.read()
                imgname = f.name
                imgtype = imghdr.what(f.name)
                self.mail.add_attachment(img,maintype='image',subtype=imgtype,filename=imgname)
                
        except:
            pass
        return self.mail
        
        
    #----------------------------   
    def sendmail(self):
        '''
        func name  : sendmail
        params     : instance obj
        processor  : sends mail to client
        retutn     : None
        '''
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
                server.login(self.authmail,self.authpassword)
                server.send_message(self.mail)
                self.report.info(f'MAIL SENDED TO : {self.clientmail}')
                server.quit()
        except smtp.SMTPAuthenticationError:
            self.report.error('COLDNT SEND MAIL......')
            
            
    #------------------------       
    def sendmails(self,emails,subject,content,img=None,document=None):
        '''
        func name  : sendmails
        params     : key of mail row in DataBaseRow
        processor  : send mails to clients
        retutn     : None
        '''
        for emailid in db.DataBaseData[emails]:
            conn = Connector(emailid)
            conn.mailformat(subject=sub,message=content,image=img,docs=document)
            conn.sendmail()
            
        

            
             

    
        



            