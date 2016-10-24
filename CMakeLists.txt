cmake_minimum_required(VERSION 3.5)

project(ppao)
# set(CMAKE_INSTALL_PREFIX "/opt")
set(CMAKE_PREFIX_PATH "${CMAKE_PREFIX_PATH};/opt/opencv")
# dependencies
# set(OpenCV_DIR "/opt/opencv/share/OpenCV")
find_package(OpenCV 3 CONFIG REQUIRED)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(CH3_SOURCE_FILES src/loadDisplaySave.h src/getSet.h)
# add_executable(img_view ${CH3_SOURCE_FILES} src/main.cpp)
add_executable(app src/main.cpp src/getSet.h src/drawing.h src/image_transformation.h)
target_link_libraries(app ${OpenCV_LIBS})