from pathlib import Path

from diagrams import Diagram
from diagrams.aws.analytics import Athena, Glue
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

output_path = Path(__file__).with_name("athena_query_flow")

with Diagram(
    "Athena Query Flow",
    direction="LR",
    filename=str(output_path),
    outformat="png",
    show=False,
    graph_attr=graph_attr,
    node_attr=node_attr,
):
    processed_data = S3("Processed Data in S3")
    catalog = Glue("Glue Data Catalog")
    athena = Athena("Amazon Athena")
    results = Rack("SQL Query Results")

    processed_data >> catalog >> athena >> results
