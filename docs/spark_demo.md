# Apache Spark Demonstration

## Objective

Demonstrate distributed data processing for large-scale healthcare sales analytics using Apache Spark.

## PySpark Example

```python
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Healthcare Analytics") \
    .getOrCreate()

# Load CSV
df = spark.read.csv(
    "healthcare_sales_100k.csv",
    header=True,
    inferSchema=True
)

# Show schema
df.printSchema()

# Total Revenue
df.groupBy().sum("Revenue").show()

# Revenue by Product
df.groupBy("Product_ID") \
  .sum("Revenue") \
  .show()

# Revenue by Region
df.groupBy("Region_ID") \
  .sum("Revenue") \
  .show()

# Stop Spark session
spark.stop()
```

## Benefits

- Fast in-memory processing
- Scalable to millions of records
- Supports SQL, Python, Java, and Scala
- Ideal for healthcare big data analytics