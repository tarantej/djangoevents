Architecture:-

1. When would you prefer to develop an Assignment 1 style web application(Server-side rendering, serving HTML)?-

When we are certain about the kind of application we will be using for all devices and do not require to change the frontend

2. When would you prefer an Assignment 2 one(REST API &amp; Single Page Application)?

When we would like our front end to be seprated from our backend regardless of the programming language

Version Control:-

1. What is git and what is it used for?-

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

2. List 3 git commands you&#39;ve learned in this course.-

git add, git commit, git push

3. What is GitHub and what is it used for?-

GitHub is a cloud-based hosting service that lets you manage Git repositories. If you have open-source projects that use Git, then GitHub is designed to help you better manage them

4. What is Kanban and what is it used for?-

Kanban is a workflow management method designed to help you visualize your work, maximize efficiency and be agile. From Japanese, kanban is literally translated as billboard or signboard. Originating from manufacturing, it later became a territory claimed by agile software development teams. Recently, it started getting recognized by business units across various areas.

5. What is Markdown and what is it used for?

Markdown is a plain text formatting syntax aimed at making writing for the internet easier. The philosophy behind Markdown is that plain text documents should be readable without tags mussing everything up, but there should still be ways to add text modifiers like lists, bold, italics, etc. It is an alternative to WYSIWYG (what you see is what you get) editors, which use rich text that later gets converted to proper HTML.

Platform vs Infrastructure:-

1. What are some of the pros and cons of using Platform-as-a-Service (PaaS) providers such as Heroku?-

Pros - 

1. Most of the essential services such as OS and server are already preconfigured and apps are hosted on sub domains
2. The software provides support for most programming languages and databases
3. Since Heroku publishes the code directly from our Git repository, therefore no FTP software like FileZilla is required to sync our local and online project

Cons - 

1. This platform is not for someone who would like to tweak the inner server configuration settings
2. Some software may not be available for installation on the platform
3. There may be higher charges for using more advanced features of the software, even though the PaaS is mostly free

2. What are some of the pros and cons of using Infrastructure-as-a-Service providers such as Amazon?

Pros - 

1. Configuring server your own way
2. Pay for what you utilize
3. No limitation on the kind of technology or software you would like to host

Cons - 

1. Setting up the server on your own without having prior technical knowledge can be difficult
2. Having your server in a region not close to you may cause latency and connectivity issues
3. Probable chances of vendor lock-in

Web Frameworks:-

1. What is Django?

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel

2. What are some of its useful features?-

1. Emphasises on clean, well-indented code
2. Beginner friendly learning curve
3. Provides an admin area for managing the database connected content out of the box

3. What is a model?-

A model is a class that maps to the data relation (table) and potentially bridge tables (e.g. for many to many relations).

4. What is a view?-

View is a user interface. View displays data from the model to the user and also enables them to modify the data.

5. Name two other popular non-Python web frameworks.-

1. Laravel(PHP)
2. BootStrap(HTML/CSS)

6. What is WSGI? What is ASGI?-

WSGI - Web Server Gateway Interface

The Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.

ASGI - Asynchronus Server Gateway Interface

ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard
interface between async-capable Python web servers, frameworks, and applications.
Where WSGI provided a standard for synchronous Python apps, ASGI provides one for both asynchronous and synchronous apps, with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.

7. What is celery and what are task queues used for?

Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system. It’s a task queue with focus on real-time processing, while also supporting task scheduling.

Task queues are used as a mechanism to distribute work across threads or machines.

A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform.

Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.

A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

Databases:-

1. What is PostgreSQL? Using StackShare, list 3 well-known companies that use PostgreSQL.-

PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

Companies that use PostgreSQL

1. Uber
2. Netflix
3. Instagram

2. List two other well-known databases.-

1. MySQL
2. SQlite

3. What are some of the pros and cons of using an Object Relational Mapper(ORM)?-

Advantages:

1. Speeds-up Development - eliminates the need for repetitive SQL code.
2. Reduces Development Time.
3. Reduces Development Costs.
4. Overcomes vendor specific SQL differences - the ORM knows how to write vendor specific SQL so you don't have to.

Disadvantages:

1. Loss in developer productivity whilst they learn to program with ORM.
2. Developers lose understanding of what the code is actually doing - the developer is more in control using SQL.
3. ORM has a tendency to be slow.
4. ORM fail to compete against SQL queries for complex queries.

4. What is the purpose of database migrations?-

Database migrations are a great way to 

1. Recreate a database from scratch
2. Make it clear at all times what state a database is in
3. Migrate in a deterministic way from your current version of the database to a newer one

5. What is redis and what are two things it can be used for?-

Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and streams.

You can run atomic operations on these types, like appending to a string; incrementing the value in a hash; pushing an element to a list; computing set intersection, union and difference; or getting the member with highest ranking in a sorted set.

All the commands in a transaction are serialized and executed sequentially. It can never happen that a request issued by another client is served in the middle of the execution of a Redis transaction. This guarantees that the commands are executed as a single isolated operation.

6. Why do we use caches?

Caching is a technique used to accelerate application response times and help applications scale by placing frequently needed data very close to the application. 

HTTP &amp; REST:-

1. Which four HTTP methods does REST use for performing CRUD operations?-

GET, POST, PUT, DELETE

2. What is Django REST Framework used for?-

Django REST framework is a powerful and flexible toolkit for building Web APIs.

3. What is serialization and why do we use it?-

Simply speaking Serialization is a process of converting an Object into stream of bytes so that it can be transferred over a network or stored in a persistent storage. Serialization provides a stable byte representation of the value of software objects that can be sent over a
network that potentially will continue to work correctly even in future implementations using different
hardware and/or software

4. Which type of object serialization notation is most commonly used on the web?-

JSON (JavaScript Object Notation) is widely used as a universal data format on the web that works much like serialization, with the additional advantages of being supported across a wide range of languages and being human-readable as text.

5. What is Postman and what is it used for?-

Postman is a software development tool. It enables people to test calls to APIs. Postman users enter data. The data is sent to a special web server address. Typically, information is returned, which Postman presents to the user.

6. What are websockets and what are they used for?

WebSockets provide a persistent connection between a client and server that both parties can use to start sending data at any time.

The client establishes a WebSocket connection through a process known as the WebSocket handshake. This process starts with the client sending a regular HTTP request to the server. An Upgrade header is included in this request that informs the server that the client wishes to establish a WebSocket connection.

Javascript:-

1. What is NodeJS and how is it different from in-browser Javascript?-

Javascript is a popular programming language and it runs in any web browser with a good web browser. On the other hand, Node.js is an interpreter and environment for the JavaScript with some specific useful libraries which JS programming can be used separately.

2. What is npm and what is it used for?-

npm is the package manager for the Node JavaScript platform. It puts modules in place so that node can find them, and manages dependency conflicts intelligently. It is extremely configurable to support a wide variety of use cases. Most commonly, it is used to publish, discover, install, and develop node programs.

3. What is ES6? List the names of 3 features that ES6 provides.-

ES6 stands for ECMAScript 6. ECMAScript was created to standardize JavaScript, and ES6 is the 6th version of ECMAScript, it was published in 2015, and is also known as ECMAScript 2015.

ES6 provides new features such as

Classes
Arrow Functions
Variables (let, const, var)

4. What is ReactJS and what is it used for?-

React. js is an open-source JavaScript library that is used for building user interfaces specifically for single-page applications. It's used for handling the view layer for web and mobile apps. React also allows us to create reusable UI components

5. List two popular alternative Javascript libraries to ReactJS.-

AngulatJs
Vue JS

6. What is the DOM? What is a virtual DOM?-

DOM stands for Document Object Model and is an abstraction of a structured text. For web developers, this text is an HTML code, and the DOM is simply called HTML DOM. Elements of HTML become nodes in the DOM. The Virtual DOM is an abstraction of the HTML DOM. It is lightweight and detached from the browser-specific implementation details.

7. What is the difference between sessionStorage and localStorage?-

localStorage and sessionStorage accomplish the exact same thing and have the same API, but with sessionStorage the data is persisted only until the window or tab is closed, while with localStorage the data is persisted until the user manually clears the browser cache or until your web app clears the data.

8. What is a library like Material-UI used for?

Material Design is a design language developed in 2014 by Google and is very popular for web and mobile applications. Material Design is inspired by the physical world and its textures, including how they reflect light and cast shadows. Material surfaces reimagine the mediums of paper and ink.
With the components from the Material-UI library it’s very easy to make use of Material Design elements in your React web or mobile application.

Docker: -

1. Why do we run apt-get update && apt-get install -y in one command when using Docker?-

So that the we can ensure that we are installing docker with updated software packages in Linux

2. What are Docker containers and what are the pros and cons of using them?

A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

Pros 

1. Fast
2. Well-Documented
3. Highlighter Public repositories

Cons

1. Platform Dependent
2. Hard to use
3. Poor Monitoring

3. What is the difference between ADD and COPY with Docker?-

COPY and ADD are both Dockerfile instructions that serve similar purposes. They let you copy files from a specific location into a Docker image.

COPY takes in a src and destination. It only lets you copy in a local file or directory from your host (the machine building the Docker image) into the Docker image itself.

ADD lets you do that too, but it also supports 2 other sources. First, you can use a URL instead of a local file / directory. Secondly, you can extract a tar file from the source directly into the destination.

4. What is a .dockerignore file used for?-

dockerignore file is similar to gitignore file, used by the git tool. similarly to . gitignore file, it allows you to specify a pattern for files and folders that should be ignored by the Docker client when generating a build context.

5. What is Kubernetes and why didn't we use it?

Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

We did not use Kubernetes because we felt that our application is way too small to be handled by Kubernetes. Kubernetes has a complex learning curve as well

Deployment:-

1. What is Amazon S3 used for?-
2. What is Amazon ECS?-
3. What is the difference between ECS Fargate and EC2?-
4. Name 3 other cloud providers.-
5. What is Sentry and what is it used for?-
6. What is Cloudflare and what is it used for?-
7. What is SendGrid andwhat is it used for?-
8. What is the difference between a DNS A record and a CNAME record?

Meta:-

1. What are some of the mistakes or difficulties you encountered in developing these 2 assignments?-
2. What have you learned from this course that you think might beuseful in your career?
