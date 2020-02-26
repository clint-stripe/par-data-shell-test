workspace(name = "pypkgtar")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_pkg",
    url = "https://github.com/bazelbuild/rules_pkg/releases/download/0.2.4/rules_pkg-0.2.4.tar.gz",
    sha256 = "4ba8f4ab0ff85f2484287ab06c0d871dcb31cc54d439457d28fd4ae14b18450a",
)

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz",
    sha256 = "aa96a691d3a8177f3215b14b0edc9641787abaaa30363a080165d06ab65e1161",
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "dc97fccceacd4c6be14e800b2a00693d5e8d07f69ee187babfd04a80a9f8e250",
    strip_prefix = "rules_docker-0.14.1",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.14.1/rules_docker-v0.14.1.tar.gz"],
)
load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)
container_repositories()
load("@io_bazel_rules_docker//python3:image.bzl", _py_image_repos = "repositories")
_py_image_repos()