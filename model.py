#This file all the required classes
from uuid import uuid4

class Company:
    def __init__(self, name, rank, employees, assets , url_company,profits ,revenues ,profits_percent_change, revenue_percent_change):
       self.id = str(uuid4())
       self.name = name
       self.rank = rank 
       self.employees = employees
       self.assets  = assets 
       self.url_company = url_company
       self.profits  =  profits 
       self.revenues = revenues 
       self.profits_percent_change = profits_percent_change
       self.revenue_percent_change = revenue_percent_change