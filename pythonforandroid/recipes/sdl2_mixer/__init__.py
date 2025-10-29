import os

from pythonforandroid.recipe import BootstrapNDKRecipe


class LibSDL2Mixer(BootstrapNDKRecipe):
    version = '2.8.1'
    url = 'https://github.com/libsdl-org/SDL_mixer/releases/download/release-{version}/SDL2_mixer-{version}.tar.gz'
    dir_name = 'SDL2_mixer'

    def get_include_dirs(self, arch):
        return [
            os.path.join(self.ctx.bootstrap.build_dir, "jni", "SDL2_mixer", "include")
        ]

    with open(os.path.join(build_dir, ".gitmodules"), "r") as file:
            for section in file.read().split('[submodule "')[1:]:
                line_split = section.split(" = ")
                # Parse .gitmodule section
                clone_path, url, branch = (
                    os.path.join(build_dir, line_split[1].split("\n")[0].strip()),
                    line_split[2].split("\n")[0].strip(),
                    line_split[-1].strip()
                )
                # Clone if needed
                if not os.path.exists(clone_path) or not os.listdir(clone_path):
                    shprint(
                        sh.git, "clone", url,
                        "--depth", "1", "-b",
                        branch, clone_path, "--recursive"
                    )

        super().prebuild_arch(arch)


recipe = LibSDL2Mixer()
