def convert_kg(value):
    # Your code starts here
    pounds = value * 2.20462
    ounces = value * 35.274
    print (value, "kg converted is", pounds,"pounds and", ounces,"ounces.")
	
def convert_pound(value):
    # Your code starts here
    kg = value * 0.453592 
    ounces = value * 16
    print (value, "pounds converted is", kg,"kg and", ounces,"ounces.")

def convert_ounce(value):
    # Your code starts here
    kg = value * 0.0283  
    pound = value * 0.0625
    print (value, "ounces converted is", kg,"kg and", pound,"pounds.")


