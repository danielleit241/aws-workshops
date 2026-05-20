from pathlib import Path

from diagrams import Diagram
from diagrams.aws.analytics import Glue
from diagrams.aws.database import Redshift
from diagrams.aws.storage import S3
from diagrams.generic.compute import Rack

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

output_path = Path(__file__).with_name("business_intelligence_flow")

with Diagram(
    "Business Intelligence Flow",
    direction="LR",
    filename=str(output_path),
    outformat="png",
    show=False,
    graph_attr=graph_attr,
    node_attr=node_attr,
):
    raw_data = S3("Raw Data in S3")
    crawler = Glue("Glue Crawler")
    catalog = Glue("Glue Data Catalog")
    etl = Glue("Glue ETL Job")
    processed_data = S3("Processed Data in S3")
    query_layer = Rack("Athena / Redshift Spectrum")
    dashboards = Rack("QuickSight Dashboards")

    raw_data >> crawler >> catalog >> etl >> processed_data >> query_layer >> dashboards
