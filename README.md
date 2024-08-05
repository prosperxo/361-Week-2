**Image Management System**

This system allows users to upload, view, and manage their images, storing the file locations in a JSON file.

**Communication Contract:**
Requesting Data from the System
To request data from the system, you interact directly with the user_data.json file.

**Example Workflow:**

Uploading an Image:

The user provides the file location of the image.
The system validates the file location and stores it in the user_data.json file under the user's account.

Viewing Images:

The system reads the user_data.json file and displays all stored image locations for the user.

Deleting an Image:

The user selects an image to delete.
The system removes the image entry from the user_data.json file.
