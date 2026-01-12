Import('env')

env.Append(CPPDEFINES=["_GNU_SOURCE", ('GPIOD_VERSION_STR',str('2.2'))])
