from diagrams import Diagram, Cluster
from diagrams.generic.compute import Rack
from diagrams.aws.security import IAM
from diagrams.aws.analytics import Glue
from diagrams.aws.database import Redshift
from diagrams.aws.storage import S3

graph_attr = {"fontsize": "12", "splines": "ortho", "nodesep": "0.7", "ranksep": "0.8", "margin": "0.05", "pad": "0.01", "overlap": "false"}
node_attr = {"fontsize": "10"}

with Diagram("External Schema Creation Flow", direction="LR", filename="external_schema_flow", show=False, graph_attr=graph_attr, node_attr=node_attr):
    with Cluster("IAM"):
        iam_role = IAM("Glue crawler role\n(processed-crawler)")

    with Cluster("AWS Glue"):
        crawler = Glue("Glue Crawler\n(glue-crawler-processed)")
        catalog = Glue("Glue Data Catalog\nredshift_database")

    with Cluster("Redshift Spectrum"):
        schema = Redshift("External Schema\n(spectrum_processed)")
        query = Rack("Query external tables")

    s3_data = S3("S3 Processed Data")

    iam_role >> crawler
    s3_data >> crawler
    crawler >> catalog >> schema >> query