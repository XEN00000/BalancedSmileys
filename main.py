from BalancedSmileys_lib import BalancedSmileys

messages = []
messages.append(input(f"Case #{len(messages) + 1}: "))


while messages[-1] != "exit":
    messages.append(input(f"Case #{len(messages) + 1}: "))
    if messages[-1] == "exit":
        messages.pop()
        break


# Test cases
#messages = [":(", 
#            ":)", 
#            "hello", 
#            "HELLO", 
#            "HELLO:",
#            "(:)", 
#            "()()", 
#            "(())",
#            "((",
#            "())"]

print("\n")

balanced_smileys = BalancedSmileys(messages)
balanced_smileys.is_balanced()
result = balanced_smileys.get_result_table()

for key, value in result.items():
    print(f"Case #{key + 1}: {value}")
