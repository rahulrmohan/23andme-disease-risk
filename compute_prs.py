import cPickle
import numpy as np
import tabix
import glob

def compute_1000genomes_prs():
	url = "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20100804/"
	url += "ALL.2of4intersection.20100804.genotypes.vcf.gz"
	tb = tabix.open(url)
	records = tb.query("1", 752720, 752721)
	for record in records:
		print record

def compute_prs(raw_genotype_file, variants):
	counter = 0
	prs_score = 0.0
	url = "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20100804/"
	url += "ALL.2of4intersection.20100804.genotypes.vcf.gz"
	tb = tabix.open(url)
	bed_file = open(raw_genotype_file.split(".")[0]+".bed","wb")

	with open(raw_genotype_file, "rb") as genotypes:
		for line in genotypes:
			if (line[0] == "#"):
				continue
			columns = line.split("\t")
			bed_file.write(columns[1] + "\t" + str(int(columns[2])-1) + "\t" + str(int(columns[2])) + "\n")
			try:
				genotype = columns[3][0] + ":" + columns[3][1]
				variant = columns[1] + ":" + columns[2] + ":" + genotype
				score = variants[variant]
				prs_score += float(score)
			except:
				continue
			counter += 1
			print(counter)
			
	bed_file.close()
	return prs_score

def compute_prs_population(disease_file):
	variants = cPickle.load(open(disease_file))
	users = glob.glob("23andMe_Users/*")
	for user_file in users:
		print compute_prs(user_file, variants)

if __name__ == '__main__':
	#compute_prs_population("CoronaryArteryDisease.pkl")
	variants = cPickle.load(open("CoronaryArteryDisease.pkl"))
	print compute_prs("genome_Karthik_Jagadeesh_v3_Full_20180908215258.txt", variants)
	#compute_1000genomes_prs()