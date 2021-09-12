from pyspark import SparkContext
from pyspark.streaming import StreamingContext



sc = SparkContext("spark://spark:7077", "SampleSparkStreamingApp")
ssc = StreamingContext(sc, 1)
ssc.stop()
