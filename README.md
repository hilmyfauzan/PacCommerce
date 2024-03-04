# **PacCommerce - CLI Customer Membership Project**

## **Case Description**
#### **General Description**
- This project is done as a project for Lecture 8 on Introduction to Python for Software Engineering at Pacmann Academy

- PacCommerce is an e-commerce service

- There are Membership Tier feature in PacCommerce :
    - Platinum
    - Gold
    - Silver

- Each tier have different perks and benefits.

    | Membership   | Discount   | Another Benefit                                             |
    |--------------|------------|-------------------------------------------------------------|
    | Platinum     | 15%        | Benefit Silver + Gold + Voucher Liburan + Cashback max. 30% |
    | Gold         | 10%        | Benefit Silver + Voucher Ojek Online                        |
    | Silver       | 8%         | Voucher Makanan                                             |

#### **Membership Prediction System**
- PacCommerce want to develop a sytem to predict which membership tier an user is eligible to

- Each membership tier have a requirement based on :
    - User Monthly Expense
    - User Monthly Income

      |   Platinum        |       Gold        |    Silver        |
      |-------------------|-------------------|------------------|
      | IDR 15,000,000.00 | IDR 10,000,000.00 | IDR 7,000,000.00 |
      |  IDR 8,000,000.00 | IDR 6,000,000.00  | IDR 5,000,000.00 |

- PacCommerce need the user Monthly Expense and Income data to as a base for its prediction system

- To predict the user membership tier, PacCommerce will use a system using distance based method

- The way it works is by measuring the distance between :
    - User current monthly expense and income
    - Monthly expense and income requirement of each tier

<p align="center">
  <img src="https://github.com/hilmyfauzan/PacCommerce/assets/144140564/ae59f048-ba9d-408a-8420-3383ffbcfbecraw=true" alt="Distance Based Membership Prediction System"/>"
</p>

<p align="center"><b>Image 1.</b> Distance Based Membership Prediction System</p>

 - The system will chose the membership with shortest distance using Eucledian Distance Method
 
 - Here is the eucledian distance formula for the membership prediction system :

   ### $r_{user-membership} = \sqrt{(expense_{user} - expense_{membership})^2 + (income_{user} - income_{membership})^2}$

   - $r_user-membership$ : Eucledian distance between user current monthly income and expense and membership requirement
   - $expense_user$ : User monthly expense in PacCommerce
   - $expense_membership$ : Monthly expense requirement for spesific membership tier
   - $income_user$ : User monthly total top-up in PacCommerce
   - $income_membership$ : Monthly total top-up requirement for spesific membership tier

## **File Description**
- main.py : This is where the main program is being developed
- module.py : This is a library to store all supporting function for the main program
- database.py : This is a library to store all supporting database for the main program
- study_case.ipynb : This is a study case to test if the main program is working properly


