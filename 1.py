import ctypes

# This Python file uses the following encoding: utf-8

if __name__ == "__main__":
    print("heoo")


# Подключение динамической библиотеки so
libhello_so = ctypes.cdll.LoadLibrary("./lib/libhello.so")
first = libhello_so.first
second = libhello_so.second

first()
second()
