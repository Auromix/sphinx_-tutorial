cmake_minimum_required(VERSION 3.10)

project(MyCppProject)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)

# Add source files
set(SOURCE_FILES
    src/main.cpp       # Make sure to include your main.cpp
    src/calculator.cpp
)

# Add executable target
add_executable(MyCppProject ${SOURCE_FILES})

# If you're using Sphinx and Doxygen, ensure these dependencies are also added
# add_dependencies(MyCppProject doc_sphinx)  # Uncomment if you are generating docs
