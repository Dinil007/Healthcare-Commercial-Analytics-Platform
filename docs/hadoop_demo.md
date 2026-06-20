# Hadoop Demonstration

## Objective
Demonstrate how healthcare sales data can be stored and processed using Hadoop Distributed File System (HDFS).

## Example Workflow

1. Export `healthcare_sales_100k.csv`.
2. Upload the file to HDFS.
3. Store large-scale healthcare sales data in a distributed environment.
4. Process the data using Hive or Spark for analytics.

## Example HDFS Commands

```bash
hdfs dfs -mkdir /healthcare
hdfs dfs -put healthcare_sales_100k.csv /healthcare/
hdfs dfs -ls /healthcare
```

## Benefits

- Distributed storage
- Fault tolerance
- Scalable for millions of records
- Suitable for big data analytics