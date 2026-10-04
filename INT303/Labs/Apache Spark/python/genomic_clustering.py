import sys
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.clustering import KMeans

encodeGenotype = lambda genotype: float(sum( allele!='0' for allele in  genotype.split('|')))
encodeGenotypes = lambda genotypes: Vectors.dense(map(encodeGenotype, genotypes))

def splitGenotypeLine(line):
    columns = line.split()
    return columns[0:9] + [ encodeGenotypes(columns[9:]) ]


def usage():
	print("genomic_clustering.py input-vcf-file output-csv-file [k-clusters = 10] [spark-pararellism=def]")
	sys.exit(1)

def main(argv):

	if len(argv) < 2: 
		usage()

	inputPath = argv[0]
	outputPath = argv[1]
	kClusters = int(argv[2]) if len(argv) > 2 else 10
	sparkPar  = int(argv[3]) if len(argv) > 3 else None

	print("Running with input: %s, output: %s, kClusters: %s, sparkPar: %s" % (inputPath, outputPath, kClusters, sparkPar))

	spark = SparkSession.builder \
		.appName("Genomic Clustering") \
		.getOrCreate()


	sc = spark.sparkContext

	chr22RDD =  sc.textFile(inputPath, sparkPar or sc.defaultMinPartitions)

	print("Loaded %s with %s partitions" % (inputPath, chr22RDD.getNumPartitions()))
	print(chr22RDD.take(10))


	header = chr22RDD.filter(lambda line: line.startswith("#CHROM")).map(lambda line:line.split()).first()
	print(header[0:10])
	columnNames = header[0:9]
	sampleNames = header[9:]
	print(sampleNames[0:10])

	df = spark.createDataFrame(chr22RDD.filter(lambda line: not line.startswith("#")).map(splitGenotypeLine), 
                          schema = columnNames + ['encoded_genotypes'])
	df.cache()
	print("DF Count: %s" % df.count())
	df.printSchema()
	df.limit(10).show()

	kMeans = KMeans(featuresCol='encoded_genotypes', k=kClusters, initMode='random')
	kMeansModel = kMeans.fit(df)

	clusterCentersPD = pd.DataFrame.from_records(kMeansModel.clusterCenters()).T
	clusterCentersPD.insert(0, 'Sample ID', sampleNames)

	spark.createDataFrame(clusterCentersPD).coalesce(1) \
		.write.csv(path=outputPath, mode='overwrite', header=True)

if __name__ == "__main__":
    main(sys.argv[1:])

