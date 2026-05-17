from diagrams import Diagram, Edge
from diagrams.aws.storage import S3
from diagrams.aws.analytics import GlueCrawlers, GlueDataCatalog, Athena

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "1.0",
    "ranksep": "1.2",
}

node_attr = {
    "fontsize": "12",
}

edge_attr = {
    "fontsize": "10",
}

with Diagram(
    "AWS Glue Data Catalog Flow",
    filename="aws_glue_data_catalog_flow",
    outformat="png",
    show=False,
    direction="LR",   # Left -> Right, để diagram nằm ngang
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    s3 = S3("Amazon S3\nStores the actual data files")

    crawler = GlueCrawlers(
        "AWS Glue Crawler\nScans data and detects schema"
    )

    catalog = GlueDataCatalog(
        "AWS Glue Data Catalog\nStores metadata about the data"
    )

    analytics = Athena(
        "Analytics Services\nUse metadata to read and process data"
    )

    s3 >> Edge(label="scan source data") >> crawler
    crawler >> Edge(label="create / update metadata") >> catalog
    catalog >> Edge(label="metadata used by services") >> analytics