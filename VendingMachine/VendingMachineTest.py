#!/usr/bin/python

import unittest
from VendingMachine import *

class VendingMachineTest(unittest.TestCase):

    def test_parse_user_iput(self):
        vm = VendingMachine()
        self.assertEqual(vm.parse_input_to_list('Q, Q, Q, Q, GET-B'), ['Q','Q','Q','Q','GET-B'])

    def test_enter_different_mode_return_invalid_input(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('K'), 'Invalid Input!')

    def test_enter_different_mode_return_coins(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('Q, N, COIN-RETURN'), ['Q', 'N'])

    def test_output_product_and_response_with_no_change(self):
        vm = VendingMachine()
        vm._user_input_value = 0.65
        self.assertEqual(vm.output_product_and_response('A'), ['A']) 

    def test_output_product_and_response_with_changes(self):
        vm = VendingMachine()
        vm._user_input_value = 0.75
        self.assertEqual(vm.output_product_and_response('A'), ['A', 'N', 'N']) 

    def test_output_product_and_response_without_enough_input_money(self):
        vm = VendingMachine()
        vm._user_input_value = 0.55
        self.assertEqual(vm.output_product_and_response('A'), ['Don\'t have enough money, please insert $0.10 extra.'])

    def test_convert_number_to_coins_with_exact_matched_coin_value(self):
        vm = VendingMachine()
        self.assertEqual(vm.find_match_coins(0.25), ['Q'])

    def test_convert_number_to_coins_without_exact_matched_coin_value(self):
        vm = VendingMachine()
        self.assertEqual(vm.find_match_coins(0.35), ['Q', 'D'])

    def test_find_match_coins_with_matched_coin_value(self):
        vm = VendingMachine()
        self.assertEqual(vm.find_match_coins(0.35), ['Q', 'D'])

    def test_find_the_largest_available_coin_for_Q(self):
        vm = VendingMachine()
        self.assertEqual(vm.find_the_largest_available_coin(0.65), 'Q')

    def test_find_the_largest_available_coin_for_D(self):
        vm = VendingMachine()
        self.assertEqual(vm.find_the_largest_available_coin(0.1), 'D')


    def test_enter_different_mode_return_item_A_with_no_changes(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('N, D, Q, Q, GET-A'), ['A'])

    def test_enter_different_mode_return_item_A_with_changes(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('Q, Q, Q, Q, GET-A'), ['A', 'Q', 'D'])

    def test_enter_different_mode_return_item_A_with_not_enough_input_money(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('Q, Q, GET-A'), ['Don\'t have enough money, please insert $0.15 extra.'])  

    def test_enter_different_mode_return_item_B_with_no_changes(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('Q, Q, Q, Q, GET-B'), ['B'])

    def test_enter_different_mode_return_item_B_with_changes(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('DOLLAR, Q, GET-B'), ['B', 'Q'])

    def test_enter_different_mode_return_item_C_with_no_changes(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('Q, Q, DOLLAR, GET-C'), ['C'])

    def test_enter_different_mode_return_item_C_with_changes(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('Q, Q, DOLLAR, Q, GET-C'), ['C', 'Q'])

    def test_enter_service_mode(self):
        vm = VendingMachine()
        self.assertEqual(vm.enter_different_mode('SERVICE'), 'Enter Service Mode...')


if __name__ == '__main__':
    unittest.main()