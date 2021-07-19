
class Router:
    """
    this exercise if for testing some information from the DEVNET exam, this is a valid reference for the safari book
    """
    def __init__(self,model,ip,version):
        self.model=model
        self.ip=ip
        self.version=version

    def getdes(self):
        """
        this return the descrition of the model
        """
        description= f'Router Model \t:{self.model}\n'\
                     f'Router version\t:{self.version}\n'\
                     f'Router IP address\t:{self.ip}\n'
        return description

class Switch(Router):
    def getdes(self):
         """
         this exercise is for heritage into class
         :return:
         """

         description = f'switch Model \t:{self.model}\n' \
                       f'switch version\t:{self.version}\n' \
                       f'switch IP address\t:{self.ip}\n'
         return description


