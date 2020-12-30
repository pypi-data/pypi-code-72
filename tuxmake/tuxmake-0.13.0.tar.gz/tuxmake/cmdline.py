import argparse
from pathlib import Path
import re

from tuxmake.utils import supported, defaults
from tuxmake import __version__


def key_value(s):
    parts = s.split("=")
    return (parts[0], "=".join(parts[1:]))


def abspath(path):
    return Path(path).absolute()


def build_parser(cls=argparse.ArgumentParser, **kwargs):
    parser = cls(
        prog="tuxmake",
        usage="%(prog)s [OPTIONS] [VAR=VALUE...] [target ...]",
        description="TuxMake is a python utility that provides portable and repeatable Linux kernel builds across a variety of architectures, toolchains, kernel configurations, and make targets.",
        add_help=False,
        **kwargs,
    )

    positional = parser.add_argument_group("Positional arguments")
    positional.add_argument(
        "targets",
        metavar="[KEY=VALUE | target] ...",
        nargs="*",
        type=str,
        help=f"Make variables to use and targets to build. If no targets are specified, tuxmake will build  {' + '.join(defaults.targets)}. Supported targets: {', '.join(supported.targets)}.",
    )

    build_input = parser.add_argument_group("Build input options")
    build_input.add_argument(
        "-C",
        "--directory",
        dest="tree",
        default=".",
        help="Tree to build (default: .).",
    )

    build_output = parser.add_argument_group("Output options")
    build_output.add_argument(
        "-o",
        "--output-dir",
        type=abspath,
        default=None,
        help="Output directory for artifacts.",
    )
    build_output.add_argument(
        "-b",
        "--build-dir",
        type=abspath,
        default=None,
        help="Build directory. For incremental builds, specify the same directory on subsequential builds (default: temporary, clean directory).",
    )

    target = parser.add_argument_group("Build output options")
    target.add_argument(
        "-a",
        "--target-arch",
        type=str,
        help=f"Architecture to build the kernel for. Default: host architecture. Supported: {(', '.join(supported.architectures))}.",
    )
    target.add_argument(
        "-k",
        "--kconfig",
        type=str,
        help=f"kconfig to use. Named (defconfig etc), path to a local config file, or URL to config file (default: {defaults.kconfig}).",
    )
    target.add_argument(
        "-K",
        "--kconfig-add",
        type=str,
        action="append",
        help="Extra kconfig fragments, merged on top of the main kconfig from --kconfig. In tree configuration fragment (e.g. `kvm_guest.config`), path to local file, URL, `CONFIG_*=[y|m|n]`, or `# CONFIG_* is not set`. Can be specified multiple times, and will be merged in the order given.",
    )

    buildenv = parser.add_argument_group("Build environment options")
    buildenv.add_argument(
        "-t",
        "--toolchain",
        type=str,
        help=f"Toolchain to use in the build. Default: none (use whatever Linux uses by default). Supported: {', '.join(supported.toolchains)}; request specific versions by appending \"-N\" (e.g. gcc-10, clang-9).",
    )
    buildenv.add_argument(
        "-w",
        "--wrapper",
        type=str,
        help=f"Compiler wrapper to use in the build. Default: none. Supported: {', '.join(supported.wrappers)}. When used with containers, either the wrapper binary must be available in the container image, OR you can pass --wrapper=/path/to/WRAPPER and WRAPPER will be bind mounted in /usr/local/bin inside the container (for this to work WRAPPER needs to be a static binary, or have its shared library dependencies available inside the container).",
    )
    buildenv.add_argument(
        "-e",
        "--environment",
        type=key_value,
        action="append",
        help="Set environment variables for the build. Format: KEY=VALUE .",
    )
    buildenv.add_argument(
        "-j",
        "--jobs",
        type=int,
        help=f"Number of concurrent jobs to run when building (default: {defaults.jobs}).",
    )
    buildenv.add_argument(
        "-r",
        "--runtime",
        help=f"Runtime to use for the builds. By default, builds are run natively on the build host. Supported: {', '.join(supported.runtimes)}.",
    )
    buildenv.add_argument(
        "-i",
        "--image",
        help="Image to build with, for container-based runtimes (docker, podman etc). {toolchain} and {arch} get replaced by the names of the toolchain and architecture selected for the build. Implies --runtime=docker if no runtime is explicit specified. (default: tuxmake-provided images).",
    )
    buildenv.add_argument("--docker-image", help="Alias for --image (deprecated).")
    buildenv.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Do a verbose build (default: silent build).",
    )
    buildenv.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Quiet build: only errors messages, if any (default: no).",
    )

    info = parser.add_argument_group("Informational options")
    info.add_argument("-h", "--help", action="help", help="Show program help.")
    info.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    info.add_argument(
        "-A",
        "--list-architectures",
        action="store_true",
        help="List supported architectures and exit.",
    )
    info.add_argument(
        "-T",
        "--list-toolchains",
        action="store_true",
        help="List supported toolchains and exit. Combine with --runtime to list toolchains supported by that particular runtime.",
    )
    info.add_argument(
        "-R",
        "--list-runtimes",
        action="store_true",
        help="List supported runtimes and exit.",
    )
    info.add_argument(
        "-p",
        "--print-support-matrix",
        action="store_true",
        help="Print support matrix (architectures x toolchains). Combine with --runtime to list support matrix for that particular runtime.",
    )
    info.add_argument(
        "-c",
        "--color",
        type=str,
        default="auto",
        choices=["always", "never", "auto"],
        help="Control use of colored output. `always` and `never` do what you expect; `auto` (the default) outputs colors when stdout is a tty.",
    )

    debug = parser.add_argument_group("Debugging options")
    debug.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Provides extra output on stderr for debugging tuxmake itself. This output will not appear in the build log.",
    )
    debug.add_argument(
        "-s",
        "--shell",
        action="store_true",
        help="Opens a shell in the runtime after the build, regardless of its result, for debugging.",
    )
    return parser


class Option:
    def __init__(self, key, opt, **kwargs):
        self.key = key
        self.opt = opt
        self.type = kwargs.get("type", None)
        self.action = kwargs.get("action", None)

    def expand(self, value):
        if self.action == "store_true":
            return [self.opt]

        if self.key == "environment":
            values = value.items()

            def f(a):
                return f"{a[0]}={a[1]}"

        else:

            def f(a):
                return a

            if self.action == "append":
                values = value
            else:
                values = [value]
        return [f"{self.opt}={f(v)}" for v in values]


class ReverseParser:
    def __init__(self, **kwargs):
        self.options = []

    def add_argument_group(self, name):
        return self

    def add_argument(self, *args, **kwargs):
        if len(args) == 1:
            opt = args[0]
        else:
            opt = args[1]
        key = re.sub(r"^--", "", opt)
        key = re.sub("-", "_", key)
        self.options.append(Option(key, opt, **kwargs))


class CommandLine:
    ignore = ["targets", "jobs", "output_dir", "build_dir"]

    def __init__(self):
        self.parser = build_parser(cls=ReverseParser)

    def reproduce(self, build):
        cmd = ["tuxmake"]
        for option in self.parser.options:
            if option.key in self.ignore:
                continue
            if hasattr(build, option.key):
                value = getattr(build, option.key)
                if not value:
                    continue
                for c in option.expand(value):
                    cmd.append(c)
        image = build.runtime.get_image(build)
        if image:
            cmd.append(f"--image={image}")
        for k, v in build.make_variables.items():
            cmd.append(f"{k}={v}")
        for target in build.targets:
            cmd.append(target.name)

        return cmd
