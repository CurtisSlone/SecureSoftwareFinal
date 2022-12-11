from flask_login import UserMixin
class UserModel(UserMixin):
    """
    
    """
    def __init__(self,serial,dn,ou):
        """
        Constructor
        """
        id = serial
        distinguishedName = dn
        organizationalUnit = ou