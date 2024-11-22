START = \
"""
Assalomu alaykum 
"""

PASSENGER_HANDLER = \
"""
Hurmatli mijoz yolovchilar sonini kriting
"""

LOCATION = \
"""
Qayerga bormoqchisiz!
"""

PHONE = \
"""
ILTIMOS telefon raqamingizni yozib yuboring yoki pasatdagi telefon raqam yuborish tugmasini bosing
"""
MAIL_HANDELR = \
    """
    Qayerga yubormochisiz ?
    """
driver_handler = \
    """
    Ismingizni kiriting
    """
    


def check(**kwargs):
    passenger = ''

    passenger += f"malumot:\n"
    passenger += f"yolovchi soni:{kwargs['count']}\n"
    passenger += f"manzil:{kwargs['location']}\n"
    passenger += f"telefon:{kwargs['phone']}\n"


    return passenger


def send_gruop(**kwargs):
    passenger = ''

    passenger += f"malumot:\n"
    passenger += f"yolovchi soni:{kwargs['count']}\n"
    passenger += f"manzil:{kwargs['location']}\n"
    passenger += f"telefon:{kwargs['phone']}\n"
    passenger += f"username:{kwargs['username']}\n"


    return passenger

def send_mail(**kwargs):
    passenger = ''

    passenger += f"malumot:\n"
    passenger += f"manzil:{kwargs['location']}\n"
    passenger += f"telefon:{kwargs['phone']}\n"

    return passenger


def send_driver(**kwargs):
    passenger = ''

    passenger += f"malumot:\n"
    passenger += f"name:{kwargs['name']}\n"
    passenger += f"telefon:{kwargs['phone']}\n"



    return passenger