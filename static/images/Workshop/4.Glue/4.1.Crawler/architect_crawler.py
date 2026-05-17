from diagrams import Diagram, Cluster, Edge
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Glue


graph_attr = {
    "fontsize": "24",
    "fontname": "Arial",
    "bgcolor": "white",
    "pad": "0.6",
    "splines": "ortho",
    "nodesep": "0.9",
    "ranksep": "1.0",
}

node_attr = {
    "fontsize": "13",
    "fontname": "Arial",
}

edge_attr = {
    "fontsize": "11",
    "fontname": "Arial",
    "color": "#4B5563",
    "fontcolor": "#374151",
    "penwidth": "1.8",
}


with Diagram(
    name="AWS Glue Crawler ETL Flow",
    filename="aws-glue-crawler-etl-flow",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    raw_s3 = S3("Amazon S3\nRaw Parquet Data")

    with Cluster("AWS Glue ETL Workflow"):
        crawler = Glue("AWS Glue Crawler\nDiscover Schema")
        catalog = Glue("AWS Glue Data Catalog\nDatabase & Tables")
        etl_job = Glue("AWS Glue ETL Job\nTransform Data")

    processed_s3 = S3("Amazon S3\nProcessed Data")

    raw_s3 >> Edge(label="1. Crawl parquet files") >> crawler

    crawler >> Edge(label="2. Create / update metadata") >> catalog

    catalog >> Edge(label="3. Provide schema metadata") >> etl_job

    raw_s3 >> Edge(label="4. Read source data") >> etl_job

    etl_job >> Edge(label="5. Write transformed data") >> processed_s3