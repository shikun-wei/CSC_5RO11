# CSC_5RO11 - Apprentissage pour la robotique
- **Name**: Shikun Wei
- **Email**: shikun.wei@ensta-paris.fr

# Homework 1

This project is a homework assignment designed to demonstrate inter-node communication in the Robot Operating System (ROS). It involves the implementation of four distinct ROS nodes: `node_A`, `node_B`, `node_C`, and `node_D`. Each node is responsible for sending and receiving messages, and each node modifies the message before passing it along to the next node in sequence. The message passes through all nodes in the system and finally returns to `node_A`.

### Topics and Remapping
The communication between nodes is handled by publishing and subscribing to topics, which are remapped in the launch file to ensure correct message flow. Below is the topic flow:

- `node_A` publishes on `outgoing_A`, which is remapped to `incoming_B`.
- `node_B` publishes on `outgoing_B`, which is remapped to `incoming_C`.
- `node_C` publishes on `outgoing_C`, which is remapped to `incoming_D`.
- `node_D` publishes on `outgoing_D`, which is remapped to `incoming_A`.

### Key Features
- Demonstrates message passing and topic remapping in ROS.
- Message type: `std_msgs/String`.
- Each node adds its corresponding letter ("A", "B", "C", or "D") to the message it receives, and forwards the updated message to the next node.

## Folder Structure of the Package
The folder structure is as follows:
```
homework_shikunwei/
├── build/
├── devel/
└──src/
    └── homework_1/
        ├── CMakeLists.txt
        ├── package.xml
        └── src/
            ├── node_A.py
            ├── node_B.py
            ├── node_C.py
            └── node_D.py     
        └── launch
            ├── homework_1.launch
