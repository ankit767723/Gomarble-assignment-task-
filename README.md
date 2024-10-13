# Gomarble-assignment-task-


# My Django Project

## Project Description

My Django Project is a web application that provides a RESTful API for managing reviews. 

## Motivation

The motivation behind this project is to provide a simple and efficient way to collect reviews data in json form for websites.

## System Architecture or Workflow

The system architecture or workflow of the project is as follows:

* The user sends a request to the API endpoint.
* The API endpoint processes the request and returns a response.
* The response is then sent back to the user.

## Instructions on How to Run the Project

To run the project, follow these steps:

1. Clone the repository using `git clone`.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the migrations using `python manage.py migrate`.
4. Start the development server using `python manage.py runserver`.

## API Usage and Sample Responses

The API provides the following endpoints:

* `GET /reviews/`: Returns a list of all reviews.
* `POST /reviews/`: Creates a new review.
* `GET /reviews/:id`: Returns a single review by ID.
* `PUT /reviews/:id`: Updates a single review by ID.
* `DELETE /reviews/:id`: Deletes a single review by ID.

Here is an example of a sample response:
{
  "reviews_count": 150,
  "reviews": [
    {
      "title": "Excellent Product!",
      "body": "I have been using this product for a week, and it has exceeded my expectations...",
      "rating": 5,
      "reviewer": "Ankit Kumar"
    },
    {
      "title": "Not worth the price",
      "body": "The product did not perform as advertised. I encountered several issues...",
      "rating": 2,
      "reviewer": "Ashish singh"
    }
   
}
