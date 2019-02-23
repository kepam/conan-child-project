from conans import ConanFile, CMake, tools
from conans import python_requires

base = python_requires("conan-base-project/0.1.0@test/test")
class ConanchildprojectConan(base.ConanbaseprojectConan):
    name = "conan-child-project"
    version = "0.1.0"
    exports_sources = "CMakeLists.txt", "src/*"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("bin/*");
