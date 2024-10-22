# Kubernetes courseware

This is the courseware for Kubernetes courses. It includes exercise files for lectures as well as a Hackthon application for students to practice the concepts they learn in class.

# Setup Instructions

Check https://gist.github.com/axel-sirota/f0583ec4ea69d6d4178f2d8f7b561304

## Optional Multi-Node Kubernetes Cluster
k3d offers a great way to start up a multi-node cluster on your local workstation using Docker containers as Kubernetes nodes. This allows you to work in a simulated large cluster environment to practice cluster management. I've tested this using Rancher Desktop, but it should work fine for Docker Desktop.
1. Visit [k3d.io](https://www.k3d.io) for more detailed instructions.
1. In a terminal, run `wget -q -O - https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash`. Alternatively, you can use Homebrew with `brew install k3d`
1. Set up your cluster. In this repository, navigate to the `k3d` directory. Run `make create-cluster` or open the `Makefile` and grab the command and run it.
1. To switch your Kubernetes context to the k3d cluster, run `kubectl config use-context k3d-k3d`
---

### All content is copyright Data Trainers LLC and is intended to be used for educational purposes alone