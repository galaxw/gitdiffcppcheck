
filegroup(
    name = "diff_python_files",
    srcs = glob([
        "diff/*.py",
    ]),
)

py_library(
    name = "git_diff_lib",
    srcs = [
        ":diff_python_files",
    ],
    visibility = ["//visibility:public"],
)

filegroup(
    name = "cppcheck_report_python_files",
    srcs = glob([
        "cppcheck/*.py",
    ]),
)

py_library(
    name = "cppcheck_report_lib",
    srcs = [
        ":cppcheck_report_python_files",
    ],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "diffcppcheck",
    main = "main.py",
    srcs = ["main.py"],
    deps = [
        ":git_diff_lib",
        ":cppcheck_report_lib",
    ],
    data = [
        "logging.config",
    ],
)
