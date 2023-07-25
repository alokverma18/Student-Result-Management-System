import pandas as pd
import matplotlib.pyplot as plt
while True:
    print('----------------------------------------------------------------------------')
    print ('STUDENT RESULT MANAGEMENT SYSTEM - DEVELOPED BY: ALOK KUMAR VERMA')
    print('----------------------------------------------------------------------------')
    print('MENU:')
    print('1. ADD NEW RECORD')
    print('2. DISPLAY ALL RESULTS')
    print('3. SEARCH A RESULT(s) ')
    print('4. DELETE A RECORD(s)')
    print('5. GRAPHICAL REPRESENTATION')
    print('6. QUIT THE APPLICATION')
    choice=int(input('Enter Your Choice as 1,2,3,4,5 or 6: '))
    if choice==1:
        while True:
           id1=input('Enter Student ID: ')
           name1=input('Enter Student Name: ')
           phy1=int(input('Enter Physics Marks: '))
           chem1=int(input('Enter Chemistry Marks: '))
           maths1=int(input('Enter Mathematics Marks: '))
           eng1=int(input('Enter English Marks: '))
           ip1=int(input('Enter IP Marks: '))
           per1=(phy1+chem1+maths1+eng1+ip1)/5
           dic={ }
           dic['ID']=id1
           dic['NAME']=name1
           dic['PHYSICS']=phy1
           dic['CHEMISTRY']=chem1
           dic['MATHS']=maths1
           dic['ENGLISH']=eng1
           dic['IP']=ip1
           dic['PERCENTAGE']=per1
           df=pd.DataFrame([dic])          
           df.to_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv",mode='a',na_rep=' ',header=False,index=False)
           #df.to_csv('d:\person.csv',mode='a',na_rep=' ',header=True)        
           print('******************************************************************************')
           print('Record Added Successfully')         
           print('******************************************************************************')
           x=input('Press any key to continue........')            
           print('\n'*3 )
           break
    elif choice==2:      
        df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv",index_col='ID',usecols=[0,1,2,3,4,5,6,7])
        print('\n',df)        
        print('******************************************************************************')
        x=input('Press any key to continue........')   
        print('\n'*3 )
    elif choice==3:
       while True:
            print('----------------------------------------------------------------------------')
            print('Select the criteria for searching! ! !')
            print('1. Search Student Name-wise!')
            print('2. Search Student ID-wise')
            print('3. Search PHY MARKS-wise!')
            print('4. Search CHEM MARKS-wise!')
            print('5. Search MATHS MARKS-wise!')
            print('6. Search ENGLISH MARKS-wise!')
            print('7. Search IP MARKS-wise!')
            print('8. Search PERCENTAGE-wise!')
            print('9. Return to the main menu!')
            choice=int(input('Enter choice:'))
            if choice==1:
                nm=input('Enter Student Name to search:')
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")          
                b=df[df['NAME']==nm]
                if b.empty:                                   
                    print('******************************************************************************')             
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')                    
                    print('******************************************************************************')
                else:
                    print('------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')                    
                    print('******************************************************************************')
                    print(b)                    
                    print('******************************************************************************')
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==2:
                id=int(input('Enter Student ID to search:'))
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")          
                b=df[df['ID']==id]
                if b.empty:                                        
                    print('******************************************************************************')           
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')
                    print('******************************************************************************')
                else:
                    print('-------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')                    
                    print('******************************************************************************')
                    print(b)                   
                    print('******************************************************************************')
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==3:
                phy=int(input('Enter Physics marks to search:'))
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")          
                b=df[df['PHYSICS']==phy]
                if b.empty:                                        
                    print('******************************************************************************')             
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')
                    print('******************************************************************************')
                else:
                    print('------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')                    
                    print('******************************************************************************')
                    print(b)                    
                    print('******************************************************************************')
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==4:
                CHEM=int(input('Enter Chemistry marks to search:'))
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")          
                b=df[df['CHEMISTRY']==CHEM]
                if b.empty:                                       
                    print('******************************************************************************')               
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')                   
                    print('******************************************************************************')
                else:
                    print('------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')                    
                    print('******************************************************************************')
                    print(b)                   
                    print('******************************************************************************')
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==5:
                maths=int(input('Enter Maths marks to search:'))
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")  
                b=df[df['MATHS']==maths]
                if b.empty:                                        
                    print('******************************************************************************')               
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')                    
                    print('******************************************************************************')
                else:
                    print('------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')
                    print('******************************************************************************')
                    print(b)                    
                    print('******************************************************************************')
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==6:
                Eng=int(input('Enter English marks to search:'))
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")          
                b=df[df['ENGLISH']==Eng]
                if b.empty:                                      
                    print('******************************************************************************')               
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')                 
                    print('******************************************************************************')
                else:
                    print('------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')                    
                    print('******************************************************************************')
                    print(b)                    
                    print('******************************************************************************')
                x=input('Press any key to continue........')
                print('\n'*3 )           
            elif choice==7:
                ip=int(input('Enter IP marks to search:'))
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")          
                b=df[df['IP']==ip]
                if b.empty:                    
                    print('******************************************************************************')               
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')                   
                    print('******************************************************************************')
                else:
                    print('------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')                    
                    print('******************************************************************************')
                    print(b)                   
                    print('******************************************************************************')       
            elif choice==8:
                per=float(input('Enter PERCENTAGE to search:'))
                df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")          
                b=df[df['PERCENTAGE']==per]
                if b.empty:                                        
                    print('******************************************************************************')               
                    print(' xxxxxxxxx Record Not Found!!  xxxxxxxxxx')                   
                    print('******************************************************************************')
                else:
                    print('------------------------------------------------------------------------------')             
                    print(len(b), 'Record(s) found!!')
                    print('******************************************************************************')
                    print(b)                    
                    print('******************************************************************************')         
            elif choice==9:
                break
    elif choice==4:
        df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")
        print('*******************CURRENT STATUS OF RESULTS OF THE STUDENTS******************')
        print(df)        
        print('******************************************************************************')  
        idx=int(input('Enter row index of the record to be deleted:'))
        x=int(input('Are you sure to delete the record. Press 1 for YES and 0 for NO:'))
        if x==1:
            df.drop(idx,inplace=True)            
            df.to_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv",mode='w',na_rep='  ')            
            print('******************************************************************************')  
            print('Record deleted successfully')           
            print('******************************************************************************')
        else:
            print('******************************************************************************')
            print('Delete Operetion is Cancelled')           
            print('******************************************************************************')
        x=input('Press any key to continue..........................................')
        print('\n'*3 )
    elif choice==5:
        while True:
            print('------------------------------------------------------------------------------')
            print('Select the criteria for PLOTTING !!!')
            print('1. PLOT THE GRAPH PHYSICS MARKS WISE!')
            print('2. PLOT THE GRAPH CHEMISTRY MARKS WISE!')
            print('3. PLOT THE GRAPH MATHS MARKS WISE!')
            print('4. PLOT THE GRAPH ENGLISH MARKS WISE!')
            print('5. PLOT THE GRAPH IP MARKS WISE!')
            print('6. PLOT THE GRAPH OVERALL PERCENTAGE WISE!')
            print('7. Return to the main menu!')
            choice=int(input('Enter choice:'))
            df=pd.read_csv(r"C:\Users\Alok Verma\Desktop\AK\Code\Book1.csv")
            if choice==1:
                a=df['PHYSICS'].tolist()
                x=df['NAME'].tolist()
                plt.bar(x,a,color=['red','yellow','blue','green','grey','violet','orange','indigo','brown'],width=0.5)
                plt.xlabel('NAMES OF THE STUDENTS')
                plt.ylabel('MARKS')
                plt.title('PHYSICS MARKS')
                plt.show()
                print('******************************************************************************')  
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==2:
                a=df['CHEMISTRY'].tolist()
                x=df['NAME'].tolist()                
                plt.bar(x,a,color=['red','yellow','blue','green','grey','violet','orange','indigo','brown'],width=0.5)
                plt.xlabel('NAMES OF THE STUDENTS')
                plt.ylabel('MARKS')
                plt.title('CHEMISTRY MARKS')
                plt.show()
                print('******************************************************************************')  
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==3:
                a=df['MATHS'].tolist()
                x=df['NAME'].tolist()                
                plt.bar(x,a,color=['red','yellow','blue','green','grey','violet','orange','indigo','brown'],width=0.5)
                plt.xlabel('NAMES OF THE STUDENTS')
                plt.ylabel('MARKS')
                plt.title('MATHS MARKS')
                plt.show()
                print('******************************************************************************')  
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==4:
                a=df['ENGLISH'].tolist()
                x=df['NAME'].tolist()                
                plt.bar(x,a,color=['red','yellow','blue','green','grey','violet','orange','indigo','brown'],width=0.5)
                plt.xlabel('NAMES OF THE STUDENTS')
                plt.ylabel('MARKS')
                plt.title('ENGLISH MARKS')
                plt.show()
                print('******************************************************************************')  
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==5:
                a=df['IP'].tolist()
                x=df['NAME'].tolist()                
                plt.bar(x,a,color=['red','yellow','blue','green','grey','violet','orange','indigo','brown'],width=0.5)
                plt.xlabel('NAMES OF THE STUDENTS')
                plt.ylabel('MARKS')
                plt.title('IP MARKS')
                plt.show()             
                print('******************************************************************************')  
                x=input('Press any key to continue........')
                print('\n'*3 )
            elif choice==6:
                a=df['PERCENTAGE'].tolist()
                x=df['NAME'].tolist()               
                plt.bar(x,a,color=['red','yellow','blue','green','grey','violet','orange','indigo','brown'],width=0.5)
                plt.xlabel('NAMES OF THE STUDENTS')
                plt.ylabel('PERCENTAGE')
                plt.title('OVERALL PERCENTAGE')
                plt.show()
                print('******************************************************************************')  
                x=input('Press any key to continue........')
                print('\n'*3 )           
            break 
    elif choice==6:
        print('Thank You!!!!')
        break

#Note : Change the path of the csv file
