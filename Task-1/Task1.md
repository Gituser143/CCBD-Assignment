Task1
======

For the task we hosted a server (Proxy 0) which connects to 4 proxy servers (Proxy 1,2,3,4). The server, Proxy 0 takes requests from the client and forwards these to the list of proxy servers. These 4 proxy servers are load balanced with the round robin algorithm.   

The 4 proxy servers connect to www.espncricinfo.com and cache the response received locally. On subsequent requests, the relevant data is loaded from cache without making another request to espncricinfo.com.    

If there are changes to the website content at espncricinfo.com, the corresponding cache is updated.

Network Structure
==================

![Network Structure](Network-Layout.png)
