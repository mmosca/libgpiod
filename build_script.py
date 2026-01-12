Import('env')

env.Append(CPPDEFINES=["_GNU_SOURCE", 1])
