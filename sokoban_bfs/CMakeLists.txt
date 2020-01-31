cmake_minimum_required(VERSION 2.8)

project(sokoban_bfs)
add_executable(${PROJECT_NAME} "main.cpp" "cpu_usage.hpp" "mem_usage.hpp")
SET(CMAKE_BUILD_TYPE Debug)
