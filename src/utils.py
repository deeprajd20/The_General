from datetime import datetime


def formatted_date():
    now = datetime.now()
    formatted = now.strftime("%Y_%m_%d__%H_%M_%S")

    return formatted
