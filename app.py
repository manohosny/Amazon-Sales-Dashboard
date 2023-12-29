from flask import Flask, render_template, jsonify
import pandas as pd
import sqlite3

app = Flask(__name__)

@app.route('/get-sales')
def get_sales():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT SUM(discounted_price) AS total_sales FROM amazon;")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-sales/Electronics')
def get_salesElectronics():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'Electronics';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-sales/Home&Kitchen')
def get_salesHome():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'Home&Kitchen';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-sales/Computers&Accessories')
def get_salesComputers():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'Computers&Accessories';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-sales/OfficeProducts')
def get_salesOfficeProducts():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'OfficeProducts';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-products')
def get_products():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT COUNT(product_id) AS total_products FROM amazon;")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-products/Electronics')
def get_productsElectronics():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'Electronics';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-products/Home&Kitchen')
def get_productsHome():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'Home&Kitchen';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-products/Computers&Accessories')
def get_productsComputers():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'Computers&Accessories';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-products/OfficeProducts')
def get_productsOfficeProducts():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'OfficeProducts';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-discount')
def get_discount():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT AVG(discount_percentage * 100) AS average_discount FROM amazon;")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-discount/Electronics')
def get_discountElectronics():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT AVG(discount_percentage * 100) AS average_discount FROM amazon WHERE main_category = 'Electronics';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-discount/Home&Kitchen')
def get_discountHome():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT AVG(discount_percentage * 100) AS average_discount FROM amazon WHERE main_category = 'Home&Kitchen';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-discount/Computers&Accessories')
def get_discountComputers():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT AVG(discount_percentage * 100) AS average_discount FROM amazon WHERE main_category = 'Computers&Accessories';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-discount/OfficeProducts')
def get_discountOfficeProducts():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT AVG(discount_percentage * 100) AS average_discount FROM amazon WHERE main_category = 'OfficeProducts';")
    data = cr.fetchall()
    db.close()
    return jsonify(data)

@app.route('/get-barchart')
def get_barchart():  # This should retrieve the selected category from the form
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT main_category, AVG(rating) AS average_rating FROM amazon GROUP BY main_category;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_ratings'])
    db.close()

    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-barchart/Electronics')
def get_barchartElectronics():  # This should retrieve the selected category from the form
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, AVG(rating) AS average_rating FROM amazon WHERE main_category = 'Electronics' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_ratings'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-barchart/Home&Kitchen')
def get_barchartHome():  # This should retrieve the selected category from the form
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, AVG(rating) AS average_rating FROM amazon WHERE main_category = 'Home&Kitchen' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_ratings'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-barchart/Computers&Accessories')
def get_barchartComputers():  # This should retrieve the selected category from the form
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, AVG(rating) AS average_rating FROM amazon WHERE main_category = 'Computers&Accessories' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_ratings'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-barchart/OfficeProducts')
def get_barchartOfficeProducts():  # This should retrieve the selected category from the form
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, AVG(rating) AS average_rating FROM amazon WHERE main_category = 'OfficeProducts' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_ratings'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-piechart')
def get_piechart():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT main_category, COUNT(product_id) AS total_products FROM amazon GROUP BY main_category;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'product_count'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-piechart/Electronics')
def get_piechartElectronics():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'Electronics' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'product_count'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-piechart/Home&Kitchen')
def get_piechartHome():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'Home&Kitchen' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'product_count'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-piechart/Computers&Accessories')
def get_piechartComputers():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'Computers&Accessories' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'product_count'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-piechart/OfficeProducts')
def get_piechartOfficeProducts():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, COUNT(product_id) AS total_products FROM amazon WHERE main_category = 'OfficeProducts' GROUP BY sub_category LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'product_count'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-bar')
def get_bar():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT main_category, SUM(discounted_price) AS total_sales FROM amazon GROUP BY main_category ORDER BY total_sales DESC;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_sales'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-bar/Electronics')
def get_barElectronics():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'Electronics' GROUP BY sub_category ORDER BY total_sales DESC LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_sales'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-bar/Home&Kitchen')
def get_barHome():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'Home&Kitchen' GROUP BY sub_category ORDER BY total_sales DESC LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_sales'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-bar/Computers&Accessories')
def get_barComputers():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'Computers&Accessories' GROUP BY sub_category ORDER BY total_sales DESC LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_sales'])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/get-bar/OfficeProducts')
def get_barOfficeProducts():
    db = sqlite3.connect('amazon.db')
    cr = db.cursor()
    cr.execute("SELECT sub_category, SUM(discounted_price) AS total_sales FROM amazon WHERE main_category = 'OfficeProducts' GROUP BY sub_category ORDER BY total_sales DESC LIMIT 4;")
    data = cr.fetchall()
    df = pd.DataFrame(data, columns=['main_category', 'total_sales'])
    df['main_category'] = df['main_category'].apply(lambda x: x.split(',')[0])
    db.close()
    result = df.to_dict(orient='records')
    return jsonify(result)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/Electronics')
def index1():
    return render_template('electronics.html')

@app.route('/Home&Kitchen')
def index2():
    return render_template('home&kitchen.html')

@app.route('/Computers&Accessories')
def index3():
    return render_template('computers&accessories.html')

@app.route('/OfficeProducts')
def index4():
    return render_template('officeproducts.html')

if __name__ == '__main__':
    app.run(debug=True)

