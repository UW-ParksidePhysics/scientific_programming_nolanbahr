code_snippets = {}

code_snippets["numbers_working"] = "numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5"

code_snippets["numbers_explanation"] = "This works cause numbers is a dictionary, so I can assign values to keys."

code_snippets["other_numbers_not_working"] = "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5"

code_snippets["other_numbers_explanation"] = "This does not work cause the list is empty and i cannot assign to an index that does not exist."

code_snippets["fixed_code"] = "other_numbers = []\nother_numbers.append(-5)\nother_numbers.append(10.5)"

for key in code_snippets:
    print(code_snippets[key])
    print()