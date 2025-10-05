def flatten_menu(node):
    """
    Recursively flatten a menu structure into a list of item names.
    Only 'item' nodes with a 'name' are included.
    'category' nodes are traversed to collect items from their children.
    Any other types or malformed nodes are ignored.
    """
    if not isinstance(node, dict) or "type" not in node:
        return []

    node_type = node["type"]

    if node_type == "item":
        return [node["name"]] if "name" in node else []

    elif node_type == "category":
        result = []
        for child in node.get("children", []):
            result.extend(flatten_menu(child))
        return result

    # ignore unknown types
    return []
