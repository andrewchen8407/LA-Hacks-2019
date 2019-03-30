import data


def set_balance(pin, amount):
    if pin in data.account_dict:
        data.account_dict[pin] = (data.account_dict[pin][0], amount)
    else:
        print("Wrong ID")
