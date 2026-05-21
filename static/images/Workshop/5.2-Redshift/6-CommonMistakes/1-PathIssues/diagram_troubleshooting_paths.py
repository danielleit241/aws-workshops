from diagrams import Diagram, Cluster
from diagrams.generic.compute import Rack
from diagrams.aws.database import Redshift
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import S3
from diagrams.generic.storage import Storage

graph_attr = {"fontsize": "12", "splines": "ortho", "nodesep": "0.45", "ranksep": "0.55", "margin": "0.05", "pad": "0.01", "overlap": "false"}
node_attr = {"fontsize": "10"}

with Diagram("Wrong Path vs Correct Spectrum Path", direction="LR", filename="spectrum_query_paths", show=False, graph_attr=graph_attr, node_attr=node_attr):
    with Cluster("Wrong path"):
        editor_wrong = Rack("Query Editor v2")
        load_data = Rack("Load data")
        native_tables = Storage("Redshift native tables")

        editor_wrong >> load_data >> native_tables

    with Cluster("Correct path"):
        editor_right = Rack("Query Editor v2")
        external_schema = Redshift("CREATE EXTERNAL SCHEMA")
        catalog = Glue("Glue Catalog")
        external_tables = Storage("External tables")

        editor_right >> external_schema >> catalog >> external_tables

    s3_data = S3("S3 Processed Data")
    s3_data >> catalog