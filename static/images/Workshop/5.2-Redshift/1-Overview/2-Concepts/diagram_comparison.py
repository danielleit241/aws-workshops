from diagrams import Diagram, Cluster
from diagrams.aws.database import Redshift
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Glue
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack

graph_attr = {"fontsize": "12", "splines": "ortho", "nodesep": "0.45", "ranksep": "0.55", "margin": "0.05", "pad": "0.01", "overlap": "false"}
node_attr = {"fontsize": "10"}

with Diagram("Traditional Redshift vs Redshift Spectrum", direction="LR", filename="redshift_comparison", show=False, graph_attr=graph_attr, node_attr=node_attr):
    with Cluster("Traditional Redshift"):
        load_data = Rack("COPY / ETL")
        warehouse = Redshift("Redshift Cluster")
        internal_tables = Storage("Internal Tables")

        load_data >> warehouse >> internal_tables

    with Cluster("Redshift Spectrum"):
        query = Rack("Query Editor v2")
        redshift = Redshift("Redshift")
        glue_catalog = Glue("Glue Catalog")
        s3_data_lake = S3("S3 Data Lake")
        external_tables = Storage("External Tables")

        query >> redshift >> glue_catalog >> s3_data_lake >> external_tables