# Decorator function which prints stars

def star(fx):
    def mfx(*args):
        print("*****")
        fx(*args)
        print("*****")
    return mfx

@star
def display(name):
    print(name)
display("Ayush")
