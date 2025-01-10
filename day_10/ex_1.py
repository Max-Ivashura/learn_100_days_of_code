# Functions with Outputs


def format_name(f_name, l_name):
    """Take a first and last name and format it to return the tittle case version of the name.

    Args:
        f_name (str): first name
        l_name (str): last name

    Returns:
        str: Formatted first and last name
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(
    format_name(input("What is your first name?\n"), input("What is your last name?\n"))
)
