users_list_retrieved = {
    "type": "object",
    'additionalProperties': False,
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"},
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"],
            },
        },
        "support": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "text": {"type": "string"}},
            "required": ["url", "text"],
        },
    },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"],
}

single_user_info_retrieved = {
    "type": "object",
    'additionalProperties': False,
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"},
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"],
        },
        "support": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "text": {"type": "string"}},
            "required": ["url", "text"],
        },
    },
    "required": ["data", "support"],
}

user_created = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["id", "createdAt"],
}


user_updated = {
    "type": "object",
    'additionalProperties': False,
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "required": ["job", "updatedAt"],
}
