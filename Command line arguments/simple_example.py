# import the necessary packages
import argparse

# construct the argument parse and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
    help="name of the user")
print(ap.parse_args())
args = vars(ap.parse_args())
print(args)

# display a friendly message to the user
print("Hi there {}, it's nice to meet you".format(args["name"]))