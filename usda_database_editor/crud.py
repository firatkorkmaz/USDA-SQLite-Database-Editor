from flask import Flask, request, render_template
import sqlite3  

app = Flask(__name__)  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/categories/dairy_and_egg_products")
def dairy_and_egg_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=100")
    rows = cur.fetchall()
    return render_template("categories/dairy_and_egg_products.html",rows = rows)

@app.route("/categories/spices_and_herbs")
def spices_and_herbs():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=200")
    rows = cur.fetchall()
    return render_template("categories/spices_and_herbs.html",rows = rows)

@app.route("/categories/baby_foods")
def baby_foods():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=300")
    rows = cur.fetchall()
    return render_template("categories/baby_foods.html",rows = rows)

@app.route("/categories/fats_and_oils")
def fats_and_oils():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=400")
    rows = cur.fetchall()
    return render_template("categories/fats_and_oils.html",rows = rows)

@app.route("/categories/poultry_products")
def poultry_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=500")
    rows = cur.fetchall()
    return render_template("categories/poultry_products.html",rows = rows)

@app.route("/categories/soups_sauces_and_gravies")
def soups_sauces_and_gravies():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=600")
    rows = cur.fetchall()
    return render_template("categories/soups_sauces_and_gravies.html", rows=rows)

@app.route("/categories/sausages_and_luncheon_meats")
def sausages_and_luncheon_meats():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=700")
    rows = cur.fetchall()
    return render_template("categories/sausages_and_luncheon_meats.html", rows=rows)

@app.route("/categories/breakfast_cereals")
def breakfast_cereals():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=800")
    rows = cur.fetchall()
    return render_template("categories/breakfast_cereals.html", rows=rows)

@app.route("/categories/fruits_and_fruit_juices")
def fruits_and_fruit_juices():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=900")
    rows = cur.fetchall()
    return render_template("categories/fruits_and_fruit_juices.html", rows=rows)

@app.route("/categories/pork_products")
def pork_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1000")
    rows = cur.fetchall()
    return render_template("categories/pork_products.html", rows=rows)

@app.route("/categories/vegetables_and_vegetable_products")
def vegetables_and_vegetable_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1100")
    rows = cur.fetchall()
    return render_template("categories/vegetables_and_vegetable_products.html", rows=rows)

@app.route("/categories/nut_and_seed_products")
def nut_and_seed_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1200")
    rows = cur.fetchall()
    return render_template("categories/nut_and_seed_products.html", rows=rows)

@app.route("/categories/beef_products")
def beef_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1300")
    rows = cur.fetchall()
    return render_template("categories/beef_products.html", rows=rows)

@app.route("/categories/beverages")
def beverages():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1400")
    rows = cur.fetchall()
    return render_template("categories/beverages.html", rows=rows)

@app.route("/categories/finfish_and_shellfish_products")
def finfish_and_shellfish_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1500")
    rows = cur.fetchall()
    return render_template("categories/finfish_and_shellfish_products.html", rows=rows)

@app.route("/categories/legumes_and_legume_products")
def legumes_and_legume_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1600")
    rows = cur.fetchall()
    return render_template("categories/legumes_and_legume_products.html", rows=rows)

@app.route("/categories/lamb_veal_and_game_products")
def lamb_veal_and_game_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1700")
    rows = cur.fetchall()
    return render_template("categories/lamb_veal_and_game_products.html", rows=rows)

@app.route("/categories/baked_products")
def baked_products():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1800")
    rows = cur.fetchall()
    return render_template("categories/baked_products.html", rows=rows)

@app.route("/categories/sweets")
def sweets():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=1900")
    rows = cur.fetchall()
    return render_template("categories/sweets.html", rows=rows)

@app.route("/categories/cereal_grains_and_pasta")
def cereal_grains_and_pasta():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=2000")
    rows = cur.fetchall()
    return render_template("categories/cereal_grains_and_pasta.html", rows=rows)

@app.route("/categories/fast_foods")
def fast_foods():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=2100")
    rows = cur.fetchall()
    return render_template("categories/fast_foods.html", rows=rows)

@app.route("/categories/meals_entrees_and_side_dishes")
def meals_entrees_and_side_dishes():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=2200")
    rows = cur.fetchall()
    return render_template("categories/meals_entrees_and_side_dishes.html", rows=rows)

@app.route("/categories/snacks")
def snacks():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=2500")
    rows = cur.fetchall()
    return render_template("categories/snacks.html", rows=rows)

@app.route("/categories/american_indian_alaska_native_foods")
def american_indian_alaska_native_foods():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=3500")
    rows = cur.fetchall()
    return render_template("categories/american_indian_alaska_native_foods.html", rows=rows)

@app.route("/categories/restaurant_foods")
def restaurant_foods():
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id=3600")
    rows = cur.fetchall()
    return render_template("categories/restaurant_foods.html", rows=rows)

##########################################

@app.route("/viewupdate", methods=['POST'])
def viewupdate():
    id = request.form["id"]
    food_group_id = request.form["food_group_id"]
    long_desc = request.form["long_desc"]
    short_desc = request.form["short_desc"]
    manufac_name = request.form["manufac_name"]
    sci_name = request.form["sci_name"]
    
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    if len(food_group_id) != 0:
        if food_group_id.isdigit():
            cur.execute("UPDATE food SET food_group_id = ? WHERE id = ?", [food_group_id, id])
    if len(long_desc) != 0:
        if long_desc.isspace():
            cur.execute("UPDATE food SET long_desc = ? WHERE id = ?", [long_desc.strip(), id])
        else:
            cur.execute("UPDATE food SET long_desc = ? WHERE id = ?", [long_desc, id])
    if len(short_desc) != 0:
        if short_desc.isspace():
            cur.execute("UPDATE food SET short_desc = ? WHERE id = ?", [short_desc.strip(), id])
        else:
            cur.execute("UPDATE food SET short_desc = ? WHERE id = ?", [short_desc, id])
    if len(manufac_name) != 0:
        if manufac_name.isspace():
            cur.execute("UPDATE food SET manufac_name = ? WHERE id = ?", [manufac_name.strip(), id])
        else:
            cur.execute("UPDATE food SET manufac_name = ? WHERE id = ?", [manufac_name, id])
    if len(sci_name) != 0:
        if sci_name.isspace():
            cur.execute("UPDATE food SET sci_name = ? WHERE id = ?", [sci_name.strip(), id])
        else:
            cur.execute("UPDATE food SET sci_name = ? WHERE id = ?", [sci_name, id])
            
    con.commit()
    cur.execute("SELECT id, food_group_id, long_desc, short_desc, manufac_name, sci_name FROM food WHERE id = ?",[id])
    rows = cur.fetchall()
    cur.execute("SELECT sequence_num, amount, description, gm_weight, num_data_pts, std_dev FROM weight WHERE food_id = ?",[id])
    rwg = cur.fetchall()
    cur.execute("SELECT nutrient_id, amount, units, tagname, name, num_decimal_places, sr_order, num_data_points, std_error, source_code, num_studients, min, max, modification_date FROM nutrient INNER JOIN nutrition ON nutrition.nutrient_id = nutrient.id WHERE food_id = ?",[id])
    rnt = cur.fetchall()
    return render_template("viewupdate.html", rows=rows, rwg=rwg, rnt=rnt)


@app.route("/delete", methods=['POST'])
def delete():
    id = request.form["id"]
    food_group_id = request.form["food_group_id"]
    
    con = sqlite3.connect("usda.sql3")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute("DELETE FROM food WHERE id = ?", [id])
    cur.execute("DELETE FROM weight WHERE food_id = ?", [id])
    cur.execute("DELETE FROM nutrition WHERE food_id = ?",[id])
    cur.execute("DELETE FROM nutrient WHERE id = (SELECT nutrient_id FROM nutrition WHERE food_id = ?)",[id])
    con.commit()
    
    cur.execute("SELECT id, food_group_id, short_desc, nitrogen_factor, protein_factor, fat_factor, calorie_factor FROM food WHERE food_group_id = ?", [food_group_id])
    rows = cur.fetchall()
    
    if food_group_id == "100":
        return render_template("categories/dairy_and_egg_products.html",rows = rows)
    elif food_group_id == "200":
        return render_template("categories/spices_and_herbs.html",rows = rows)
    elif food_group_id == "300":
        return render_template("categories/baby_foods.html",rows = rows)
    elif food_group_id == "400":
        return render_template("categories/fats_and_oils.html",rows = rows)
    elif food_group_id == "500":
        return render_template("categories/poultry_products.html",rows = rows)
    elif food_group_id == "600":
        return render_template("categories/soups_sauces_and_gravies.html", rows=rows)
    elif food_group_id == "700":
        return render_template("categories/sausages_and_luncheon_meats.html", rows=rows)
    elif food_group_id == "800":
        return render_template("categories/breakfast_cereals.html", rows=rows)
    elif food_group_id == "900":
        return render_template("categories/fruits_and_fruit_juices.html", rows=rows)
    elif food_group_id == "1000":
        return render_template("categories/pork_products.html", rows=rows)
    elif food_group_id == "1100":
        return render_template("categories/vegetables_and_vegetable_products.html", rows=rows)
    elif food_group_id == "1200":
        return render_template("categories/nut_and_seed_products.html", rows=rows)
    elif food_group_id == "1300":
        return render_template("categories/beef_products.html", rows=rows)
    elif food_group_id == "1400":
        return render_template("categories/beverages.html", rows=rows)
    elif food_group_id == "1500":
        return render_template("categories/finfish_and_shellfish_products.html", rows=rows)
    elif food_group_id == "1600":
        return render_template("categories/legumes_and_legume_products.html", rows=rows)
    elif food_group_id == "1700":
        return render_template("categories/lamb_veal_and_game_products.html", rows=rows)
    elif food_group_id == "1800":
        return render_template("categories/baked_products.html", rows=rows)
    elif food_group_id == "1900":
        return render_template("categories/sweets.html", rows=rows)
    elif food_group_id == "2000":
        return render_template("categories/cereal_grains_and_pasta.html", rows=rows)
    elif food_group_id == "2100":
        return render_template("categories/fast_foods.html", rows=rows)
    elif food_group_id == "2200":
        return render_template("categories/meals_entrees_and_side_dishes.html", rows=rows)
    elif food_group_id == "2500":
        return render_template("categories/snacks.html", rows=rows)
    elif food_group_id == "3500":
        return render_template("categories/american_indian_alaska_native_foods.html", rows=rows)
    elif food_group_id == "3600":
        return render_template("categories/restaurant_foods.html", rows=rows)
        

if __name__ == "__main__":
    app.run(debug = True)