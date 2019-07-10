""" 
program manages bank accounts by dividing them into 
checking, saving, and business accounts.
Also keeps up with credit card statements

"""

class Account:
	def __init__(self, cust_id, total_amount):
		self.cust_id = cust_id
		self.total_amount = total_amount

	def __repr__(self):
		return "{}'s account".format(self.cust_id)


class CheckingAccount(Account):
	
	
	def __repr__(self):
		return "{}'s checking account: ${} available.".format(self.cust_id, self.total_amount)

	def deposit(self, deposit_amount):
		self.total_amount += deposit_amount
		return self.total_amount

	def withdrawal(self, withdrawal_amount):
		if withdrawal_amount <= self.total_amount:
			self.total_amount -= withdrawal_amount
			return self.total_amount 
		else:
			return 'insufficient funds!'

	def get_amount(self):
		return '$' + str(self.total_amount)

	def display_amount(self):
		print(self.total_amount)



class SavingsAccount(Account):


	def __repr__(self):
		return "{}'s savings account: ${} available.".format(self.cust_id, self.total_amount)

	def deposit(self, deposit_amount):
		self.total_amount += deposit_amount
		return self.total_amount

	def withdrawal(self, withdrawal_amount):
		if withdrawal_amount <= self.total_amount:
			self.total_amount -= withdrawal_amount
			return self.total_amount 
		else:
			return 'insufficient funds!'

	def get_amount(self):
		return '$' + str(self.total_amount)

	def display_amount(self):
		print(self.total_amount)



class BusinessAccount(Account):


	def __repr__(self):
		return "{}'s business account: ${} available.".format(self.cust_id, self.total_amount)

	def deposit(self, deposit_amount):
		self.total_amount += deposit_amount
		return self.total_amount

	def withdrawal(self, withdrawal_amount):
		if withdrawal_amount <= self.total_amount:
			self.total_amount -= withdrawal_amount
			return self.total_amount 
		else:
			return 'insufficient funds!'

	def get_amount(self):
		return '$' + str(self.total_amount)

	def display_amount(self):
		print(self.total_amount)


if __name__ == '__main__':
	isSessionOn = True 
	isCustomer = False 

	def initialize_objects():
		global jackson_checking, jackson_savings, jackson_business, master_list



		jackson_checking = CheckingAccount('Jackson', 4100)
		jackson_savings = SavingsAccount('Jackson', 100000)
		jackson_business = BusinessAccount('Jackson', 15000)

        # List that holds the customerID at index 1 and the account type at index 2
		master_list = [[jackson_checking, 1, 1], [jackson_savings, 1, 2], [jackson_business, 1, 3]]


		return None

	initialize_objects()

	while isSessionOn == True:
		print('Welcome to 24-hour ATM service.')
		print('insert your card.')


		# Card reading the customer info representation
		customerID = int(input('Enter your customer id number: '))
		print("\n")


        # Takes in the customer's ID and then adds the accounts they have to cust_accounts
		cust_accounts = []
		for i in master_list:
			if i[1] == customerID:
				cust_accounts.append(i[2])
				isCustomer = True 

		if isCustomer == True:
			isAccountSelected = False 


			while isAccountSelected == False:
				print("Enter 1 for checkings account")
				print("Enter 2 for savings account")
				print("Enter 3 for business account")
				account_type = int(input("Enter which account to use: "))

                # sets the object of which account is selected 
				if account_type in cust_accounts:
					for x in master_list:
						if account_type == x[2]:
							object_name = x[0]

					isAccountSelected = True 
					isAccountSessionOn = True 


					while isAccountSessionOn == True:
						print("\nHow may I help you?")
						print("press 1 for balance view.")
						print("press 2 for withdrawals.")
						print("press 3 to deposit.")
						print("press 4 to exit.")

						action_value = int(input("please enter your choice: "))


						if action_value == 1:
							object_name.display_amount()
							print("\n")

						if action_value == 2:
							amt_to_withdraw = int(input("Enter the amount to withdraw: "))
							
							adjusted_amount = amt_to_withdraw
							object_name.withdrawal(adjusted_amount)

							print("current balance is {}".format(object_name.get_amount()))
							print("\n")

						if action_value == 3:
							amt_to_deposit = int(input("Enter the amount ou would like to deposit: "))

							added_amount = amt_to_deposit
							object_name.deposit(added_amount)

							print("current balance is {}".format(object_name.get_amount()))
							print("\n") 
							
						if action_value == 4:
							isAccountSessionOn = False 
							print("Thank you for using the 24-hour ATM Service.")
							

				else:
					print("Error. you do not have that account.")
					print("please try again.\n")

		else:
			print("cannot find your record.")
			print("Please get your card.")
			print("Closing this session...")


			



















