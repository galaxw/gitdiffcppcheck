filegroup(
    name = "test_data",
    srcs = glob([
        "data/*.xml",
    ]),
)


py_test(
    name = "test_cppcheck_report",
    main = "main.py",
    srcs = [
        "main.py",
        "test_cppcheck_report.py",
    ],
    deps = [
        "//diffcppcheck:cppcheck_report_lib",
    ],
    data = [
        ":test_data",
    ],
    args = [
        "--junitxml=$${XML_OUTPUT_FILE}",
        "."
    ],
)
