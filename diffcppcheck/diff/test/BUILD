filegroup(
    name = "test_data",
    srcs = glob([
        "data/*.diff",
    ]),
)


py_test(
    name = "test_diff",
    main = "main.py",
    srcs = [
        "main.py",
        "test_diff.py",
    ],
    deps = [
        "//diffcppcheck:git_diff_lib",
    ],
    data = [
        ":test_data",
    ],
    args = [
        "--junitxml=$${XML_OUTPUT_FILE}",
        "."
    ],
)
