from scipy import spatial
import numpy as np
import pandas as pd


def cosine_similarity(arr1, arr2):
	return 1 - spatial.distance.cosine(arr1, arr2)


padpick = pd.read_json("padpick.json", "r")


dvs = open("description_vectors.txt", "r")

#print padpick

description_vectors = []

for line in dvs:
	description_vectors.append(line.strip().split(' '))

index_file = open("indices.txt", "r")

indices = []

for line in index_file:
	indices.append(int(float(line.strip())))

#print indices
#print description_vectors


#print len(description_vectors)

#x = raw_input("Enter a number between 1 and 3129\n")


weights = open("recommender_weights.txt", "r")

weight_values = []

for line in weights:
	weight_values.append(float(line.strip()))

print weight_values


new_description_vectors = []

for i,j in enumerate(description_vectors):
	cur = np.asarray(map(float, description_vectors[i]))
	cur2 = []
	for k,l in enumerate(cur):
		cur2.append(cur[k] * l)

	new_description_vectors.append(np.array(cur2))


new_description_vectors = np.asarray(new_description_vectors)

print new_description_vectors


file = open("recommender_input.txt", "r")

entries_liked = []
for line in file:
	entries_liked.append(int(line.strip(' ').strip('\n')))

#print recipes_liked

file.close()




x = int(raw_input("Enter a number between 0 and 3128\n"))

user_input = new_description_vectors[x]

cosine_distances = []
for j,i in enumerate(new_description_vectors):
	cosine_distances.append(cosine_similarity(map(float, user_input), map(float, i)))
	#print cosine_similarity(map(float, mass_fractions_matrix[0]), map(float, i))

cosine_distances = np.asarray(cosine_distances)
order = cosine_distances.argsort()

#print order
#print cosine_distances

#print indices

results = []

#print "Your selected real estate entry was:\n"
#print np.asarray(padpick)[int(indices[int(x) - 1]) - 1]

print "\n\n"
results.append(np.asarray(padpick)[int(indices[int(x)])])

#print "\n\nThe top 10 results are:"
for i in order[-11:][::-1][1:]:
	#print np.asarray(padpick)[int(indices[int(i) - 1]) - 1]
	results.append(np.asarray(padpick)[int(indices[int(i)])])
	#print cosine_similarity(map(float, user_input), map(float, description_vectors[i]))
	#print "\n\n"

file = open(str(x)+ ".tsv", "w")
file.write("Address\tBathrooms\tBedrooms\tBrokerage\tBuilder\tDetailedCharacteristics\tDisclaimer\tDiscloseAddress\tExpenses\tForeclosureStatus\tFullBathrooms\tHalfBathrooms\tLeadRoutingEmail\tListPrice\tListPriceLow\tListingCategory\tListingDate\tListingDescription\tListingKey\tListingParticipants\tListingStatus\tListingTitle\tListingURL\tLivingArea\tLocation\tLotSize\tMarketingInformation\tMlsId\tMlsName\tMlsNumber\tModificationTimestamp\tOffices\tOneQuarterBathrooms\tOpenHouses\tPartialBathrooms\tPhotos\tPropertySubType\tPropertyType\tProviderCategory\tProviderName\tProviderURL\tTaxes\tThreeQuarterBathrooms\tVirtualTours\tYearBuilt\n")
for i in results:
	#print i
	cur = []
	for j in i:
		#print type(j)
		if type(j) == type(u'dd'):
			cur.append(j.encode('utf-8'))
		else:
			cur.append(str(j).encode('utf-8'))
	file.write ('\t'.join(cur))
	file.write('\n')

file.close()

