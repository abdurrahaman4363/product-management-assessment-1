# Django REST API for Product and Category Management

This project implements a Django REST API to manage products and categories, with support for image uploads, JWT authentication, pagination, and throttling. The project also includes database optimization, deployment on a cloud platform, and CI/CD setup for automatic deployment.

## Features

1. **CRUD Operations on Products and Categories**  
   The API provides endpoints to create, retrieve, update, and delete products and categories.

2. **Image Upload**  
   Image upload functionality is implemented using Django's `ImageField` for product images.

3. **JWT Authentication**  
   Authentication is implemented using `djangorestframework-simplejwt` to secure the API.

4. **Pagination and Throttling**  
   The API includes pagination for product listings and throttling to limit request rates.

5. **Database Optimization**  
   Database indexing has been applied to frequently queried fields to improve query performance. Optimized queries using Django ORM are implemented.

6. **Deployment on Render**  
   The project is deployed on a cloud platform with PostgreSQL as the database. It includes secure HTTPS connections, and environment configuration follows security best practices.

7. **CI/CD Setup**  
   CI/CD pipelines are configured for automatic deployment whenever new code is pushed to the repository.

---

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT 
- **Database**: PostgreSQL
- **Cloud Hosting**: Render 
- **CI/CD**: GitHub Actions/Render CI/CD

## API Endpoints

Here is a brief overview of the main API endpoints:

### Categories
- [`GET /category/`](https://product-management-assessment.onrender.com/category)


### Products
- [`GET /products/`](https://product-management-assessment.onrender.com/products)


### Authentication
- [`POST /register/`](https://product-management-assessment.onrender.com/register)
  - **Description:** 
  This endpoint allows you to create a new user by providing `username`, `email`, and `password`.
- [`POST /login/`](https://product-management-assessment.onrender.com/login)
  - **Description:** 
  This endpoint allows users to log in by providing username and password. It will return an access and refresh token for authentication.
- [`POST /logout/`](https://product-management-assessment.onrender.com/logout)
  - **Description:** 
  This endpoint logs out the user by blacklisting the refresh token. You need to provide the refresh token in the request body and the access token in the Authorization header.



---

