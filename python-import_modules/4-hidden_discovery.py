#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util

    module_path = "/tmp/hidden_4.pyc"

    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)

