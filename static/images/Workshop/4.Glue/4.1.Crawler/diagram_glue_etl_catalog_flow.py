from pathlib import Path

from diagrams import Diagram
from diagrams.aws.analytics import GlueDataCatalog, Glue
from diagrams.aws.storage import S3

graph_attr = {
    "fontsize": "12",
    "splines": "ortho",
    "nodesep": "0.45",
    "ranksep": "0.55",
    "margin": "0.05",
    "pad": "0.01",
    "overlap": "false",
}
node_attr = {"fontsize": "10"}

output_path = Path(__file__).with_name("glue_etl_catalog_flow")

with Diagram(
    "Glue ETL Catalog Flow",
    direction="LR",
    filename=str(output_path),
    outformat="png",
    show=False,
    graph_attr=graph_attr,
    node_attr=node_attr,
):
    catalog_table = GlueDataCatalog("Glue Data Catalog\nTable")
    etl_context = Glue("Glue ETL Job\nSchema + S3 Location")
    s3_source = S3("Amazon S3\nSource Files")
    etl_transform = Glue("Glue ETL Job\nTransform Data")
    s3_output = S3("Amazon S3\nProcessed Data")

    catalog_table >> etl_context >> s3_source >> etl_transform >> s3_output
