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

<p style="text-align: center"><img src="https://github.com/hilmyfauzan/PacCommerce/assets/144140564/ae59f048-ba9d-408a-8420-3383ffbcfbec"></p>


 - The system will chose the membership with shortest distance using Eucledian Distance Method




