import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from Handlers import MainHandler
import pandas as pd
from Handlers import MainHandler
import sys
from Connector import Connector
import os
from AdminPanel import Admin
import threading
class DataBaseModel(MainHandler,Connector):
    
    def __init__(self,gsheet_title,credentials):
        '''
        Starting Point of the execution..
        Class     : DataBaseModel
        func name : DataBaseModel Constructor
        params    : Name of the DataBase Sheet...
        process   : executes the all the initial credentials ......
        return    : None
        '''
        self.title = gsheet_title
        super().__init__()
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        # Adding Credentials to perform Operations on DataBaseSheet or Google SpreadSheet
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        self.report.warning(f'@{self.auth_admin}  ADDING CREDENTIALS....')
        # authorising the client
        self.client = gspread.authorize(credentials)
        self.DataBaseSheet = self.client.open(self.title).sheet1
        self.report.info('COLLECTING DATA ....')
        self.DataBaseData = pd.DataFrame(self.DataBaseSheet.get_all_records())
        self.report.info(f'''\033[1;34;9m 
        Administration Block:
            Admin Name   : {self.auth_admin}
            project name : {self.title}
            Filepath     : {os.getcwd()}
       This process has undertaken under the google guidelines and privacy policy of an individual user
       This data is collected from your google cloud platform with the accessibity procedure
       This software is allowed to view ,overwrite and change the data from the google cloud account...
       google Account : {self.auth_emailid}
       -------------------------------
        ''')
        self.DataBase = self.DataBaseSheet.get_all_records()
        '''Rank attribute'''
        self.rank = len(self.DataBaseData.ID)
        self.attributes = None
        self.report.info(f'Records count :   {self.rank}')
        

        
        
     
    def verifyattribute(self,key):
        flag=False
        for attire in attribute:
            if attire==key:
                flag=True
        if flag:
            return True
        else:
            return False   
    
    # SETTING ATTRUBUTES.....    
    def setAttributes(self,attributes):
        '''
        Func        : setattributes
        parameters  : list
        method.     : sets attributes to the DataBase
        returns     : None
        '''
        newattributes=['ID',]
        i=0
        for i in range(len(attributes)):
            newattributes.append(attributes[i])
        self.DataBaseSheet.insert_row(newattributes,1)
        self.report.info(f'Attributes updated\nNew Attributes {newattributes} ')
        
        self.maincache(self.cache(['attributes'],[newattributes],f'@{self.auth_admin}  : SETTING ATTRIBUTES'))
      
    #------------------------------ 
    # FINDING CELL ....
    def findcell(self,keyperson,attribute):
        '''
        Func name : findcell
        params    : keyperson
                    attributate
        process   : Finds the index of row[keyperson] and column[attribute]
        return    : pair of row and column in format of list
        '''
        # FINDING ROW
        row=1
        for key in self.DataBaseData[self.key]:
            row+=1
            if key==keyperson:
                break
            
        # FINDING COLUMN
        
        col =1
        for attire in self.getAttributes():
            if attire == attribute:
                break
            col += 1
        return [row,col]
    #---------------------------
    '''
    func name   : getvalues
    params      : keyperson and attributes
    process     : searches the values of the given keyperson's attribute
    returns     : values in list datatype
    '''       
    def getvalues(self,keyperson,attributes):
        if type(attributes)==type([]):
            pass
        else:
            attributes = [attributes]
        values = []
        for attire in attributes:
            matrix = self.findcell(keyperson,attire)
            value = self.DataBaseSheet.cell(matrix[0],matrix[1]).value
            try:
                value = int(value)
            except:
                pass
            values.append(value)
        return values
    #---------------------------
    '''
    func name   : getvalue
    params      : keyperson and attribute
    process     : searches the value of the given keyperson's attribute
    returns     : value in str datatype
    '''    
    def getvalue(self,keyperson,attribute):
        matrix = self.findcell(keyperson,attribute)
        values = self.DataBaseSheet.cell(matrix[0],matrix[1]).value
        return values
            
    #-----------------------------
    # REPLACING THE CELL.....
    def replacecell(self,keyperson,attribute,value):
        '''
        func name  : replacecell
        params     : keyperson
                     attribute
                     value
        process    : This updates the value at row[keyperson] column[attribute]'''
        cell = self.findcell(keyperson,attribute)
        self.DataBaseSheet.update_cell(cell[0],cell[1],value)
        self.report.warning('Successfully Updated...')
        self.report.warning(f'{keyperson}[{attribute}] = {value}')
        self.record.warning(f'Updation :  {keyperson}[{attribute}] = {value}')
        self.attributes = None
             
          
    #-------------------------------
    def getAttributes(self):
        '''
        func name : getattributes
        method    : Instance
        params    : Instance object
        returns.  : All the attributes from the DatqBase
                   <list data type>
         creates  : self.attributes
         '''
        if self.attributes:
            return self.attributes
        self.attributes = self.DataBaseSheet.row_values(1)
        self.report.info(f'Getting Attributes....')  
        return self.attributes
          
    #-------------------------------
   
    def setprimarykey(self,key):
        '''  
    func name : setprimarykey
    params    : key
    process   : sets the key to perform operations on database
    returns   : key
    '''
        try:
            self.getAttributes()
            flag = False
            for model in self.attributes:
                if key==model:
                    flag = True
                    break
            if flag:
                self.key = key
                self.report.info(f'@{self.auth_admin:10}Primary key : {self.key}')
                return key
            else:
                self.invalid.error('could not set primary key')
                return False
        except:
            self.invalid.error('No attribute found on name {key}')          
        
       
    # ----------------------------- 
    def insert(self,record):
        '''
        funcname : insertion
        params   : record
        process  : appends the record
        return   : True
                   if appended
                   False   
        
        '''
        try:
            self.getAttributes()
            position = len(self.DataBaseData.ID)+2
            
            self.DataBaseSheet.insert_row(record,position)
            record = pd.DataFrame([record],columns=self.attributes)
            record = record.loc[0,:]
            self.report.info(f'Inserting/Appending new record')
            self.report.info(f'Admin : {self.auth_admin}')
            self.report.info(f'\022 [1;34;40m Newrecord :\n{record}\n ')
            self.record.warning(f'ADMIN   : @{self.auth_admin}\nDATA INSERTED AT {position}\nNEW RECORD DETAILS\n{record}')
            
            return True
        except:
            self.invalid.error(f'could not insert DataBase .')
            self.invalid.error('RAISE ERROR.....')
            return False
             
    #----------------------------   
    def insertat(self,record,position):
        '''
        func. : insertion at the given record of database into DataBase  
        parameters : record  position
        returns True if inserted
        else 
        returns 5000 
        '''
        try:
            self.getAttributes()
            self.DataBaseSheet.insert_row(record,position)
            
            self.report.info(f'Inserting/Appending new record')
            record = pd.DataFrame([record],columns=self.attributes)
            record = record.loc[0,:]
            self.report.info(f'Admin : {self.auth_admin}')
            self.report.info(f'Newrecord :\n{record} ')
            self.record.warning(f'ADMIN   : @{self.auth_admin}\nDATA INSERTED AT {position}\nNEW RECORD DETAILS\n{record}')
            
            return True
        except:
            self.report.error(f'could not insert DataBase .')
            self.report.error('RAISE ERROR.....')
            
            return False
             
    #-----------------------------
    def deleteat(self,position):
        '''
        func name : Delete
        Delete the element at particular position from the Database
        parameters : position
        returns True if deljeted'''
        try:
            record = self.DataBaseSheet.delete_row(position)
            self.report.info(f'Admin : {self.auth_admin}')
            self.report.warning('successfully deleted....')
            
            
            
            return True   
        except:
            self.report.warning('CAN NOT DELETE OBJECT')
            return False

             
    #-----------------------------
    def delete(self):
        '''
        func name : Delete
        Delete the element at particular position from the Database
        parameters : position
        returns True if deleted'''
        try:
            position = len(self.DataBaseData.ID)+2
            record = self.DataBaseSheet.row_values(position)
            self.DataBaseSheet.delete_row(position)
            record = pd.DataFrame([record],columns=self.attributes)
            self.record.warning(f'Data Deleted\n{record}')
            
            self.report.info(f'Admin : {self.auth_admin}')
            self.report.warning(f'successfully deleted....\n{record}')
            
            return True   
        except:
            self.report.warning('CAN NOT DELETE OBJECT')
            return False           
                        
                                                
    #-----------------------------  
    def searchby(self,element,attribute):
        '''
        func name : searchby
        searches the element in the database
        parameters:attribute name database id
        returns the entire object of the id
        checked by Theddu srihari
        
        '''
        try:
            self.count = 0
            flag = False
            for model in self.DataBaseData[attribute]:
                if model==element:
                    flag = True
                    break
                self.count += 1
            if flag:
                model = self.DataBaseData.loc[self.count,:]
                self.report.info(f'@{self.auth_admin} Record Found ')
                return model
            else:
                self.report.info(f'@{self.auth_admin} No  Record Found ')
                return 'No record Found' 
        except:
            self.report.info(f'@{self.auth_admin} No Attribute Found ')
            return 'No Attribute'
            


    def getelements(self,attribute,value):
        '''
        func name : getelements
        searches the element in the database
        parameters:attribute name database value
        returns the objects of having values
        checked by Theddu srihari
        
        '''
        try:
            count=0
            models=[]
            for model in self.DataBaseData[attribute]:
                if model==value:
                    models.append(self.DataBaseData.loc[count,:])
                count+=1
            return models 
        except:
            return 'No attribute'  
                    
                              
                    
                                   
    def clearDataBase(self):
        try:
            if input('Enter Admin password.  : ')==self.password:
                for count in range(len(self.DataBaseData.ID)+2):
                    self.DataBaseSheet.delete(count)
        except:
           return "Could not delete the data"
   
   
   
    def countnumber(self):
       return len(self.DataBaseData.ID)
   
    #-----------------------------  
    def posterprint(self):
        '''
        func name : posterprint
        prints the entire database in the form of poster for every set of record in database
        parameters: instance method
        returns None
        checked by Theddu Srihari
        '''
        self.report.info(f'@{self.auth_admin}  PosterPrint Availed')
        for record in self.DataBase:
            print('-'*40)
            print(self.title)
            print('-'*40)
            for value in record.items():
                print(f'{value[0]:18}: {value[1]:18}')
            print('-'*40)







