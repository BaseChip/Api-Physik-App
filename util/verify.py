import re


class Verify:
    # überprüft, ob der übergebene String dem typischen email Format entspricht (xxx@xxx.xxx)
    def email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False