
import logging as log
import os
from AdminPanel import Admin
import smtplib
from email.message import EmailMessage

class MainHandler(Admin):
    
    def __init__ (self):
        #self.auth_title = input('PROJECT NAME    :  ')
        self.auth_title ='ganesh'
        try:
            os.mkdir(self.auth_title)
        except:
            pass
        #---------------------------
        # FILE URLS...............
        
        '''loada the path of the files in the url format 
        accessable variables
        DBMS_DIR : DataBase directory path.......
        AUTH_DIR : Authentication directory path
        auth_creds_url  : credentils directory path.......
        logbookpath_url : 
        cachepath_url
        '''
            
        
        self.DBMS_DIR = '/storage/emulated/0/mydbms/'
        
        #self.AUTH_DIR = f'/storage/emulated/0/mydbms/{self.auth_title}'
        
        self.AUTH_DIR = os.path.join(os.getcwd(),self.auth_title)
        
        self.auth_creds_url =os.path.join(self.AUTH_DIR,'Authentication_Admin_Credentials.json')
        self.logbookpath_url= os.path.join(self.AUTH_DIR,'logbook.txt')
        self.cachepath_url = os.path.join(self.AUTH_DIR,'cache.txt')
        #---------------------------
        # Stream Handler.....
        self.report= log.getLogger('Report')
        self.report.setLevel(log.DEBUG)
        # Logbook Handler....
        self.record = log.getLogger('Record')
        self.record.setLevel(log.DEBUG)
        # cache handler
        self.cache= log.getLogger()
        self.cache.setLevel(log.DEBUG)
        
        
        
        #Binding all Handlers
        self.ConsoleHandler()
        self.FileHandler()
        self.CacheHandler()
        self.ErrorHandler()
        
        super().__init__()
        
    #   FILE HANDLER.......
    def FileHandler(self):
        self.FileHandler = log.FileHandler(filename=self.logbookpath_url)
        self.FileHandler.setLevel(log.DEBUG)
        self.FileFormatter = log.Formatter(f"#Timestamp :  %(asctime)s \n %(message)s\n--------------------------------------",datefmt='%d-%m-%Y  %H:%M')
        self.FileHandler.setFormatter(self.FileFormatter)
        self.record.addHandler(self.FileHandler)
        
        
        
        
       
    # CONSOLE HANDLER........
    def ConsoleHandler(self):
        self.consoleHandler = log.StreamHandler()
        self.consoleHandler.setLevel(log.DEBUG)
        self.consoleFormatter = log.Formatter(f"\033[1;32;9m #cmd : %(levelname)s-%(message)s  \033[1;32;9m" ,datefmt='%Y-%m-%d => %H:%M ')
        self.consoleHandler.setFormatter(self.consoleFormatter)
        
        self.report.addHandler(self.consoleHandler)
        
    # CACHE HANDLER......   
    def CacheHandler(self):
        self.cacheHandler = log.FileHandler(filename=self.cachepath_url)
        self.cacheHandler.setLevel(log.DEBUG)
        self.cacheFormatter = log.Formatter(f"%(message)s")
        self.cacheHandler.setFormatter(self.cacheFormatter)
        self.cache.addHandler(self.cacheHandler)
    
    #    DATABASEHANDLER
    def DatabaseHandler (self):
        self.databaseHandler = log.FileHandler(filename = self.database_path)
        self.databaseHandler.setLevel(log.WARNING)
        self.databaseHandlerFormatter= log.Formatter(f'%(message)s')
        self.databaseHandler.setFormatter(self.databaseHandlerFormatter)
        self.report.addHandler(self.databaseHandler)
    
    #   ERROR HANDLER.....
    def ErrorHandler (self):
    	self.invalid = log.getLogger('error')
    	self.invalid.setLevel(log.ERROR)
    	self.dismatch = log.StreamHandler()
    	self.dismatch.setLevel(log.ERROR)
    	self.errorFormatter = log.Formatter(f'\033[2;31;9m %(levelname)s-%(name)s- %(message)s \033[0;32;40m ')
    	self.dismatch.setFormatter(self.errorFormatter)
    	self.invalid.addHandler(self.dismatch)
        
        
        
        
      
    def context(self,modname,funcname,data,result):
        message = f'func name :{funcname}\n Inmod  : {modname}\ndata  : {data}\nresult :{result}'
        return message
        
    def CacheConfig(self,mkey,mvalue,msg):
        cachef={}
        for key,value in zip(mkey,mvalue):
            cachef[key]=value
        msg = msg+'\n'+'-'*35
        self.record.info(msg)
        return cachef


     
 
        
     
        
   


            
        
                               
    
         

      



    