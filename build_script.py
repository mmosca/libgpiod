Import('env')

env.Append(CPPDEFINES=["_GNU_SOURCE"])
env.Append(CPPFLAGS=["-DGPIOD_VERSION_STR=\"\\"2.2.2\\\"\""])
