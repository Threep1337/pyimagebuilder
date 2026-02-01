# This will be a utility that monitors an upstream docker image repo, and performs rebuilds and pushes to a downstream repo

# Going to try using the docker python libraries
# https://docker-py.readthedocs.io/en/stable/
import docker


# TODO:
# Add labels to the downstream image with the upstream image digest, and check the labels on the downstream image
#    LABEL org.opencontainers.image.base.digest="sha256:..."
# Make the config file be read in from a json file
# Use the python logging module rather than print messages
# Do an image rebuild and push to a registry
# Log the records at first just to the screen, but later make it log records to a DB
# Add error handling for when there is no downstream image currently in the registry that matches the upstream tag
# Make a file that stores variables .env for secure ones that isnt in the repo, maybe another for general config
# Add some unit tests eventually
# Allow for selective rebuilds somehow, maybe via args, so rather than having to go through all images in the config, allow overriding
# The first goal is going to be just to have a simple, hardcoded, auto rebuilder and pusher, hardcode even the docker file for now

def main():
      
    #Quick and dirty image monitoring data, later this all needs to be changed to using a json config file or DB records:
    #Im also hardcoding in the tag for now, later this needs to be seperate in an array
    #This will need many more options as well, like smoke tests, docker steps, etc, for now just hardcode everything and test it.
    rebuildConfig = {
        "upstreamImage" : "localhost:5000/upstreamimage:latest",
        "downstreamImage": "localhost:5000/downstream:latest"
    }

    print("Starting Python docker rebuilder")
    print(f"Going to check {rebuildConfig['upstreamImage']} to see what its digest is.")

    dockerClient = docker.from_env()
    #dockerClient.images.get(rebuildConfig["upstreamImage"])
    #dockerClient.images.pull(rebuildConfig["upstreamImage"])
    regData = dockerClient.images.get_registry_data(rebuildConfig["upstreamImage"])
    upstreamDigest = regData.id
    print(f"The upstream image digest is: {upstreamDigest}")

    print ("Going to get the downstream image digest...")

    # This throws an error if the downstream doesnt exist yet
    # If it doesn't exist, or if the hash is different, I want to rebuild and re push the downstream image
    # I actually need to get the label that shows the upstream origin digest.
    regData = dockerClient.images.get_registry_data(rebuildConfig["downstreamImage"])

    downstreamDigest = regData.id
    print(f"The downstream image digest is: {downstreamDigest}")




if __name__ == '__main__':
    main()
