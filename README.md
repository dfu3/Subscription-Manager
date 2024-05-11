# Subscription-Manager
Flask API to handle user's subscriptions to weekly newsletter

## Setup
(after cloning repo, ensure you have python installed)
This project installs its dependencies using a python virtual envirenment:
(Windows OS)
```
PS> python -m venv venv
PS> .\venv\Scripts\activate
(venv) PS>
```
( if you get an error when activating the env^ try running the following in an admin shell: `set-executionpolicy remotesigned`) 

After setting up your VE, install dependenices using:
```
(venv) $ python -m pip install -r requirements.txt
```
## Running the API
Run the main app to start the service:
```
(venv) $ python app.py
```
Once running, navigate to `localhost:8000/api/ui/` to view the endpoints

Here, you can test out the endpoints, acting as the front end client that would consume this API.

For example, you can: 
1. find a user_id to test with using -> `GET /users`
2. view the user's active subscription using -> `GET /subscriptions/{user_id}/active`
3. view the user's subscription history using -> `GET /subscriptions/{user_id}/history`
4. create a new subscription for the user -> `POST /subscriptions/{user_id}`
5. delete an existing subscription -> `DELETE /subscriptions/{subscription_id}`
6. update or remove a users current subscription ->  `PATCH /users/{user_id}`
7. AND MORE!

*note: the inital data set is statically initialized upon startup, but changes you make while interacting with the API will live as long as it is running

## Considerations
* The API was designed to allow a web client restful and safe actions on USER and SUBSCRIPTION resources, focusing on any customization we might want to support for a user
* Defining the API routing and parameters in `swagger.yml` allows for simple and modular configuration. The reusable schemas will make extending the API's functionality easier
* The structure of the code is purposely segmented to isolate the API endpoint functions from direct access to the data store
* For the purpose of this exercise, the data is represented as simple python dictionaries that live in memory, but the addition of a rubost ORM such as Django or SQLAlchemy would make the data operations much more efficient and scalable
