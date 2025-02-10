### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    global machine_resources
    global sandwich_size
    global coins
    global ingredients
    def __init__(self, machine_resources):
        size = ""
        properInput = False
        userInput = ""
        while(not properInput): 
            userInput = input("What would you like? (small, medium, large, off, report): ")
            if (userInput == "small" or userInput == "medium" or userInput == "large" or userInput == "off" or userInput == "report"):
                if (userInput == "small"):
                    size = "small"
                elif(userInput == "medium"):
                    size = "medium"
                elif(userInput == "large"):
                    size = "large"
                elif(userInput == "off"):
                    size = "off"
                    print("Turning off")
                else:
                    size = "report"
                    print("Bread: "+str(resources["bread"])+" slice(s)")
                    print("Ham: "+str(resources["ham"])+" slice(s)")
                    print("Cheese: "+str(resources["cheese"])+" pound(s)")
                properInput = True
        self.sandwich_size = size
        self.machine_resources = machine_resources
        self.coins = 0.0

    def check_resources(self, ingredients):
        self.ingredients = ingredients
        if (self.machine_resources["bread"] < ingredients[self.sandwich_size]["ingredients"]["bread"]):
            print("Sorry there is not enough bread")
            return False
        elif (self.machine_resources["ham"] < ingredients[self.sandwich_size]["ingredients"]["ham"]):
            print("Sorry there is not enough ham")
            return False
        elif (self.machine_resources["cheese"] < ingredients[self.sandwich_size]["ingredients"]["cheese"]):
            print("Sorry there is not enough cheese")
            return False
        else:
            return True

    def process_coins(self):
        print("Please insert coins.")
        coins = 0.0
        finished = False
        while(not finished):
            dollars = float(input("how many large dollars?: "))
            halfDollars = float(input("how many half dollars?: "))
            quarters = float(input("how many quarters?: "))
            nickels = float(input("how many nickels?: "))
            coins = dollars + halfDollars*0.5 + quarters*0.25 + nickels*0.05
            self.coins += coins
            if(self.transaction_result(self.coins, self.ingredients[self.sandwich_size]["cost"])):
                finished = True
                return self.coins
            else:
                print("Sorry, that’s not enough money. Money refunded")
                self.coins = 0.0
                return 0.0

    def transaction_result(self, coins, cost):
        difference = self.coins - float(self.ingredients[self.sandwich_size]["cost"])
        if (difference >= 0):
            print("Here is $"+str(difference)+" in change.")
            self.coins = self.ingredients[self.sandwich_size]["cost"]
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        resources["bread"] -= order_ingredients[sandwich_size]["ingredients"]["bread"]
        resources["ham"] -= order_ingredients[sandwich_size]["ingredients"]["ham"]
        resources["cheese"] -= order_ingredients[sandwich_size]["ingredients"]["cheese"]

### Make an instance of SandwichMachine class and write the rest of the codes ###

while(True):
    sandwichMachine = SandwichMachine(resources)
    if(sandwichMachine.sandwich_size == "off"):
        break
    elif (sandwichMachine.sandwich_size != "report"):
        if(sandwichMachine.check_resources(recipes)):
            if (sandwichMachine.transaction_result):
                sandwichMachine.make_sandwich(sandwichMachine.sandwich_size, sandwichMachine.ingredients)
                print(sandwichMachine.sandwich_size+ " sandwich is ready. Bon appetit!")

        



