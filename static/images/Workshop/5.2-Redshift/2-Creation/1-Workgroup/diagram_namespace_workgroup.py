from diagrams import Diagram, Cluster, Edge
from diagrams.aws.database import Redshift
from diagrams.aws.security import IAM
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Glue
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack

graph_attr = {"fontsize": "12", "splines": "ortho", "nodesep": "0.45", "ranksep": "0.55", "margin": "0.05", "pad": "0.01", "overlap": "false"}
node_attr = {"fontsize": "10"}

with Diagram("Redshift Serverless Architecture", direction="LR", filename="redshift_serverless_architecture", show=False, graph_attr=graph_attr, node_attr=node_attr):
    with Cluster("Namespace"):
        database = Storage("Database Objects")
        users = IAM("Users & Permissions")
        roles = IAM("IAM Roles")
        metadata = Storage("Metadata & Encryption")

        database >> Edge(style="invis") >> users >> Edge(style="invis") >> roles >> Edge(style="invis") >> metadata

    with Cluster("Workgroup"):
        endpoint = Rack("Query Endpoint")
        compute = Redshift("Compute Engine\n4 RPU")
        monitoring = Rack("Query Monitoring")

        endpoint >> Edge(style="invis") >> compute >> Edge(style="invis") >> monitoring

    with Cluster("External Data Access"):
        iam_role = IAM("S3 / Glue Role")
        s3 = S3("S3 Buckets")
        glue = Glue("Glue Catalog")

        iam_role >> Edge(style="invis") >> s3 >> Edge(style="invis") >> glue

    database >> compute
    users >> compute
    roles >> compute
    metadata >> compute
    endpoint >> compute
    monitoring >> compute
    compute >> iam_role >> s3 >> glue