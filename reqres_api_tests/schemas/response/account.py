registerged_successfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"id": {"type": "integer"}, "token": {"type": "string"}},
    "required": ["id", "token"],
}

failed_to_register = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}


logged_in_successfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"token": {"type": "string"}},
    "required": ["token"],
}


failed_to_log_in = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}
