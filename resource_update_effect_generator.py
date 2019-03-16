# Use this script to quickly generate a set of scripted effects
# These are used to update variables in states when resources change in them

resources = [
    "wood",
    "coal",
    "cotton",
    "fabric",
    "iron",
    "steel",
    "rubber",
    "oil",
    "plastics",
    "aluminium",
    "tungsten",
    "chromium",
    "titanium",
    "silicates",
    "ceramics",
    "machine_parts",
    "rare_earth_metals",
    "eletronics",
    "portable_power"
    ]

for resource in resources:
    print(
        "update_"+resource+" = {\n"
        "   add_to_variable = { "+resource+" = amt }\n"
        "   if = {\n"
        "      limit = {\n"
        "            # Check if it exists, and if not then create it\n"
        "            NOT = {has_variable = "+resource+"}\n"
        "      }\n"
        "      set_variable = { "+resource+" = amt }\n"
        "   }\n"
        "   clear_variable = amt\n"
        "}\n"
    )
