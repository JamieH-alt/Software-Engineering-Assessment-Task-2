import re
from pathlib import Path

def extract_uncommented_classes(file_path: str, output_list_name="items") -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    pattern = re.compile(r"^(\w+)\s*=\s*cs\.(Item|Weapon|Armour)\s*\(")
    active_vars = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        match = pattern.match(stripped)
        if match:
            var_name = match.group(1)
            active_vars.append(var_name)

    # Format the list
    formatted_list = f"{output_list_name} = [\n"
    formatted_list += ",\n".join(f"    {name}" for name in active_vars)
    formatted_list += "\n]"

    return formatted_list


if __name__ == "__main__":
    input_file = "item.py"  # Path to your item definitions
    output = extract_uncommented_classes(input_file)
    print(output)

    # Optional: Save to a separate .py file
    with open("item_list.py", "w", encoding="utf-8") as f:
        f.write("# Auto-generated list of item variables\n\n")
        f.write(output + "\n")
