class BalancedSmileys:
    result_table = {}

    def __init__(self, messages: list[str]):
        self.messages = messages

    def is_balanced(self):
        for i, message in enumerate(self.messages):
            if self.is_balanced_message(message):
                self.result_table[i] = "YES"
            else:
                self.result_table[i] = "NO"

    def is_balanced_message(self, message):
        allowed_chars = set('abcdefghijklmnopqrstuvwxyz :()')
        

        if message == "":
            return True
        
        # sprawdza czy są tylko dozwolone znaki
        if not all(char in allowed_chars for char in message):
            return False
        
        # sprawdza czy jest tyle samo otwierających i zamykających nawiasów
        if message.count("(") != message.count(")"):
             if message[message.find("(") - 1] != ":" and message[message.find(")") - 1] != ":":
                  return False
             else:
                  return True
             
        # sprawdza czy jest otwierający nawias przed zamykającym
        if message.count("(") != 0:
            if "(" in message and ")" in message[message.find("(") + 1 :]:
                    return True
            else:
                if message[message.find("(") - 1] != ":" and message[message.find(")") - 1] != ":":
                    return False
        return True

    def get_result_table(self):
        return self.result_table 