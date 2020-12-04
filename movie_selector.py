import sys
import youtube_api

class Entertainment():
    
    def __init__(self):
        self.platform = None
        
    def print_menu(self):  ## Your menu design here
        print("1. Youtube")
        print("2. Hulu")
        print("3. Amazon_Prime")
        print("4. All")
        print("5. Exit")
  
loop=True      
  
while loop:  ## While loop which will keep going until loop = False
    my_entertainment = Entertainment()
    my_entertainment.print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))
     
    if choice==1:     
        print("Youtube has been selected")
        my_entertainment.platform = "Youtube"
        loop = False
    elif choice==2:
        print("Hulu has been selected")
        my_entertainment.platform = "Hulu"
        loop = False
    elif choice==3:
        print("Amazon_Prime has been selected")
        my_entertainment.platform = "Amazon_Prime"
        loop = False
    elif choice==4:
        print("All has been selected")
        my_entertainment.platform = "All"
        loop = False
    elif choice==5:
        print("Menu 5 has been selected")
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")

print(my_entertainment.platform)

if __name__ == "__main__":
    youtube_api.youtube()
    