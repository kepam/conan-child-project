cmake_minimum_required (VERSION 2.8.11)
project(test)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test src/main.cpp)
target_link_libraries(test)
