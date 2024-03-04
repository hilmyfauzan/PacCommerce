from module import (
    euclidean_distance, membership_discount, convert
)
from database import (
    membership_requirement,
    membership_benefit_table,
    membership_requirement_table
)

class Membership:
    def __init__(self, username:str, 
                 monthly_expense:float=None, monthly_income:float=None) -> None:
        """
        Initialize all the necessary parameter for Membership instance.

        Parameters
        ----------
        username : str
        monthly_expense : float, optional
            user monthly expense in PacCommerce, by default None
        monthly_income : float, optional
            user monthly top up in PacCommerce, by default None
        """
        self.username = username
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income
        self.membership = None
    
    def show_benefit(self):
        """
        This function will show Membership Benefit Table.

        Membership Benefit Table will contain information regarding :
        - Discount for each Membership Tier
        - Another Benefit for each Membership Tier
        """
        # Shows all membership benefit
        print(membership_benefit_table)

    def show_requirements(self):
        """
        This Function will show the membership_requirement_table.
        
        The membership_requirement_table contain : 
           - the required monthly income
           - and monthly expense for each membership tier
        """
        # Show all membership plan requirement
        print(membership_requirement_table)

    def predict_membership(self):
        """
        This function will predict the user membership using distance based method.
        
        This function will calculate the distance using
        Eucledian Distance Method between :
           - User monthly expense and income
           - Membership required monthly expense and income

        The user membership tier is choosen based on which tier have the closest
        distance.
        """
        # Predict user membership using euclidean distance
        membership = euclidean_distance(self.monthly_income,
                                        self.monthly_expense,
                                        membership_requirement)
        print(f'Hi {self.username}')
        print(f"Based on your income and expense, "
              f"you're eligible for {membership} Membership")
        
        self.membership = membership

    def calculate_price(self, shopping_price_list:list):
        """Displaying the price based on membership status.

        Parameters
        ----------
        shopping_price_list : list
            list of price in shopping cart
        """
        # Sum all the price in shopping_price_list
        total_original_price = sum(shopping_price_list)
        # Checking the final price based on membership
        final_price = membership_discount(total_original_price, self.membership)
        # Shows the final_price on the screen
        print(convert(final_price))
