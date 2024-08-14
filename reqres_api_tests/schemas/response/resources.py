resources_list_retrieved = {
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
                    "name": {"type": "string"},
                    "year": {"type": "integer"},
                    "color": {"type": "string"},
                    "pantone_value": {"type": "string"},
                },
                "required": ["id", "name", "year", "color", "pantone_value"],
            },
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"},
            },
            "required": ["url", "text"],
        },
    },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"],
}

single_resource_info_retrieved = {
    "type": "object",
    'additionalProperties': False,
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "color": {"type": "string"},
                "pantone_value": {"type": "string"},
            },
            "required": ["id", "name", "year", "color", "pantone_value"],
        },
        "support": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "text": {"type": "string"}},
            "required": ["url", "text"],
        },
    },
    "required": ["data", "support"],
}
