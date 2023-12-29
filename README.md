Sales Dashboard Project
=======================

This project is a sales dashboard that provides insights into various categories of products sold on Amazon. The dashboard includes visualizations such as bar charts, pie charts, and a list of top-selling products.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Database Configuration](#database-configuration)
- [Running the Application](#running-the-application)
- [Accessing Different Sections](#accessing-different-sections)
- [Viewing the Dashboard](#viewing-the-dashboard)
- [Closing the Application](#closing-the-application)

### Prerequisites

Ensure that you have the following software/tools installed on your machine:

- Python (version X.X.X)
- Flask framework
- SQLite database
- Pandas library
- AmCharts library
- Bootstrap library

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone [repository_url]
   cd [project_directory]
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Configuration:**

   - Ensure you have the SQLite database file (`amazon.db`) with the required schema.

### Running the Application

```bash
python app.py
```

The application will be accessible at http://localhost:5000/.

### Accessing Different Sections

- Use the sidebar links to navigate to specific categories: Electronics, Home & Kitchen, Computers & Accessories, Office Products.

### Viewing the Dashboard

1. Open your web browser and go to http://localhost:5000/.
2. Explore the different sections of the dashboard:
   - Total Sales, Total Orders, and Average Discount Percentage.
   - Bar charts displaying the average rating by category.
   - Pie charts showing the breakdown of categories.
   - Bar charts illustrating sales by category.
   - A list of top-selling products.

### Closing the Application

Press `Ctrl + C` in the terminal where the Flask application is running to stop the server.
