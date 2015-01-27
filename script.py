from temboo.Library.Factual import FindRestaurantsByName
from temboo.core.session import TembooSession

#top 100 chains source: http://nrn.com/us-top-100/top-100-chains-us-sales
restaurants = ["McDonald's", "subway", "starbucks", "burger king", "wendys", "taco bell", "Dunkin Donuts", "pizza hut", "KFC", "applebees", "Chick-fil-A", "Sonic, Americas Drive-In", "Olive Garden", "Chilis Grill Bar ", "Dominos Pizza ", "Panera Bread", "Jack in the Box", "Arbys", "Dairy Queen", "Red Lobster", "IHOP", "Dennys", "Outback Steakhouse", "Chipotle Mexican Grill/Chipotle ", "Papa Johns Pizza", "Buffalo Wild Wings Grill Bar", "Cracker Barrel Old Country Store", "Hardees", "T.G.I. Fridays", "7-Eleven", "Popeyes Louisiana Kitchen", "Golden Corral", "The Cheesecake Factory", "Panda Express", "Disney theme parks, hotels resorts", "Little Caesars Pizza", "Carls Jr.", "Ruby Tuesday", "Texas Roadhouse", "Whataburger", "Marriott Hotels Resorts", "Red Robin Gourmet Burgers Spirits", "hilton", "LongHorn Steakhouse", "Jimmy Johns", "Waffle House", "Bob Evans Restaurants", "Five Guys Burgers and Fries", "P.F. Changs China Bistro", "Sheraton Hotels", "Churchs Chicken", "Hooters", "Holiday Inn", "Quiznos Sub ", "Zaxbys", "Steak n Shake", "Bojangles Famous Chicken n Biscuits", "Culvers", "Long John Silvers", "Papa Murphys Take N Bake Pizza", "Perkins Restaurant and Bakery", "Carrabbas Italian Grill", "California Pizza Kitchen", "Logans Roadhouse", "Romanos Macaroni Grill ", "BJs Restaurant Brewery", "In-N-Out Burger ", "Del Taco", "Hyatt Hotels", "Circle K ", "Friendlys Ice Cream", "El Pollo Loco", "Costco", "Jasons Deli", "OCharleys ", "Boston Market", "Krispy Kreme Doughnuts", "Wawa ", "Qdoba Mexican Grill", "White Castle", "CiCis Pizza", "Caseys General Stores", "Baskin-Robbins", "Famous Daves", "Tim Hortons", "Ruths Chris Steak House", "Target Cafe (Target Stores)", "Westin Hotels Resorts", "Bonefish Grill", "Sheetz", "Jamba Juice", "Cheddars", "Einstein Bros. Bagels", "Captain Ds Seafood", "Checkers", "Sbarro, The Italian Eatery", "Krystal", "Chuck E. Cheeses", "Big Boy Restaurant Bakery/Frischs Big Boy", "On the Border Mexican Grill Cantina"]

# Instantiate the Choreo
findRestaurantsByNameChoreo = FindRestaurantsByName(session)


for r in restaurants:

	# Get an InputSet object for the Choreo
	findRestaurantsByNameInputs = findRestaurantsByNameChoreo.new_input_set()

	# Set the Choreo inputs
	findRestaurantsByNameInputs.set_Query(r)

	# Execute the Choreo
	findRestaurantsByNameResults = findRestaurantsByNameChoreo.execute_with_results(findRestaurantsByNameInputs)

	# Print the Choreo outputs
	with open("data/"+ r + ".txt", 'w') as f:
		f.write(findRestaurantsByNameResults.get_Response())
