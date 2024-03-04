from tabulate import tabulate

"""
Membership Requirement Database
---
This Database contain the Income and Expense requirement for each membership tier.

This data is written in this format: 
{Membership Name : (Income Requirement, Expense Requirement)}
"""
membership_requirement = {'Platinum':(15_000_000, 8_000_000),
                          'Gold':(10_000_000, 6_000_000),
                          'Silver': (7_000_000, 5_000_000)
                         }

membership_requirement_table = tabulate(membership_requirement, headers="keys",
                                  tablefmt="github", intfmt=",")
""" 
Membership Benefit Table.
---
This database contain membership benefit table.
This table will have 3 columns headers :
   - Membership Tier
   - Discount 
   - Another Benefit 
"""
membership_benefit_table = [
    ['Membership', 'Discount', 'Another Benefit'],
    ['Platinum', '15%', 'Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%'],
    ['Gold', '10%', 'Benefit Silver + Voucher Ojek Online'],
    ['Silver', '8%', 'Voucher Makanan']
]

membership_benefit_table = tabulate(membership_benefit_table,
                                    headers="firstrow", tablefmt="github")