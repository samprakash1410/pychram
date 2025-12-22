def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

fun(couser="data analyst",platform="jenny with code",difficult="moderate")