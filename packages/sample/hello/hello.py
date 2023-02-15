# def tessttt():
#     var = "Hello"
#     print(var)
#     return var
# tessttt()


def main(args):
    name = args.get("name", "stranger")
    greeting = name
    print(greeting)
    return {"body": greeting}
    my_file = open("../output/file.txt", "w")
    my_file.write(greeting)
    my_file.close()
