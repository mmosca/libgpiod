Import('env')

env.Append(CPPDEFINES=["_GNU_SOURCE", ("GPIOD_VERSION_STR", "\"\\\"2.2.x-platformio\\\"\"")])
