 # This project will allow the user to enter the name and cost of an expense. The program will inform the user on how much they spend each month and annually on that expense .
    # 9/22/21
    # CTI-110 P1HW2 - Basic Math
    # Tommy Williams
    #
    #


                #Input Section
                    #expense =(input("Enter Name of expense"))
                    #monthly_charge =float(input("Enter montly charge:"))
                #process
                    #monthly_charge_wTax =float(tax + monthly_charge)
                    #annual_charge = (monthly_charge_wTax * 12)
                    #print("Bill:$",expense, "--------- Before Tax:$",monthly_charge)
                #output
                    #print("Monthly Tax:$",tax)
                    #print("Monthly Charge:$",monthly_charge_wTax)
                    #print("Annual Charge:$",annual_charge )

                
                



    
    #input  enter "Name of expense" into expense 
expense = (input("Enter name of expense:"))
    #enter monthly charge 
monthly_charge =float(input("Enter monthly charge:"))
    #(proccess) the variable tax is assigned the sum of monthly_charge * .06
tax = float(monthly_charge * .06)
    #the sum oftax + monthly charge = monthly _ chargewTax    
monthly_charge_wTax =float(tax + monthly_charge)
    # monthyl_chagewTax * 12 is stored inannual_charge 
annual_charge = (monthly_charge_wTax * 12)

    #"Bill:$",expense, "--------- Before Tax:$",monthly_charge is displayed
print("Bill:$",expense, "--------- Before Tax:$",monthly_charge)
    #"Monthly Tax:$",tax is displayed
print("Monthly Tax:$",tax)
    #"Monthly Charge:$",monthly_charge_wTax is displayed
print("Monthly Charge:$",monthly_charge_wTax)
    #"Annual Charge:$",annual_charge is displayed
print("Annual Charge:$",annual_charge)


