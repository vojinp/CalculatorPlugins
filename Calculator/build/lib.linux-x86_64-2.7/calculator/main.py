import pkg_resources

def load_plugins(tag):
    plugins = {}

    for ep in pkg_resources.iter_entry_points(group=tag):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()

        plugins[plugin.identifier()] = plugin

    return plugins

print("ASD")
# visualizer_parser = load_plugins("visualizer")
print(pkg_resources.iter_entry_points)