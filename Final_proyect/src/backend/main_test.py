"This file is used to call al the methods of the other classes "

from .n_class import users

#User.create_account()
#Customer.test_costumers_integrity(Customer)
users.User.create_admin()
users.Admin.test_admins_integrity(users.Admin)
users.Admin.add_product(users.Admin, True)
