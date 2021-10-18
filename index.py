from tkinter import ttk
from tkinter import *
import trainModel

class PerformanceTestAnalysis:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Performance Test Analysis')
        self.wind.geometry("400x300")

        ## Creating a Frame Container
        frame = LabelFrame(self.wind, text = 'Predict Outcome')
        frame.grid(row = 0, column = 2, columnspan = 4, pady = 30, padx=80)

        ## Elapse input
        Label(frame, text = 'Elapse: ').grid(row = 1, column = 0)
        self.elapse = Entry(frame)
        self.elapse.focus()
        self.elapse.grid(row=1, column=1)


        ## ResponseCode input
        Label(frame, text = 'ResponseCode: ').grid(row = 2, column = 0)
        self.responseCode = Entry(frame)
        self.responseCode.grid(row=2, column=1)

        ## success input
        Label(frame, text='Success: ').grid(row=3, column=0)
        self.combo= ttk.Combobox(frame,state="readonly",width=17)
        self.combo['values'] = [1,0]
        self.combo.grid(row=3, column=1)
        #self.success = Entry(frame)
        #self.success.grid(row=3, column=1)

        ## bytes input
        Label(frame, text = 'Bytes: ').grid(row = 4, column = 0)
        self.bytes = Entry(frame)
        self.bytes.grid(row=4, column=1)

        ##sentBytes
        Label(frame, text = 'Sent Bytes: ').grid(row = 5, column = 0)
        self.sentBytes = Entry(frame)
        self.sentBytes.grid(row=5, column=1)

        ## allThreads input
        Label(frame, text = 'All Threads: ').grid(row = 6, column = 0)
        self.allThreads = Entry(frame)
        self.allThreads.grid(row=6, column=1)

        ## Latency input
        Label(frame, text = 'Latency: ').grid(row = 7, column = 0)
        self.latency = Entry(frame)
        self.latency.grid(row=7, column=1)

        ## Connect input
        Label(frame, text = 'Connect: ').grid(row = 8, column = 0)
        self.connect = Entry(frame)
        self.connect.grid(row=8, column=1)


        ## Button Add Product
        # sticky = De Oeste a Este (Todo el ancho disponible)
        ttk.Button(frame, text = 'Predict', command = self.predictOutCome).grid(row = 9, columnspan = 2, sticky = W + E)

        # Output message
        self.message = Label(text = '', fg = 'Green', font="Ubuntu 14")
        self.message.grid(row = 3, column = 3,sticky = W + E)

    def validation(self):
        return len(self.elapse.get()) != 0 and len(self.responseCode.get()) != 0 and len(self.combo.get()) != 0 and len(self.bytes.get()) != 0 and len(self.allThreads.get()) != 0 and len(self.latency.get()) != 0 and len(self.connect.get()) != 0
 
    def predictOutCome(self):
        try:
            self.message['text'] = ''
            if self.validation():
                datos = {"V0":self.elapse.get(), "V1":self.responseCode.get(),"V2":self.combo.get(), "V3":self.bytes.get(), "V4":self.sentBytes.get(), "V5":self.allThreads.get(), "V6":self.latency.get(), "V7": self.connect.get()}
                output = trainModel.check_input(datos)
                if ( output == 1.0):
                    self.message['fg']= 'green'
                    self.message['text'] = 'Meets the criteria '
                else:
                    self.message['fg']= 'red'
                    self.message['text'] = 'Does not meet the criteria '
            else:
                self.message['fg']= 'red'
                self.message['text'] = 'All fields are required'
        except:
            print("An error occurred evaluating the input data")

if __name__ == '__main__':
   window = Tk()
   application = PerformanceTestAnalysis(window)
   window.mainloop()