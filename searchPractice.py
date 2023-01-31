from tkinter import *
from time import time
from xmlrpc.client import boolean

class Searching(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.function = {0:self.linear, 1:self.binary}
        self.inputFormat = {0:self.list_entry,1:self.dict_entry}
        self.master.title("Searching")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)
        self.refOfElements = []
        self.listOfElements = []
        self.refOfKeys = []
        self.refOfValues = []
        self.listOfKeys = []
        self.listOfValues = []
        self.dict = {}
        self.size_var = StringVar()
        self.size_entry = Entry(self,textvariable=self.size_var)
        self.prFlag = FALSE
        self.ele_btn = Button(self,text = 'Start sorting',command = self.eleCheck)
        self.dict_btn = Button(self,text = 'Submit entries',command = self.genDict)
        self.key_var = StringVar()
        self.key_entry = Entry(self,textvariable=self.key_var)

        
        #label for search intro
        self.label1 = Label(self, text="Searching algorithms", width=25, height=2)
        self.label1.grid(row=0, column=1, sticky=N+E+W)
        self.label2 = Label(self, text='Enter number of elements : ', width=2, height=2)
        self.label3 = Label(self, text='', width=2, height=2)

        #label for errors
        self.error = Label(self,text='')
        self.error.grid(row=15,column=1)

        #Radio buttons for search
        self.v_search = IntVar()
        for indx, button in enumerate(('LinearSearch','BinarySearch')):
            name = button 
            button = Radiobutton(self, text=name, variable=self.v_search, value=indx)
            button.grid(row=1, column=indx, sticky=W+E+N+S)
        button.deselect()

        #radio buttons for input format
        self.v_input = IntVar()
        for indx, button in enumerate(('List', 'Dictionary')):
            name = button 
            button = Radiobutton(self, text=name, variable=self.v_input, value=indx)
            button.grid(row=2, column=indx, sticky=W+E+N+S)
        button.deselect()

        #button to get size
        self.button4 = Button(self,text='Submit',command=self.getSize)
        self.button4.grid(row=3, column=1, sticky=W+E+N+S)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(5, weight=1)

    # def create_but2sort(self):
    #     self.button5 = Button(self, text='start sorting', command=self.sortit)
    #     self.button5.grid(row=4, column=1, sticky=W+E+N+S)
    #     self.rowconfigure(5, weight=1 )
    #     self.columnconfigure(5, weight=1)


    def eleCheck(self):
        flag = TRUE
        self.listOfElements.clear()
        for e in self.refOfElements:
            t = e.get()
            self.listOfElements.append(t)
        print(self.listOfElements)
        for e in self.listOfElements:
            print(e)
            if e =='':
                flag=FALSE
                self.error.config(text='Dont leave entry blank!! Re-enter size and try again!',fg = 'red')
            elif e.isalnum() == FALSE:
                flag = FALSE    
                self.error.config(text='One of the entries is not alphanumeric. Re-enter size and try again!',fg = 'red')
            
                

           
        if flag==TRUE:
            s = self.size_var.get()
            self.key_label = Label(self,text = 'Enter key : ')
            self.key_label.grid(row=20 + int(s), column=0)
            self.key_entry.grid(row = 20+int(s), column=1)
            self.key_btn= Button(self,text='Submit for searching...',command = self.searchit)
            self.key_btn.grid(row=20 + int(s), column=2, sticky=W+E+N+S)
    
            

        self.error.after(3000,lambda:self.error.config(text=''))
        

    def list_entry(self):
        print('hey from list')
        self.listOfElements.clear()
        s = self.size_var.get()
        for j in range(int(s)):
            ele_label=Label(self,text='Entry: '+str(j+1),fg='blue')
            ele_label.grid(row=j+17,column=0,padx=3)

            ele_entry = Entry(self,bg='lightyellow') 
            ele_entry.grid(row=j+17, column=1,padx=10,pady=3) 
            
            self.refOfElements.append(ele_entry) #store references

        self.ele_btn = Button(self,text = 'Submit elements',command = self.eleCheck)
        self.ele_btn.grid(row=17,column=2,sticky=S)

        # self.list_btn = Button(self,text = 'Submit size',command = self.sizeCheck)
        # self.list_btn.grid(row=10,column=1,sticky=S)
    def genDict(self):        
        flag = TRUE
        self.listOfKeys.clear()
        self.listOfValues.clear()
        for e in self.refOfKeys:
            p = e.get()
            self.listOfKeys.append(p)
        for f in self.refOfValues:
            q = f.get()
            self.listOfValues.append(q)
        for e in self.listOfKeys:
            print(e)
            if e =='':
                flag=FALSE
                self.error.config(text='Dont leave entry blank!! Re-enter size and try again!',fg = 'red')
            elif e.isalnum() == FALSE:
                flag = FALSE    
                self.error.config(text='One of the entries is not alphanumeric. Re-enter size and try again!',fg = 'red')
        for e in self.listOfValues:
            print(e)
            if e =='':
                flag=FALSE
                self.error.config(text='Dont leave entry blank!! Re-enter size and try again!',fg = 'red')
            elif e.isalnum() == FALSE:
                flag = FALSE    
                self.error.config(text='One of the entries is not alphanumeric. Re-enter size and try again!',fg = 'red')
            
        if flag==TRUE:
            self.dict = dict(zip(self.listOfKeys,self.listOfValues))    
            print(self.dict)           
            # self.sortit()
            print('everything is alright')
            pass

        self.error.after(3000,lambda:self.error.config(text=''))
                    

    def dict_entry(self):
        print('hey from dict')
        s = self.size_var.get()
        for w in Frame.winfo_children(self):
            if(w.winfo_class()=='Entry'):
                if(w!=self.size_entry):
                        w.destroy()
            elif(w.winfo_class()=='Label'):
                if(w!=self.label1 and w!=self.label2 and w!= self.label3 and  w!=self.error):
                    w.destroy()
            elif(w.winfo_class()=='Button'):
                if(w==self.ele_btn):
                    w.destroy()
        
        for j in range(int(s)):
            key_label=Label(self,text='key: '+str(j+1),fg='blue')
            key_label.grid(row=j+17,column=0,padx=3)

            key_entry = Entry(self,bg='lightyellow') 
            key_entry.grid(row=j+17, column=1,padx=10,pady=3) 
            self.refOfKeys.append(key_entry)

        for j in range(int(s)):
            value_label=Label(self,text='value: '+str(j+1),fg='blue')
            value_label.grid(row=j+17,column=2,padx=3)

            value_entry = Entry(self,bg='lightyellow') 
            value_entry.grid(row=j+17, column=3,padx=10,pady=3)
            
            self.refOfValues.append(value_entry)
            # self.refOfElements.append(ele_entry) #store references

        self.ele_btn = Button(self,text = 'Submit entries',command = self.eleCheck)
        self.ele_btn.grid(row=17,column=5,sticky=S)        

    def sizeCheck(self):
        if(self.prFlag ==TRUE):
            self.label3.destroy()
        flag = FALSE
        s = (self.size_entry.get())
        if(s.isdigit()==FALSE or int(s)<=0):
            self.error.config(text='Please enter an appropriate value!!',fg = 'red')
        else :
            flag = TRUE

        # holds error for 1.5 seconds
        self.error.after(1500,lambda:self.error.config(text=''))

        if(flag==TRUE):
            for w in Frame.winfo_children(self):
                if(w.winfo_class()=='Entry'):
                    if(w!=self.size_entry and w!=self.key_entry):
                        w.destroy()
                elif(w.winfo_class()=='Label'):
                    if(w!=self.label1 and w!=self.label2 and w!= self.label3 and  w!=self.error):
                        w.destroy()
                elif(w.winfo_class()=='Button'):
                    if(w!=self.size_btn):
                        w.destroy()
            self.refOfElements.clear()
            self.listOfElements.clear()
            inputFormat = self.inputFormat[self.v_input.get()]
            inputFormat()          





    def getSize(self):
        
        # self.label2 = Label(self, text='Enter number of elements : ', width=2, height=2)
        self.label2.grid(row =5, columnspan=10, sticky=W+E+N+S)
        self.size_entry.grid(row=7,columnspan=10)
        self.size_btn = Button(self,text = 'Submit size',command = self.sizeCheck)
        self.size_btn.grid(row=10,column=1,sticky=S)

    def searchit(self):
        function = self.function[self.v_search.get()]
        result = function()
        s = self.size_var.get()
        if (result == -1):
           self.label3 = Label(self, text= 'Not found !!' )
           self.label3.grid(row= 21 + int(s),column=1)
        else: 
            self.label3 = Label(self,text = 'Element found at position: '+ str(result+1))   
            self.label3.grid(row=21 + int(s),column=1 )

    def linear(self):
        for i in range(0,len(self.listOfElements)):
        
            if self.listOfElements[i] == self.key_var.get():
                return i
 
        return -1
    

    def binary(self):
        l=0
        r=len(self.listOfElements)-1
        while(l<=r):
          mid=(l+r)//2
          if(self.listOfElements[mid]==self.key_var.get()):
            return mid
          elif(self.key_var.get()<self.listOfElements[mid]):
            r=mid-1
          elif(self.key_var.get()>self.listOfElements[mid]):
            l=mid+1
        return -1
        
def main():
    Searching().mainloop()

if __name__ == "__main__":
    
    main()