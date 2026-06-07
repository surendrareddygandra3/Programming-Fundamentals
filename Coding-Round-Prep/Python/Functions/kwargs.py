# Function definition
def show(**kwargs):

    # Traverse dictionary
    for key, value in kwargs.items():

        print(key, ":", value)


# Function call
show(
    name="Surendra",
    age=23,
    city="Vijayawada"
)