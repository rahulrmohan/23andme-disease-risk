import shelve
import cPickle

def scores_file_to_db(file_name, scores_file_name):
	variant_to_effect_map = {}
	counter = 0
	with open(file_name, "rb") as scores_file:
		for line in scores_file:
			if (counter % 1000 == 0):
				print counter
			if (line[0] == "#"):
				continue
			columns = line.split("\t")
			if (columns[0] == "variant"):
				continue
			variant_to_effect_map[columns[0]] = columns[2]
			counter += 1
	cPickle.dump(variant_to_effect_map, open(scores_file_name,"wb"), protocol=2)

if __name__ == '__main__':
	scores_file_to_db("CoronaryArteryDisease_PRS_LDpred_rho0.001_v3.txt", "CoronaryArteryDisease.pkl")




