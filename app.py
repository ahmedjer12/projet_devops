def greet(name):
    """Return a formatted greeting."""
    name = name.strip()

    if not name:
        name = "Guest"

    name = name.title()

    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("DevOps"))