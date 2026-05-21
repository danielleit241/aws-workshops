from diagrams import Diagram
from diagrams.generic.compute import Rack
from diagrams.aws.database import Redshift, Database
from diagrams.aws.security import IAM, SecurityHub
from diagrams.generic.device import Tablet
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server

graph_attr = {"fontsize": "12", "splines": "ortho", "nodesep": "0.7", "ranksep": "0.8", "margin": "0.05", "pad": "0.01", "overlap": "false"}
node_attr = {"fontsize": "10"}

with Diagram("Redshift Serverless Setup Flow", direction="LR", filename="redshift_setup_flow", show=False, graph_attr=graph_attr, node_attr=node_attr):
    access = Client("1. Open Redshift\nConsole")
    customize = Server("2. Customize\nsettings")
    namespace = Database("3. Configure\nNamespace")
    workgroup = Redshift("4. Configure\nWorkgroup")
    iam = IAM("5. Create IAM\nrole")
    network = Server("6. Set network\n& security")
    create = Tablet("7. Review\nand create")
    wait = Rack("8. Wait for\nAvailable")
    complete = Redshift("Ready for\nQuery Editor v2")

    access >> customize >> namespace >> workgroup >> iam >> network >> create >> wait >> complete