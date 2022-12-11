from flask_login import UserMixin
class UserModel(UserMixin):
    """
    
    """
    def __init__(self,dn,ou):
        """
        Constructor
        """
        distinguishedName = dn
        organizationalUnit = ou