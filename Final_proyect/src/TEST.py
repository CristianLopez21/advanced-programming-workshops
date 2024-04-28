"This file is used to call al the methods of the other classes "

from users import User, Customer, Admin

User.create_account()
Customer.test_costumers_integrity(Customer)
#User.create_account()
#Admin.test_admins_integrity(Admin)
Customer.add_shipping_address(Customer,user_email="cslc@gmail.com")
