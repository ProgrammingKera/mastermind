from flask import Blueprint, render_template, send_from_directory, redirect

routes = Blueprint('routes', __name__)

# ==================== Auth Pages =====================
@routes.route('/signup')
def signup():
    return render_template('SignUp.html')

@routes.route('/signin')
def signin():
    return render_template('SignIn.html')

@routes.route('/forgot_password')
def forgot_password():
    return render_template('ForgetPassword.html')

@routes.route('/verification')
def verification():
    return render_template('verification.html')

@routes.route('/reset-password')
def reset_password_page():
    return render_template('reset-password.html')

# ==================== Dashboards =====================
@routes.route('/dashboard')
def dashboard():
    return render_template("ownerdashboard.html")

@routes.route('/BIexpiry')
def BIexpiry():
    return render_template("BIexpiry.html")

@routes.route('/customerdashboard')
def customerdashboard():
    return render_template("customerdashboard.html")

# ==================== Admin-only Pages (Now Public) =====================
@routes.route('/admininventory')
def inventory():
    return render_template("admininventory.html")

@routes.route('/employes')
def employes():
    return render_template("employee.html")

@routes.route('/expiry')
def expiry():
    return render_template("expiriy.html")

@routes.route('/order')
def order():
    return render_template("order.html")

@routes.route('/customer')
def customer():
    return render_template("customer.html")

@routes.route('/customerprofile')
def customer_profile():
    return render_template("customerprofile.html")

# ==================== Owner/Admin User Management =====================
@routes.route('/adminusers')
def admin_users():
    return render_template("adminusers.html")

# ==================== Employee Pages =====================
@routes.route('/pos')
def point_of_sale():
    return send_from_directory('pos', 'pos.html')

@routes.route('/inventory')
def pos_inventory():
    return send_from_directory('pos', 'inventory.html')

@routes.route('/invoice')
def pos_invoice():
    return send_from_directory('pos', 'invoice.html')

@routes.route('/returns')
def pos_returns():
    return send_from_directory('pos', 'returns.html')

@routes.route('/logout')
def logout():
    return redirect('/')

@routes.route('/payment')
def payment():
    return send_from_directory('payment', 'index.html')

# ==================== Static File Routes =====================
@routes.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('css', filename)

@routes.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory('js', filename)

@routes.route('/pictures/<path:filename>')
def send_pictures(filename):
    return send_from_directory('pictures', filename)

@routes.route('/<filename>.js')
def serve_js_file(filename):
    return send_from_directory('pos', f'{filename}.js')

@routes.route('/<filename>.css')
def serve_css_file(filename):
    return send_from_directory('pos', f'{filename}.css')

@routes.route('/pictures/pos/<path:filename>')
def serve_images(filename):
    return send_from_directory('pos/Picture', filename)

@routes.route('/payment/<path:filename>.css')
def serve_payment_css(filename):
    return send_from_directory('payment', f'{filename}.css')

@routes.route('/payment/<path:filename>.js')
def serve_payment_js(filename):
    return send_from_directory('payment', f'{filename}.js')

# ==================== Extra Pages =====================
@routes.route('/customer-pattern')
def customer_pattern():
    return render_template('customerpurchase.html')

@routes.route('/seasonal-demand')
def seasonal_demand():
    return render_template('forecast.html')

@routes.route('/restocking')
def restocking():
    return render_template('Restockprediction.html')

@routes.route('/smart-recommendation')
def smart_recommendation():
    return render_template('SmartRecommendation.html')

@routes.route('/owner-approvals')
def owner_approvals():
    return render_template('owner-approvals.html')

@routes.route('/admin-approvals')
def admin_approvals():
    return render_template('admin-approvals.html')

@routes.route('/profit-margin')
def profit_margin():
    return render_template('ownerdashboard.html')
