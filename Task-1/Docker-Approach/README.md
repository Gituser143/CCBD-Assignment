Execution
=========

**Method 1 Description:** This method implements multiple containers running locally. It uses one server which the end user connects to and multiple proxy servers which load balance the incoming traffic. Each of these servers run in separate containers. If needed more proxy servers can be added.

**Method 2 Description:** This method uses a single container hosting one server (which the user contacts) and 4 proxy servers. This image can be pulled from dockerhub.

Method 1:
---------

In the current project directory run ```docker-compose up```

Then navigate to ```localhost:8000```

Method 2:
---------

Execute the following commands:
```
  docker pull skete/ccbdproxy
  docker run -p 8000:8000 skete/ccbdproxy
````
Then navigate to ```localhost:8000```
