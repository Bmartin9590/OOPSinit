## To create a OOPS: First you create a class
 #Then you create your "constructor" with the "def __init__(self)" method, and list the categories that you will fill in after (self)
# def a variable for the final version of the car so you can call it later and list the print functions for each category, make sure to include (self) after
#Create a variable to call the car class and input the characteristics
#Use your variable you just created to print (printTheCar) your output in the console

class footballplayer:
    def __init__(self, height, weight, position, rating):
        self.height = height
        self.weight = weight
        self.position = position
        self.rating = rating
    
    def printPlayer(self):
        print("Their height will be", self.height)
        print("Their weight will be", self.weight)
        print("Their poistion is", self.position)
        print("Their rating is", self.rating)
myplayer = footballplayer("6ft", "180lbs", "QB", "99")
myplayer.printPlayer() 
