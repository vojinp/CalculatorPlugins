import pkg_resources


def load_plugins(tag):
    plugins = {}

    for ep in pkg_resources.iter_entry_points(tag):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()

        plugins[plugin.get_identifier()] = plugin

    return plugins


if __name__ == "__main__":
    plugins = load_plugins("operation")

    print(plugins['addition'].execute(3, 2))
    print(plugins['subtraction'].execute(3, 2))
