#!/usr/bin/python
import math

class VendingMachine(object):
    def __init__(self):
        self._user_input_value = 0

        self._coins_dict = {
            'N':{
                'quantity': 10,
                'value': 0.05
                },
            'D':{
                'quantity': 10, 
                'value': 0.10
                },
            'Q':{
                'quantity': 10, 
                'value': 0.25
                },
            'DOLLAR':{
                'quantity': 10, 
                'value': 1.00
                }
        }

        self._product_dict = {
            'A':{
                'quantity': 10,
                'value': 0.65
            },
            'B':{
                'quantity': 10,
                'value': 1.00
            },
            'C':{
                'quantity': 10,
                'value': 1.50
            }
        }

        
    def parse_input_to_list(self, input):
        """Parse the input string which is separetd by the comma and a space and store the result into a list

        Args:
            input (String): User input to represent their actions
        
        Returns:
            List: A list of elements contain in the input string
        """
        parsed_input_list = input.split(", ")
        return parsed_input_list


    def output_product_and_response(self, product):
        """Output the product A or B or C and changes or responses based on the user inputs
        
        Args:
            product (String): User requested inout product type A or B or C
        
        Returns:
            List: Product or/and response
        """
        vm_response = []
        item_value = self._product_dict[product]['value']
        
        # The user input amount is greater than and equal to ITEM's value
        if (self._user_input_value >= item_value and self._product_dict[product]['quantity'] > 0):
            vm_response.append(product)
            change_value = self._user_input_value - item_value
            if (change_value > 0):
                vm_response.extend(self.find_match_coins(change_value))
            self._user_input_value = 0

        elif (self._user_input_value >= item_value and self._product_dict[product]['quantity'] == 0):
            vm_response.append("Don't have enough product %s" % product)
            vm_response.append(self.find_match_coins((self._user_input_value)))

        else:
            owe_amount = item_value - self._user_input_value
            vm_response.append("Don't have enough money, please insert $%.2f extra." % owe_amount)

        return vm_response


    def insert_coin(self, item):
        """User insert the coin to the vending machine and the corresponding state of user_insert_amount 
        and corresponding amount of money in the vending machine increamented
        
        Args:
            item (String): Coins, i.e. N, Q, DOLLAR
        """
        self._coins_dict[item]['quantity'] += 1
        self._user_input_value += self._coins_dict[item]['value']


    def enter_different_mode(self, input):
        """Based on the user input to enter the corresponding state in the vending machine
        
        Args:
            input (String): User input money and product request, e.g. Q, Q, Q, Q, GET-A
        
        Returns:
            Changes and product or responses, e.g. A
        """
        input_list = self.parse_input_to_list(input)

        for item in input_list:
            if (item in self._coins_dict):
                self.insert_coin(item)

            elif (item == 'COIN-RETURN'):
                return self.find_match_coins(self._user_input_value)

            elif (item.startswith('GET-') and len(item) == 5):
                product = item[-1]

                if(product in self._product_dict):
                    self._product_dict[product]['quantity'] -= 1
                    return self.output_product_and_response(product)

            elif (item == 'SERVICE'):
                self.service()
                return "Enter Service Mode..."

            else :
                return "Invalid Input!"


    def find_match_coins(self, money):
        """Find the match coins for the amount of input money
        
        Args:
            money (float): Amount of number/money
        
        Returns:
            List: Coin representation of value, e.g. Q, Q (0.50)
        """
        return_coin_list = []

        deduct_coin = self.find_the_largest_available_coin(money)

        self._coins_dict[deduct_coin]['quantity'] -= 1
        return_coin_list.append(deduct_coin)
        remain_amount = money - self._coins_dict[deduct_coin]['value']
        remain_amount = round(remain_amount, 2)


        if (remain_amount == 0 ):
            return return_coin_list

        return return_coin_list + self.find_match_coins(remain_amount)


    def find_the_largest_available_coin(self, money):
        """Find the largest the possible coin from the coin dictionary based on the amount of input money
        
        Args:
            money (float): Description
        
        Returns:
            String: Key of the coin
        """
        pre_diff = float('inf')
        max_coin_value = 0
        final_coin = ''
        for coin in self._coins_dict:
            current_diff = money - self._coins_dict[coin]['value']

            if (money - self._coins_dict[coin]['value']) >= 0 and \
            (max_coin_value < self._coins_dict[coin]['value']) and \
            (self._coins_dict[coin]['quantity'] > 0):
                max_coin_value = self._coins_dict[coin]['value']
                final_coin = coin

        return final_coin

    def service(self):
        """Service will reset each coin's and item's quantity to 10
        """
        for coin in self._coins_dict:
            self._coins_dict[coin]['quantity'] = 10

        for item in self._product_dict:
            self._product_dict[item]['quantity'] = 10


if __name__=="__main__":
    pass
