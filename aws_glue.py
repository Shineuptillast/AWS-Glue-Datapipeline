import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df_glue = glueContext.create_dynamic_frame_from_options(
    connection_type='s3', connection_options={"paths": [s3_location]}, format='json', tranformation_ctx='data_1')
df = df_glue.toDF()


job.commit()
