import re

exp_code_pattern = re.compile(r"^Dataset,([A-Za-z0-9]*)")
conditions_pattern = re.compile(r"start_conditions([\s\S]*)end_conditions")
data_pattern = re.compile(r"start_data([\s\S]*)end_data")
error_pattern = re.compile(r"start_errors([\s\S]*)end_errors")
unit_pattern = re.compile(r"/[ ]?([\u00BF-\u1FFF\u2C00-\uD7FF\w/.]*)")
variable_pattern = re.compile(r"([=@()A-Za-z0-9_\[\]-]*)/ ")
token_pattern = re.compile(f"([=@()A-Za-z0-9\[\]-]*)")

# TODO: add more patterns
concentration_unit_patterns = [
    r"/M",
    r"/ M",
    r"/mM",
    r"/ mM",
    r"/ μM",
    r"/μM",
    r"/μM",
    r"/ μM",
    r"M",
    r"M",
    r"mM",
    r"mM",
    r"μM",
    r"μM",
    r"μM",
    r"μM",
]

conc_units = [re.compile(x) for x in concentration_unit_patterns]

# TODO: add more patterns
flow_unit_patterns = [
    r"/ μL/h",
    r"/μL/h",
    r"/ μL/h",
    r"/μL/h",
    r"/ µl/h",
    r"/µl/h",
    r"/ µL/h",
    r"μL/h",
    r"μL/h",
    r"μL/h",
    r"μL/h",
    r"µl/h",
    r"µl/h",
    r"µL/h",
]

flow_units = [re.compile(x) for x in flow_unit_patterns]


# TODO: add more patterns
time_unit_patterns = [
    r"/ s",
    r"/s",
    r"/ min.",
    r"/min.",
    r"/ h",
    r"/h",
    "s",
    r"s",
    r"min.",
    r"min.",
    r"h",
    r"h",
]

time_units = [re.compile(x) for x in flow_unit_patterns]
