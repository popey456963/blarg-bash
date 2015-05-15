def Parser(data):
    datastr = data.decode("utf-8") # Comes in as bytes, turn this to utf-8
    dataarray = datastr.split(",") # CSV, turn them into an array
    print(dataarray) # Show the array to the user