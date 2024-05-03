
from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.users


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
  
        
  def insertion_sort_click(self, **event_args):
    arr = list(self.text_box_1.text.split(" "))
    """This method is called when the button is clicked"""
    insertion_sort(arr)
    s = ""
    for i in range(len(arr)):
      s = s + arr[i]+" "
    self.text_box_2.text = s + "\tinsertion sort"

  def selection_sort_click(self, **event_args):
    arr = list(self.text_box_1.text.split(" "))
    """This method is called when the button is clicked"""
    selection_sort(arr)
    s = ""
    for i in range(len(arr)):
      s = s + arr[i]+" "
    self.text_box_2.text = s + "\tselection sort"

  def merge_sort_click(self, **event_args):
    arr = list(self.text_box_1.text.split(" "))
    """This method is called when the button is clicked"""
    mergeSort(arr)
    s = ""
    for i in range(len(arr)):
      s = s + arr[i]+" "
    self.text_box_2.text = s + "\tmerge sort"

  def bubble_sort_click(self, **event_args):
    arr = list(self.text_box_1.text.split(" "))
    """This method is called when the button is clicked"""
    bubble_sort(arr)
    s = ""
    for i in range(len(arr)):
      s = s + arr[i]+" "
    self.text_box_2.text = s + "\tbubble sort"


def insertion_sort(arr):
      n = len(arr)
      for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
      n = len(arr)
      for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

