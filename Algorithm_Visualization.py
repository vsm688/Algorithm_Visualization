"""
Algorithm visulisation tool implemented with tkinter which also uses multithreading and prevents the program from crashing/freezing, more algorithms to be added over time. 
Author: Vakho/Michael Shvili 

"""



from tkinter import *
from tkinter import ttk
import random
import time
import threading


def bubble_sort(array_val,visualise):
    color_array = [None] * len(array_val)
    for i in range(len(array_val) - 1):
        
        for k in range(len(array_val) - i - 1):
            
            if array_val[k] > array_val[k + 1 ]:
                array_val[k],array_val[k + 1] = array_val[k + 1],array_val[k] # highlights the indicies which are being compared / swapped.
                for x in range(len(array_val)):
                    if x == k or x == k + 1:
                        color_array[x] = "#0000FF"
                    else:
                        color_array[x] = "#ff0000"
                t2 = threading.Thread(target = visualise, args = (array_val, color_array))
                # creates a thread to allocate resources to run the visulisation seperately, allows main program/window to continue running
                t2.start()
                time.sleep(0.1) # delay in each "swap" and hence visulisation.
def selection_sort(array_val,visualise):
    color_array = [None] * len(array_val)
    for i in range(len(array_val)):
        min_index = i
        for k in range(i + 1, len(array_val) ):
            if array_val[min_index] > array_val[k]:
                min_index = k
                for x in range(0,len(color_array)): # code for coloring the bars based on swap.
                    if x == k:
                        color_array[x] = "#0000FF"
                    elif x < i + 3 :
                        color_array[x] = "#32CD32"
                    else:
                        color_array[x] = "#FF0000"
                t2 = threading.Thread(target = visualise, args = (array_val, color_array))
                # creates a thread to allocate resources to run the visulisation seperately, allows main program/window to continue running
                t2.start()
                time.sleep(0.1) # delay in each "swap" and hence visulisation.

        array_val[i],array_val[min_index] = array_val[min_index], array_val[i]
    color_array[-2] = "#32CD32"
    color_array[-1] = "#32CD32"
    t2 = threading.Thread(target = visualise, args = (array_val, color_array))
    # creates a thread to allocate resources to run the visulisation seperately, allows main program/window to continue running
    t2.start()
        
def insertion_sort(array_val,visualise):
    color_array = [None] * len(array_val)
    for i in range(1,len(array_val)):
        key = array_val[i]
        j = i - 1
        while j >= 0 and key < array_val[j]:
            array_val[j + 1] = array_val[j]
            
            
            j -= 1
        
        array_val[j + 1] = key
        for x in range(len(array_val)):
            if x == j + 1: # this color (blue) is the position of where the previous element was inserted
                color_array[x] = "#0000FF" 
            elif x == i + 1 :
                color_array[x] = "#32CD32" # this color(light green) is the position of where our current element is
            else: 
                color_array[x] = "#FF0000" # this color (red) represents all the other elements 

        t2 = threading.Thread(target = visualise, args = (array_val,color_array))
        t2.start()
        time.sleep(0.1) # delay in each "swap" and hence visulisation.
        


    
def visualise(array_val, colors):
    array_display.delete("all")
    rectangle_width = array_display.winfo_width() / (len(array_val) + 1 )

    bar_graph = []
    for i in range(len(data)):
        bar_graph.append(data[i] / max(data))

    for i, height in enumerate(bar_graph):
        x0 = i * rectangle_width + 4 + 2
        y0 = 300 - height * 200
        x1 = ( i + 1 ) * rectangle_width
        y1 = 300
        array_display.create_rectangle(x0,y0,x1,y1, fill = colors[i])

    window.update_idletasks()
def create_array():
    global data
    data = []
    color_array = []
    for i in range(0,50):
        val = random.randint(1,51)
        data.append(val)
    for k in range(0,len(data)):
        color_array.append('#ff0000') # append array of HEX value for red ( unsorted)
    
    visualise(data,color_array)
def sort():
    global data
    print(data)
    if menu.get() == "Bubble sort":
        print("true")
        t1 = threading.Thread(target = bubble_sort, args = (data,visualise))
        t1.start()
    if menu.get() == "Selection sort":
        print("true")
        t1 = threading.Thread(target = selection_sort, args = (data,visualise))
        t1.start()
        
    if menu.get() == "Insertion sort":
        print("true")
        t1  = threading.Thread(target = insertion_sort, args = (data, visualise))
        t1.start()
# add windows which tells you information about the sorting algorithm
sorting_algorithms = ["Bubble sort", "Selection sort", "Insertion sort"]

#creating the UI window
window = Tk()
window.title("Sorting Algorithm")
window.geometry("700x600")
window.maxsize(900,900)

#defining labels for selecting algorithm
algorithm_selector = Label(window, text = "Select Algorithm:")
algorithm_selector.grid(column = 0, row = 0)

sort_button = Button(window,command = sort, text = "Sort")
sort_button.grid(column = 1, row = 0)

generate_array = Button(window, command = create_array,text = "Generate Array")
generate_array.grid(column = 1, row = 0)

algorithm_selector.place(relx = 0.3, rely = 0, anchor ="n")
sort_button.place(relx = 0.5, rely = 0.1, anchor = "n")
generate_array.place(relx = 0.3, rely = 0.1, anchor = "n")


#generating dropdown menu for sorting algorithm
menu = ttk.Combobox(window, textvariable = StringVar(), values = sorting_algorithms)
menu.grid (row = 1, column = 1 )
menu.place(relx = 0.5, rely = 0, anchor = "n")
array_display = Canvas(window, width = 500, height = 300, bg = "#FFFFED")
array_display.grid(row = 1, column = 0)
array_display.place(relx = 0.5, rely = 1, anchor = "s")

window.mainloop()
#defining button for executing sorting algorithm

