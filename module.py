def euclidean_distance(monthly_income:float, 
                       monthly_expense:float, 
                       target_coordinate:list) -> str:
    """
    Calculate the Eucledian Distance between membership to predict 
    which one is the closest membership that the user will get.

       The program will calculate the shortest distance between :
          - Current Coordinate    : user monthly income, monthly expense
          - Membership Coordinate : membership income, expense requirement.

    Parameters
    ----------
    monthly_income : float
        User monthly income
    monthly_expense : float
        User monthly expense
    target_coordinate : list
        List of membership income and expense requirement

    Returns
    -------
    smallest_distance_membership : str
        The predicted user membership 
        (The membership with shorthest Eucledian Distance)
    """
    # Create an empty dict to store all the distance
    distances = {}
    # Calculate user input coordinate with target coordinate
    for membership, coordinate in target_coordinate.items():
        # Caculate the Eucledian Distance
        dist =  (monthly_income-coordinate[0])**2 + (monthly_expense-coordinate[1])**2
        dist = round(dist**0.5, 2)
        # Store the distance and the membership name in distances dictionary.
        distances.update({dist:membership.title()})
    # Find the smallest distance between all those target coordinate
    smallest_distance_membership = distances[min(distances.keys())]
    # Return the smallest distance
    return smallest_distance_membership

def membership_discount(price:float, membership:str) -> float:
    """Calculating the price based on membership.
       
       Platinum Membership  : Discount 15%
       Gold Membership      : Discount 10%
       Silver Membership    : Discount  8%

    Parameters
    ----------
    price : float
    membership : str

    Returns
    -------
    final_price : float
        The final price after being discounted based on membership tier.
    """
    # Calculating the price based on the membership
    match membership.lower():
        # if platinum, discount 15%
        case 'platinum': final_price = price * 0.85
        # if gold, discount 10%
        case 'gold': final_price = price * 0.9
        # if silver, discount 8%
        case 'silver': final_price = price * 0.92
    
    return round(final_price,2)

def convert(price:float)->str:
    """
    convert float into a currency styled string

    Parameters
    ----------
    price : float
        any numbers of IDR currency

    Returns
    -------
    price : str
        the numbers of IDR currency already in format Rp. x,xxx,xxx.xx
    """
    price = f'{price:,.2f}'
    price = price.replace('.','`').replace(',','.').replace('`', ',')
    return f'Rp. {price}'