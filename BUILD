load("@subpar//:subpar.bzl", "par_binary")

par_binary(
    name = "app",
    srcs = [":main.py"],
    main = "main.py",
    zip_safe = False,
    deps = ["//foo:libfoo"],
)
