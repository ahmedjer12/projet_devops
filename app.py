def greet(name):
    name = name.strip()

    if not name:
        name = "Guest"

    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("DevOps"))