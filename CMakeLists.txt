cmake_minimum_required(VERSION 3.0)
project(opencv_imgcodecs)

set(CXX_STANDARD 14)
list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_BINARY_DIR})

find_package(OpenCV REQUIRED)

add_executable(test_conan_opencv_codecs test_conan_opencv_codecs.cpp)
target_link_libraries(
    test_conan_opencv_codecs PRIVATE
    opencv_core opencv_imgcodecs opencv_imgproc opencv_highgui
    )
