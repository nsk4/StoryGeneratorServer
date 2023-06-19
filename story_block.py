class StoryBlock:
    def __init__(self, role, text, options) -> None:
        self.role = role
        self.text = text
        self.options = options

# TODO: add user response to the block itself
#    def select_option(self, option_number):
#        if option_number < len(self.options):
#            self.select_option = option_number
#        else:
#            print("Invalid option selected")