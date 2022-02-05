class CoffeMashine:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    funds = 550

    def mashine_status(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups''')

        if self.funds > 0:
            print(f"${self.funds} of money\n")
        if self.funds == 0:
            print(f"{self.funds} of money\n")

    def check(self, cur_water, cur_coffee, cur_milk, cur_funds):

        if self.water >= cur_water and self.coffee >= cur_coffee and self.milk >= cur_milk:
            print("I have enough resources, making you a coffee!\n")
            self.water -= cur_water
            self.coffee -= cur_coffee
            self.milk -= cur_milk
            self.funds += cur_funds
            self.cups -= 1

        else:
            if self.water < cur_water:
                print("Sorry, not enough water!\n")
            if self.milk < cur_milk:
                print("Sorry, not enough milk!\n")
            if self.coffee < cur_coffee:
                print("Sorry, not coffee beans!\n")

    def buy(self):

        if self.cups >= 0:
            product = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")

            if product == "back":
                self.action()
            elif product == "1":
                self.check(250, 16, 0, 4)
            elif product == "2":
                self.check(350, 20, 75, 7)
            elif product == "3":
                self.check(200, 12, 100, 6)
        else:
            print("Sorry, not enough disposable coffee cups!")
            self.cups -= 1

    def fill(self):

        self.water += int(input("\nWrite how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable coffee cups you want to add:\n"))
        print("")

    def take(self):

        print(f"\nI gave you ${self.funds}\n")
        self.funds = 0

    def action(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "exit":
            return False
        else:
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                print("")
                self.mashine_status()
            return True


def main():
    mashine = CoffeMashine()
    while mashine.action() == True:
        continue


main()
