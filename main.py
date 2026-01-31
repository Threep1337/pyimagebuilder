# This will be a utility that monitors an upstream docker image repo, and performs rebuilds and pushes to a downstream repo
import docker


def main():
      
    #Quick and dirty image monitoring data, later this all needs to be changed to using a json config file or DB records:
    #Im also hardcoding in the tag for now, later this needs to be seperate in an array
    rebuildConfig = {
        "upstreamImage" : "localhost:5000/upstreamimage:latest",
        "downstreamImage": "localhost:5000/downstream:latest"
    }

    print("Hello world")



if __name__ == '__main__':
    main()
