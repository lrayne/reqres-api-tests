register_successfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"id": {"type": "integer"}, "token": {"type": "string"}},
    "required": ["id", "token"],
}

register_unsuccessfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}


login_successfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"token": {"type": "string"}},
    "required": ["token"],
}


login_unsuccessfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}