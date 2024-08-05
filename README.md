**Image Management System**

This system allows users to upload, view, and manage their images, storing the file locations in a JSON file.

**Communication Contract:**

**Requesting Data from the System:**
To request data from the system, you interact directly with the user_data.json file. For example, as below: 
![image](https://github.com/user-attachments/assets/3fbf7e38-8220-4d11-9dc1-b2e9cdd8202b)

**Receive Data from the System:**
The data will be implemented in the user_data.json file and no futher action needs to be incorporated.
![image](https://github.com/user-attachments/assets/453c5ce0-fc05-4a45-96b2-8b7fc0948ac6)


**Example Workflow:**

Uploading an Image:

The user provides the file location of the image.
The system validates the file location and stores it in the user_data.json file under the user's account.

Viewing Images:

The system reads the user_data.json file and displays all stored image locations for the user.

Deleting an Image:

The user selects an image to delete.
The system removes the image entry from the user_data.json file.


****UML SEQUENCE DIAGRAM: ****

![image](https://github.com/user-attachments/assets/4977e9e8-8fb6-41b6-8193-c157f0af208a)

