#   Kristen Anderson
#   CIS261
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00  
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print()
        print('Name: ', empname)
        print('From Date: ', fromdate)
        print('To Date: ', todate)
        print('Hours Worked: ', f"{hours:,.2f}")  
        print('Hourly Rate: ', f"{hourlyrate:,.2f}") 
        print('Gross Pay: ', f"{grosspay:,.2f}")  
        print('Tax Rate: ', f"{taxrate:,.1%}") 
        print('Income Tax: ', f"{incometax:,.2f}")  
        print('Net Pay: ', f"{netpay:,.2f}")
        print()
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals['TotEmp'] = TotEmployees
        EmpTotals["HoursTot"] = TotHours
        EmpTotals["GrossPayTot"] = TotGrossPay
        EmpTotals["TaxTot"] = TotTax
        EmpTotals["NetPayTot"] = TotNetPay
def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Number Of Hours: {EmpTotals["HoursTot"]}')
    print(f'Total Gross Pay: {EmpTotals["GrossPayTot"]}')
    print(f'Total Tax: {EmpTotals["TaxTot"]}')
    print(f'Total Net Pay: {EmpTotals["NetPayTot"]}')
    print()
if __name__ == "__main__":
    
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
       
        EmpDetail = (fromdate, todate, empname, hours, hourlyrate, taxrate)
                   
        EmpDetailList.append(EmpDetail)
            
    printinfo(EmpDetailList)
    PrintTotals(EmpTotals)




