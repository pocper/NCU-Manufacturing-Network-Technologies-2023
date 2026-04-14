import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "Machine")
    myobj.add_variable(idx, "CncTypeName", "Milling")
    myobj.add_variable(idx, "VendorName", "黃鉦淳")
    myobj.add_variable(idx, "VendorRevision", "108303013")
    myobj.add_variable(idx, "Version", "1.0.0.0")

    # starting!
    server.start()
    
    try:
        while True:
            time.sleep(1)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()