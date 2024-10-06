# mattermost-orchestrate-django-application-with-kubernetes

Do you have an application built with Django and PostgreSQL that you’d like to run on Kubernetes?

If so, you’re in luck! In this tutorial, you’ll learn how to orchestrate your Django application with Kubernetes. Since we’re working with multiple microservices, it can be difficult to ensure all parts work together. This tutorial will demystify all that.

To get started, you’ll Dockerize your application, push it to the Docker Hub, then pull it to Kubernetes for orchestration and management. For the Django project, to keep things straight to the point, you’ll build a lead management application. But if you already have an application you’re working with, you can skip that step.

Kubernetes is the most prominent tool used for container orchestration, and many developers learn to use it because of its great value.

Prerequisites
Basic understanding of Docker and Kubernetes
minikube and Kubectl installed.
VirtualBox 5.2 or higher, or the latest Docker
Build a Django application
As mentioned earlier, you’ll build a lead management application. That said, we’ll only be working with the models and using the Django admin to do all the testing. First, we’ll create the Leads model with its required fields then update the admin.py file so that we can access the model we just created on the admin panel.

https://mattermost.com/blog/orchestrate-django-application-with-kubernetes/

https://www.linuxtechi.com/how-to-install-minikube-on-debian/

https://killercoda.com/playgrounds/scenario/kubernetes
