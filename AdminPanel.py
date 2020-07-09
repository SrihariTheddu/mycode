from getpass import getpass
import json
import sys
import os
from datetime import datetime

import logging
from logging import handlers

#-----------------------------------
class Admin:
    def __init__(self):
        
        '''
        func name   : Admin logging user constructor.....
        params      : instance metho
        process     : Admin processor
        '''
        #FILE URLS.......
        
        
        #---------------------------
        # CHECKING INTERNET CONN
        
        try:
            # checking internet conn
            import urllib.request as r
            with r.urlopen('http://google.com') as server:
                pass
        except:
            
            self.invalid.error('CHECK YOUR INTERNET CONNECTION')
            sys.exit()
        # CONNECTING TO ADMIN PAGE
        #------------------------   
        # Connecting to Admin Folder
        try:
            with open(self.auth_creds_url,'r') as admin:
                
                self.auth_creds = admin.read()
                
              
                # redirecting into json Format.............
                
                self.auth_creds = json.loads(self.auth_creds)
                
            # FRONT END CONNECTION
            #--------------------- 
            
            self.auth_admin = input(f'\033[1;37;9m {"USERNAME":20}: ')
            temp = 'PASSWORD'
            password = getpass(f'\033[1;37;9m {"PASSWORD":20}: ')
            
            #----------------------
            # BACKEND CONNECTION
            # Logging into DataBase
            # IF ADMIN LOGIN SUCCESS
            if password==self.auth_creds['auth_password'] and self.auth_admin==self.auth_creds['auth_admin']:
                self.auth_emailid = self.auth_creds['auth_emailid']
                
                self.auth_permissions=True
                self.report.info(f'SUCCESSFULLY LOGGED IN...')
                print(f'\033[4;34;9m ADMIN NAME : {self.auth_admin} \033[1;32;9m  ')
                # actions into logbook 
                self.record.warning(f'\nAdmininstration panel\nUSERNAME   : {self.auth_admin}\nLOGGED IN SUCCESSFULLY..')
                with open(self.cachepath_url,'w') as cache:
                    cache.write(str(datetime.today()))
            #ADMIN LOGIN FAILED
            else:
                self.auth_permissions = False
                
                self.invalid.error('\033[1;31;9m ADMINISTRATION : ADMIN LOGIN FAILED \n INVALID AUTHENTICATION OR INVALID PASSWORD.')
                sys.exit()
        # CREATING NEW ADMIN FOLDER
        except :
            self.report.info(f'\033[1;34;9m ADMINISTRATION PANEL :\nCREATING CREDIENTIALS')
            self.report.info('\033[1;35;9m CREDENTIALS ARE IN JSON FORMAT OR DICTIONARY FORMAT...')
            self.report.info('\033[1;36;9m This email is used in connections to send emails to your users in the database')
            # FRONTEND CONNECTIONS
            #Accessing email address
            self.auth_emailid = input(f'\033[2;37;6m{"MAIL ID":20}: \033[2;36;9m')
            #email_password
            self.auth_emailpassword = getpass(f'\033[1;38;6m{"MAIL PASSWORD":20}: \033[2;36;9m')
            self.auth_admin =input(f'\033[1;37;6m{"USERNAME":20}:\033[2;36;9m')
            self.VerifyPassword()
            # creating credentials
            self.MakeCredentials()
            #self.ConfigFolder()
            #self.ConfigFiles()
            self.ConfigCredentials()
            
            
            
            

            
                                    

            
                                    
    #-----------------------------
    #  WRITING CREDENTUALS INTO ADMINISTRATION PANEL......
    def MakeCredentials(self):
        '''
        func name  : loading credentials
        params     : email
                     mailpassword
                     username
                     password
                     project title
        process    : converts the data into json or dict Format
        '''
        self.auth_creds = f'"auth_admin":"{self.auth_admin}","auth_password":"{self.auth_password}","auth_emailid":"{self.auth_emailid}","auth_emailpassword":"{self.auth_emailpassword}","date of creation":"{str(datetime.today())}","storage_url":"{self.DBMS_DIR}"'
        self.auth_creds = '{'+self.auth_creds+'}'
        # LOGBOOK RECORD.....
        self.report.info('CREDENTIALS CREATED SUCCESSFULLY....')
        
        

                        



    #-----------------------------
    #  WRITING CREDENTUALS INTO ADMINISTRATION PANEL......
    def ConfigCredentials(self):
        '''
        func name  : loading credentials
        params     : email
                     mailpassword
                     username
                     password
                     project title
        process    : converts the data into json or dict Format
        '''
        with open(self.auth_creds_url,'w') as creds:
            creds.write(str(self.auth_creds))
            self.report.warning(f'CREDENTIALS ADDED SUCCESSFULLY.....')



    #------------------------------
    # PASSWORD VERIFICATION...
    def VerifyPassword(self):
        '''
        func name   : verifypassword
        params      : None
        process     : verifies password
        '''
        self.auth_password= getpass(f'\033[1;37;9m{"DATABASE PASSWORD":20}:')
        print(f'\033[1;34;9m Password must match.........')
        dummy_password=getpass(f'\033[1;37;9m{"RENTER PASSWORD":20}:')
        
        if self.auth_password==dummy_password:
            pass
        else:
            self.invalid.error('PASSWORD NOT VERIFIED....')
            self.VerifyPassword()




    def ConfigFiles(self):
        '''
        func name : makefolder
        params    : title of project
        process   : open files                           related to project
                    filenames:
                        logbook.txt
                        cache.txt
                        Admin.bin
        returns   : None
        '''
        filepath = [self.logbookpath_url,self.cachepath_url]
        
        for path in filepath:
            with open(path,'w') as openfile:
                openfile.write(path)
                self.report.info(f'ADMINISTRATION STATUS  : \n CONFIGURING FILES FOR DATABASE MANAGEMENT SYSTEM.....\n{path}')
                
                
    def ConfigFolder(self):
        try:
            os.mkdir(self.auth_title)
            self.report.info(f'ADMINISTRATION CONFIGURATION SET UP SUCCESSFULL')
            self.auth_admin_config_setup = True
            return False
        except:
            self.report.error('ADMINISTRATION CONFIGURATION HAS ALREADY SET UP \nCOULD NOT SET UP NO MORE 5000...')

                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      