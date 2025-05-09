APP_ITEM_JSON_SCHEMA = {
    'type': 'object',
    'properties': {
        'categories': {
            'type': 'array',
            'items': {'type': 'string'},
        },
        'tags': {
            'type': 'array',
            'items': {'type': 'string'},
        },
        'screenshots': {
            'type': 'array',
            'items': {'type': 'string'},
        },
        'icon_url': {'type': 'string'},
    },
    'required': ['categories'],
}

APP_CAPABILITIES_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'description': {'type': 'string'},
            'name': {'type': 'string'},
        },
        'required': ['description', 'name'],
    },
}

APP_RUN_AS_CONTEXT_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'description': {'type': 'string'},
            'gid': {'type': 'integer'},
            'group_name': {'type': 'string'},
            'user_name': {'type': 'string'},
            'uid': {'type': 'integer'},
        },
        'required': ['description'],
    },
}

APP_METADATA_JSON_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'train': {'type': 'string'},
        'description': {'type': 'string'},
        'home': {'type': 'string'},
        'chagelog_url': {'type': 'string'},
        'date_added': {
            'type': 'string',
            'pattern': '20[0-9]{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])',
        },
        'app_version': {'type': 'string'},
        'annotations': {
            'type': 'object',
            'properties': {
                'min_scale_version': {'type': 'string'},
                'max_scale_version': {'type': 'string'},
            },
        },
        'title': {'type': 'string'},
        'sources': {
            'type': 'array',
            'items': {'type': 'string'},
        },
        'maintainers': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'url': {'type': 'string'},
                },
                'required': ['name', 'email'],
            },
        },
        'keywords': {
            'type': 'array',
            'items': {'type': 'string'},
        },
        'version': {
            'type': 'string',
            'pattern': '[0-9]+.[0-9]+.[0-9]+',
        },
        'lib_version': {
            'type': 'string',
            'pattern': '[0-9]+.[0-9]+.[0-9]+',
        },
        'lib_version_hash': {'type': 'string'},
        'run_as_context': APP_RUN_AS_CONTEXT_SCHEMA,
        'capabilities': APP_CAPABILITIES_SCHEMA,
        'host_mounts': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'description': {'type': 'string'},
                    'host_path': {'type': 'string'},
                },
                'required': ['description', 'host_path'],
            },
        },
        'screenshots': {
            'type': 'array',
            'items': {'type': 'string'},
        },
        'categories': {
            'type': 'array',
            'items': {'type': 'string'},
        },
    },
    'required': [
        'name', 'train', 'version', 'app_version', 'title', 'description', 'home',
        'sources', 'maintainers', 'run_as_context', 'capabilities', 'host_mounts',
    ],
    'if': {
        'properties': {
            'lib_version': {'type': 'string'},
        },
        'required': ['lib_version'],
    },
    'then': {
        'required': ['lib_version_hash'],
    },
}
APP_MIGRATION_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'app_name': {'type': 'string'},
            'action': {'type': 'string', 'enum': ['move']},
        },
        'required': [
            'app_name',
            'action'
        ],
        'allOf': [
            {
                'if': {
                    'properties': {
                        'action': {
                            'const': 'move',
                        },
                    },
                },
                'then': {
                    'properties': {
                        'old_train': {'type': 'string'},
                        'new_train': {'type': 'string'},
                    },
                    'required': [
                        'new_train',
                        'old_train',
                    ],
                },
            },
        ],
    },
}
BASE_LIBRARIES_JSON_SCHEMA = {
    'type': 'object',
    'patternProperties': {
        '[0-9]+.[0-9]+.[0-9]+': {
            'type': 'string',
        },
    },
}
CATALOG_JSON_SCHEMA = {
    'type': 'object',
    'patternProperties': {
        '.*': {
            'type': 'object',
            'title': 'Train',
            'patternProperties': {
                '.*': {
                    'type': 'object',
                    'title': 'Item',
                    'properties': {
                        'name': {
                            'type': 'string',
                            'title': 'Name',
                        },
                        'categories': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            },
                        },
                        'app_readme': {
                            'type': 'string',
                        },
                        'location': {
                            'type': 'string',
                        },
                        'healthy': {
                            'type': 'boolean',
                        },
                        'healthy_error': {
                            'type': ['string', 'null'],
                        },
                        'last_update': {
                            'type': 'string',
                            'pattern': r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$',
                        },
                        'latest_version': {
                            'type': 'string',
                        },
                        'latest_app_version': {
                            'type': 'string',
                        },
                        'latest_human_version': {
                            'type': 'string',
                        },
                        'description': {
                            'type': ['string', 'null'],
                        },
                        'title': {
                            'type': 'string',
                        },
                        'icon_url': {
                            'type': ['string', 'null'],
                        },
                        'run_as_context': APP_RUN_AS_CONTEXT_SCHEMA,
                        'capabilities': APP_CAPABILITIES_SCHEMA,
                        'maintainers': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                    'url': {'type': ['string', 'null']},
                                    'email': {'type': 'string'}
                                },
                                'required': ['name', 'email'],
                            }
                        },
                        'home': {
                            'type': 'string',
                        },
                        'tags': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                            }
                        },
                        'screenshots': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                            }
                        },
                        'sources': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                            }
                        },
                    },
                    'required': [
                        'name', 'categories', 'location', 'healthy', 'icon_url',
                        'latest_version', 'latest_app_version', 'latest_human_version',
                        'last_update', 'recommended', 'healthy_error', 'maintainers',
                        'home', 'tags', 'sources', 'screenshots',
                    ],
                }
            }

        }
    }
}
RECOMMENDED_APPS_JSON_SCHEMA = {
    'type': 'object',
    'patternProperties': {
        '.*': {
            'type': 'array',
            'items': {'type': 'string'},
        }
    },
}
VERSION_VALIDATION_SCHEMA = {
    'type': 'object',
    'title': 'Versions',
    'patternProperties': {
        '[0-9]+.[0-9]+.[0-9]+': {
            'type': 'object',
            'properties': {
                'healthy': {
                    'type': 'boolean',
                },
                'supported': {
                    'type': 'boolean',
                },
                'healthy_error': {
                    'type': ['string', 'null']
                },
                'location': {
                    'type': 'string',
                    'pattern': r'^(\/[a-zA-Z0-9_.-]+)+$'
                },
                'last_update': {
                    'type': 'string',
                    'pattern': '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$'
                },
                'required_features': {
                    'type': 'array',
                    'items': {
                        'type': 'string'
                    }
                },
                'human_version': {
                    'type': 'string'
                },
                'version': {
                    'type': 'string',
                    'pattern': '[0-9]+.[0-9]+.[0-9]+'
                },
                'app_metadata': APP_METADATA_JSON_SCHEMA,
                'chart_metadata': APP_METADATA_JSON_SCHEMA,
                'readme': {'type': ['string', 'null']},
                'changelog': {'type': ['string', 'null']},
                'schema': {
                    'type': 'object',
                    'properties': {
                        'groups': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'name': {
                                        'type': 'string'
                                    },
                                    'description': {
                                        'type': 'string'
                                    },
                                },
                                'required': ['description', 'name'],
                            }
                        },
                        'portals': {
                            'type': 'object'
                        },
                        'questions': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'variable': {'type': 'string'},
                                    'label': {'type': 'string'},
                                    'group': {'type': 'string'},
                                    'schema': {
                                        'type': 'object',
                                        'properties': {
                                            'type': {'type': 'string'}
                                        },
                                        'required': ['type']
                                    }
                                }
                            }
                        }
                    },
                    'required': ['groups', 'questions']
                },
            },
            'required': [
                'healthy', 'supported', 'healthy_error', 'location', 'last_update', 'required_features',
                'human_version', 'version', 'app_metadata', 'schema', 'readme', 'changelog',
            ],
        },
    },
    'additionalProperties': False
}  # FIXME: See if all keys port
APP_CONFIG_MIGRATIONS_SCHEMA = {
    'type': 'object',
    'properties': {
        'migrations': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'file': {'type': 'string'},
                    'from': {
                        'type': 'object',
                        'properties': {
                            'min_version': {'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'},
                            'max_version': {'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'}
                        },
                        'additionalProperties': True,
                    },
                    'target': {
                        'type': 'object',
                        'properties': {
                            'min_version': {'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'},
                            'max_version': {'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'}
                        },
                        'additionalProperties': True,
                    }
                },
                'required': ['file'],
                'additionalProperties': True,
            }
        }
    },
    'required': ['migrations'],
}
