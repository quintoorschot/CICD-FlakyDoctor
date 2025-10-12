import javalang

def helper(java_src: str):
    tree = javalang.parse.parse(java_src)
    package_name = tree.package.name if tree.package else ""

    tests = []
    for _, class_decl in tree.filter(javalang.tree.ClassDeclaration):
        class_name = class_decl.name
        for method in class_decl.methods:
            if any(a.name == "Test" or a.name.endswith(".Test") for a in method.annotations or []):
                full_name = f"{package_name}.{class_name}.{method.name}" if package_name else f"{class_name}.{method.name}"
                tests.append(full_name)
    return tests


def get_test_names(file_path: str):
    """Return list of fully qualified @Test method names from a Java file."""
    with open(file_path, "r", encoding="utf-8") as f:
        java_src = f.read()
    return helper(java_src)


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    for name in get_test_names(path):
        print(name)
