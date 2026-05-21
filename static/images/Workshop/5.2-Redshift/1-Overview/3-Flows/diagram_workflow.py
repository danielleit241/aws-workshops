from diagrams import Diagram
from diagrams.aws.database import Redshift
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import S3
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage

graph_attr = {"fontsize": "12", "splines": "ortho", "nodesep": "0.45", "ranksep": "0.55", "margin": "0.05", "pad": "0.01", "overlap": "false"}
node_attr = {"fontsize": "10"}

with Diagram("Redshift Spectrum Workflow", direction="LR", filename="redshift_spectrum_workflow", show=False, graph_attr=graph_attr, node_attr=node_attr):
    user = Rack("User / BI Tool")
    redshift = Redshift("Redshift Query Layer")
    glue = Glue("Glue Data Catalog")
    s3 = S3("S3 Data Lake")
    spectrum_nodes = Storage("Spectrum Scan")
    results = Rack("Result Set")

    user >> redshift >> glue >> s3 >> spectrum_nodes >> results