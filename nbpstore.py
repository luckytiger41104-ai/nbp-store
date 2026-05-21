import json
from flask import Flask

app = Flask(__name__)

# 1. आपके स्टोर के सभी 48 प्रोडक्ट्स की पूरी लिस्ट
PRODUCTS = [
    {"id": 1, "name": "Aata (Wheat Flour)", "unit": "1kg", "price": 40, "cat": "grocery"},
    {"id": 2, "name": "Chawal (Rice)", "unit": "1kg", "price": 45, "cat": "grocery"},
    {"id": 3, "name": "Dal Chana", "unit": "1kg", "price": 100, "cat": "grocery"},
    {"id": 4, "name": "Dal Mashur", "unit": "1kg", "price": 80, "cat": "grocery"},
    {"id": 5, "name": "Dal Arhar (Toor)", "unit": "1kg", "price": 130, "cat": "grocery"},
    {"id": 6, "name": "Sarso Tel (Oil)", "unit": "1L", "price": 185, "cat": "grocery"},
    {"id": 7, "name": "Namak (Salt)", "unit": "1kg", "price": 10, "cat": "grocery"},

    {"id": 8, "name": "Cheeni (Sugar)", "unit": "1kg", "price": 50, "cat": "grocery"},
    {"id": 9, "name": "Maida", "unit": "1kg", "price": 40, "cat": "grocery"},
    {"id": 10, "name": "Besan", "unit": "1kg", "price": 120, "cat": "grocery"},
    {"id": 11, "name": "Sooji (Semolina)", "unit": "1kg", "price": 50, "cat": "grocery"},
    {"id": 12, "name": "Poha (chura)", "unit": "500g", "price": 20, "cat": "grocery"},
    {"id": 13, "name": "Rai (Mustard Seeds)", "unit": "100g", "price": 15, "cat": "grocery"},
    {"id": 14, "name": "Jeera (Cumin)", "unit": "100g", "price": 70, "cat": "grocery"},
    {"id": 15, "name": "Lal Mirch Powder", "unit": "100g", "price": 30, "cat": "grocery"},
    {"id": 16, "name": "Haldi Powder", "unit": "100g", "price": 25, "cat": "grocery"},
    {"id": 17, "name": "Dhaniya Powder", "unit": "100g", "price": 25, "cat": "grocery"},
    {"id": 18, "name": "Garam Masala", "unit": "50g", "price": 30, "cat": "grocery"},
    {"id": 19, "name": "Chai Patti dalmia (Tea)", "unit": "50g", "price": 25, "cat": "grocery"},
    {"id": 20, "name": "Maggi Noodles", "unit": "4pk", "price": 40, "cat": "grocery"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 30, "cat": "puja"},
    {"id": 22, "name": "Dhoop Batti", "unit": "Pack", "price": 20, "cat": "puja"},
    {"id": 23, "name": "gulal", "unit": "Pack", "price": 10, "cat": "puja"},
    {"id": 24, "name": "Camphor (Kapoor)", "unit": "1Pack", "price": 70, "cat": "puja"},
    {"id": 25, "name": "Haldi Pooja", "unit": "50", "price": 10, "cat": "puja"},
    {"id": 26, "name": "Sindoor", "unit": "Pack", "price": 5, "cat": "puja"},
    {"id": 27, "name": "Roli", "unit": "Pack", "price": 15, "cat": "puja"},
    {"id": 28, "name": "astgandh chandan", "unit": "1Pack", "price": 20, "cat": "puja"},
    {"id": 29, "name": "Gangajal", "unit": "Bottle", "price": 30, "cat": "puja"},
    {"id": 30, "name": "Pooja Thali", "unit": "1pc", "price": 150, "cat": "puja"},
    {"id": 31, "name": "butter Biscuit", "unit": "10pk", "price": 50, "cat": "snacks"},
    {"id": 32, "name": "Marie Biscuit", "unit": "Pack", "price": 40, "cat": "snacks"},
    {"id": 33, "name": "Namkeen", "unit": "200g", "price": 30, "cat": "snacks"},
    {"id": 34, "name": "Chips (Lays)", "unit": "1Pack", "price": 5, "cat": "snacks"},
    {"id": 35, "name": "Toffee (Mango Bite)", "unit": "10pc", "price": 10, "cat": "snacks"},
    {"id": 36, "name": "Kurkure", "unit": "1Pack", "price": 5, "cat": "snacks"},
    {"id": 37, "name": "Sabun detol (Soap)", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 38, "name": "Shampoo dove", "unit": "10pc", "price": 20, "cat": "personal"},
    {"id": 39, "name": "Toothpaste", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 40, "name": "Toothbrush", "unit": "1pc", "price": 30, "cat": "personal"},
    {"id": 41, "name": "Surf Excel", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 42, "name": "guide surf ", "unit": "500gram", "price": 40, "cat": "personal"},
    {"id": 43, "name": "Matchbox", "unit": "1pk", "price": 10, "cat": "other"},
    {"id": 44, "name": "Candle (Mombatti)", "unit": "Pack", "price": 40, "cat": "other"},
    {"id": 45, "name": "Pen", "unit": "5pc", "price": 25, "cat": "other"},
    {"id": 46, "name": "Notebook Hindi (Copy)", "unit": "1pc", "price": 30, "cat": "other"},
    {"id": 47, "name": "Safety Pin", "unit": "Pack", "price": 10, "cat": "other"},
    {"id": 48, "name": "Rubber Band", "unit": "Pack", "price": 10, "cat": "other"},
    {"id": 49, "name": "Tata namak", "unit": "1kg", "price": 30, "cat": "grocery"},
    {"id": 50, "name": "Notebook Hindi(Copy)", "unit": "1pc", "price": 10, "cat": "other"},
    {"id": 51, "name": "Notebook Hindi(Copy)", "unit": "1pc", "price": 20, "cat": "other"},
    {"id": 52, "name": "Notebook White (Copy)", "unit": "1pc", "price": 30, "cat": "other"},
    {"id": 53, "name": "Notebook White (Copy)", "unit": "1pc", "price": 20, "cat": "other"},
    {"id": 54, "name": "Notebook white(Copy)", "unit": "1pc", "price": 10, "cat": "other"},
    {"id": 55, "name": "Toothbrush", "unit": "1pc", "price": 20, "cat": "personal"},
    {"id": 56, "name": "Toothbrush", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 57, "name": "Toothpaste", "unit": "1pc", "price": 20, "cat": "personal"},
    {"id": 58, "name": "Shampoo clinic plus", "unit": "10pc", "price": 10, "cat": "personal"},
    {"id": 59, "name": "Shampoo sun silk", "unit": "10pc", "price": 10, "cat": "personal"},
    {"id": 60, "name": "Sabun lifebuoy(Soap)", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 61, "name": "Sabun lux (Soap)", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 62, "name": "Agarbatti", "unit": "1Pack", "price": 65, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 20, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 50, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 15, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 50, "cat": "puja"},

]
# 2. आपका वेबपेज डिज़ाइन (HTML/CSS/JS)
HTML = """<!DOCTYPE html>
<html lang='hi'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>NBP General Store and Puja Bhandar</title>
<link href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap' rel='stylesheet'>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Poppins,sans-serif;background:#FFF8F0;color:#1a1a1a}
header{background:linear-gradient(135deg,#FF6B00,#C0392B);position:sticky;top:0;z-index:100;box-shadow:0 3px 15px rgba(0,0,0,.3)}
.hi{display:flex;align-items:center;justify-content:space-between;padding:10px 14px}
.logo{width:44px;height:44px;background:#FFB300;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0;color:#1a1a1a}
.sn{flex:1;margin-left:10px}
.sn h1{font-size:13px;font-weight:700;color:#fff}
.sn p{font-size:11px;color:rgba(255,255,255,.85)}
.cartbtn{background:#FFB300;border:none;border-radius:20px;padding:8px 14px;font-weight:700;font-size:13px;cursor:pointer;display:flex;align-items:center;gap:6px;font-family:Poppins,sans-serif}
.cn{background:#C0392B;color:#fff;border-radius:50%;width:20px;height:20px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700}
.bn{background:#FFB300;padding:7px 14px;text-align:center;font-size:11px;font-weight:600;border-bottom:2px dashed #FF6B00}
.search-box{padding:10px 14px;background:#fff;border-bottom:1px solid #eee}
.search-box input{width:100%;padding:9px 14px;border:2px solid #FF6B00;border-radius:25px;font-size:13px;font-family:Poppins,sans-serif;outline:none}
.cats{display:flex;gap:8px;padding:10px 14px;overflow-x:auto;scrollbar-width:none;background:#fff;border-bottom:1px solid #eee}
.cats::-webkit-scrollbar{display:none}
.ct{flex-shrink:0;padding:6px 14px;border-radius:20px;border:2px solid #FF6B00;background:#fff;color:#FF6B00;font-size:12px;font-weight:600;cursor:pointer;font-family:Poppins,sans-serif}
.ct.on,.ct:hover{background:#FF6B00;color:#fff}
.st{padding:14px 14px 8px;font-size:16px;font-weight:700;color:#C0392B}
.pg{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:0 10px 80px}
.pc{background:#fff;border-radius:12px;padding:12px;box-shadow:0 2px 8px rgba(0,0,0,.08);border-top:3px solid #FF6B00}
.ptag{display:inline-block;background:#fff3e0;color:#FF6B00;font-size:9px;font-weight:700;padding:2px 8px;border-radius:10px;margin-bottom:6px;text-transform:uppercase}
.pn{font-size:12px;font-weight:700;margin-bottom:2px;color:#1a1a1a}
.pu{font-size:11px;color:#999;margin-bottom:5px}
.pp{font-size:15px;font-weight:700;color:#FF6B00;margin-bottom:8px}
.ab{width:100%;background:linear-gradient(135deg,#FF6B00,#C0392B);color:#fff;border:none;border-radius:8px;padding:8px;font-size:12px;font-weight:600;cursor:pointer;font-family:Poppins,sans-serif}
.qc{display:flex;align-items:center;justify-content:space-between;background:#fff3e0;border-radius:8px;padding:3px}
.qb{width:30px;height:30px;background:#FF6B00;color:#fff;border:none;border-radius:6px;font-size:20px;font-weight:700;cursor:pointer;line-height:1;font-family:Poppins,sans-serif}
.qnum{font-size:15px;font-weight:700}
.no-results{padding:30px;text-align:center;color:#aaa;font-size:14px;grid-column:span 2}
.ov{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:200}
.ov.on{display:block}
.cp{position:fixed;bottom:0;left:0;right:0;background:#fff;border-radius:20px 20px 0 0;max-height:90vh;overflow-y:auto;z-index:201;transform:translateY(100%);transition:transform .3s;padding-bottom:30px}
.cp.on{transform:translateY(0)}
.ch{background:linear-gradient(135deg,#FF6B00,#C0392B);color:#fff;padding:15px 18px;border-radius:20px 20px 0 0;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:5}
.ch h2{font-size:16px;font-weight:700}
.xb{background:rgba(255,255,255,.25);border:none;border-radius:50%;width:32px;height:32px;color:#fff;font-size:18px;cursor:pointer;font-family:Poppins,sans-serif}
.ci{padding:10px 14px}
.cit{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #f5f0e8}
.cf{flex:1}
.cfn{font-size:13px;font-weight:600}
.cfp{font-size:13px;color:#FF6B00;font-weight:700}
.rb{background:#ffebee;border:none;border-radius:6px;padding:6px 10px;color:#C0392B;cursor:pointer;font-size:13px;font-family:Poppins,sans-serif}
.cs{margin:4px 14px 14px;background:#fff8f0;border-radius:10px;padding:12px;border:1px dashed #FFB300}
.sr{display:flex;justify-content:space-between;padding:4px 0;font-size:13px}
.sr.tot{font-weight:700;font-size:15px;color:#C0392B;border-top:1px solid #ddd;padding-top:10px;margin-top:6px}
.of{padding:0 14px}
.of h3{font-size:14px;font-weight:700;margin-bottom:10px}
.fg{margin-bottom:10px}
.fg label{font-size:11px;font-weight:600;color:#555;display:block;margin-bottom:3px}
.fg input,.fg select{width:100%;padding:9px 12px;border:1.5px solid #ddd;border-radius:8px;font-size:14px;font-family:Poppins,sans-serif;background:#fff;outline:none}
.fg input:focus,.fg select:focus{border-color:#FF6B00}
.dn{background:#e8f5e9;border-radius:8px;padding:9px;font-size:11px;color:#1B5E20;font-weight:500;margin-bottom:12px}
.wb{width:100%;background:#25D366;color:#fff;border:none;border-radius:12px;padding:14px;font-size:15px;font-weight:700;cursor:pointer;font-family:Poppins,sans-serif}
.empty{text-align:center;padding:40px 20px;color:#bbb;font-size:14px}
footer{background:#1a1a1a;color:#fff;text-align:center;padding:20px;font-size:12px}
footer p{opacity:.7;margin:4px 0}
footer strong{color:#FFB300}
</style>
</head>
<body>

<header>
  <div class='hi'>
    <div class='logo'>NBP</div>
    <div class='sn'>
      <h1>NBP General Store &amp; Puja Bhandar</h1>
      <p>Dhamna, Jamui, Bihar | Ph: 7667984349</p>
    </div>
    <button class='cartbtn' onclick='openCart()'>Cart <span class='cn' id='cc'>0</span></button>
  </div>
  <div class='bn'>15 rupees Delivery: Pandey Tola | Pandit Tola | Bhumihar Tola | Goswami Tola</div>
</header>

<div class='search-box'>
  <input type='text' id='searchInput' placeholder='Product khojein... (e.g. Aata, Dal, Soap)' oninput='doSearch(this.value)'>
</div>

<div class='cats'>
  <button class='ct on' onclick='filt("all",this)'>Sab Products</button>
  <button class='ct' onclick='filt("grocery",this)'>Grocery</button>
  <button class='ct' onclick='filt("puja",this)'>Puja Samagri</button>
  <button class='ct' onclick='filt("snacks",this)'>Snacks</button>
  <button class='ct' onclick='filt("personal",this)'>Personal Care</button>
  <button class='ct' onclick='filt("other",this)'>Anya (Other)</button>
</div>

<div class='st' id='stitle'>Hamare Products</div>
<div class='pg' id='pg'></div>

<footer>
  <p><strong>NBP General Store &amp; Puja Bhandar</strong></p>
  <p>Dhamna, Jamui, Bihar</p>
  <p>Phone: 7667984349</p>
  <p>Home Delivery Available</p>
</footer>

<div class='ov' id='ov' onclick='closeCart()'></div>
<div class='cp' id='cp'>
  <div class='ch'>
    <h2>Aapka Cart</h2>
    <button class='xb' onclick='closeCart()'>X</button>
  </div>
  <div id='cb'></div>
</div>

<script>
var WA = "917667984349";
var PR = PRODUCTS_JSON;
var cart = {};
var curCat = "all";
var searchTerm = "";

var catNames = {
  "grocery": "Grocery",
  "puja": "Puja Samagri",
  "snacks": "Snacks",
  "personal": "Personal Care",
  "other": "Anya (Other)"
};

function renderP() {
  var g = document.getElementById("pg");
  var list = PR;
  if (searchTerm) {
    list = PR.filter(function(p){ return p.name.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1; });
  } else if (curCat !== "all") {
    list = PR.filter(function(p){ return p.cat === curCat; });
  }
  if (list.length === 0) {
    g.innerHTML = "<div class='no-results'>Koi product nahi mila.</div>";
    return;
  }
  g.innerHTML = list.map(function(p) {
    var q = cart[p.id] ? cart[p.id].qty : 0;
    var tag = catNames[p.cat] || p.cat;
    var btn = q === 0
      ? "<button class='ab' onclick='add("+p.id+")'>+ Cart mein Daalo</button>"
      : "<div class='qc'><button class='qb' onclick='dec("+p.id+")'>-</button><span class='qnum'>"+q+"</span><button class='qb' onclick='add("+p.id+")'>+</button></div>";
    return "<div class='pc'>"
      +"<div class='ptag'>"+tag+"</div>"
      +"<div class='pn'>"+p.name+"</div>"
      +"<div class='pu'>"+p.unit+"</div>"
      +"<div class='pp'>Rs. "+p.price+"</div>"
      +btn+"</div>";
  }).join("");
}

function doSearch(val) {
  searchTerm = val;
  if (val) {
    document.getElementById("stitle").textContent = "Search: " + val;
    document.querySelectorAll(".ct").forEach(function(b){ b.classList.remove("on"); });
  } else {
    document.getElementById("stitle").textContent = "Hamare Products";
  }
  renderP();
}

function filt(c, el) {
  curCat = c;
  searchTerm = "";
  document.getElementById("searchInput").value = "";
  document.getElementById("stitle").textContent = c === "all" ? "Hamare Products" : catNames[c] || c;
  document.querySelectorAll(".ct").forEach(function(b){ b.classList.remove("on"); });
  el.classList.add("on");
  renderP();
}

function fp(id){ for(var i=0;i<PR.length;i++) if(PR[i].id===id) return PR[i]; }

function add(id){
  var p = fp(id);
  if(!cart[id]) cart[id] = {id:p.id, name:p.name, price:p.price, qty:0};
  cart[id].qty++;
  upC(); renderP();
}

function dec(id){
  if(!cart[id]) return;
  cart[id].qty--;
  if(cart[id].qty <= 0) delete cart[id];
  upC(); renderP();
}

function rem(id){ delete cart[id]; upC(); renderP(); renderC(); }

function upC(){
  var t = 0;
  Object.keys(cart).forEach(function(k){ t += cart[k].qty; });
  document.getElementById("cc").textContent = t;
}

function openCart(){
  document.getElementById("ov").classList.add("on");
  document.getElementById("cp").classList.add("on");
  renderC();
}

function closeCart(){
  document.getElementById("ov").classList.remove("on");
  document.getElementById("cp").classList.remove("on");
}

function renderC(){
  var box = document.getElementById("cb");
  var items = Object.keys(cart).map(function(k){ return cart[k]; });
  if(items.length === 0){
    box.innerHTML = "<div class='empty'><p>Cart khali hai!<br>Kuch products add karein.</p></div>";
    return;
  }
  
  var sub = items.reduce(function(s,i){ return s + i.price * i.qty; }, 0);
  var totalItems = items.reduce(function(s,i){ return s + i.qty; }, 0);
  
  var delCharge = 15;
  if (totalItems >= 11 && totalItems <= 19) {
    delCharge = 25;
  } else if (totalItems >= 20) {
    delCharge = 30;
  }
  
  var isPickup = (document.getElementById("ar") && document.getElementById("ar").value === "Shop Pickup");
  if(isPickup) {
    delCharge = 0;
  }

  var finalTotal = sub + delCharge;
  var advanceAmount = Math.round(finalTotal / 2);

  var rows = items.map(function(i){
    return "<div class='cit'>"
      +"<div class='cf'><div class='cfn'>"+i.name+" x "+i.qty+"</div>"
      +"<div class='cfp'>Rs. "+(i.price*i.qty)+"</div></div>"
      +"<button class='rb' onclick='rem("+i.id+")'>Hatao</button></div>";
  }).join("");
  
  var ao = ["Pandey Tola","Pandit Tola","Bhumihar Tola","Goswami Tola","Shop Pickup"]
    .map(function(a){ return "<option>"+a+"</option>"; }).join("");
    
  var advanceHTML = isPickup 
    ? "<div class='sr' style='color:#C0392B; font-weight:700;'><span>Advance (50% Online)</span><span>Rs. "+advanceAmount+"</span></div>"
      +"<div class='sr' style='color:#1B5E20; font-weight:600;'><span>Baki Paisa (Dukan par)</span><span>Rs. "+(finalTotal - advanceAmount)+"</span></div>"
    : "";

  box.innerHTML = "<div class='ci'>"+rows+"</div>"
    +"<div class='cs'>"
    +"<div class='sr'><span>Subtotal ("+totalItems+" items)</span><span>Rs. "+sub+"</span></div>"
    +"<div class='sr'><span>Delivery Charge</span><span id='delText'>Rs. "+delCharge+"</span></div>"
    +"<div class='sr tot'><span>Total Bill</span><span id='totText'>Rs. "+finalTotal+"</span></div>"
    +"<div id='advBox'>"+advanceHTML+"</div>"
    +"</div>"
    +"<div class='of'><h3>Delivery Details</h3>"
    +"<div class='fg'><label>Aapka Naam</label><input type='text' id='nm' placeholder='Naam likhein'></div>"
    +"<div class='fg'><label>Phone Number</label><input type='tel' id='ph' placeholder='10 digit number'></div>"
    +"<div class='fg'><label>Delivery Area</label><select id='ar' onchange='updateDel()'><option value=''>-- Area chunein --</option>"+ao+"</select></div>"
    +"<div class='dn' id='noticeText'>Delivery Charge: 1-10 items = Rs.15 | 11-19 items = Rs.25 | 20+ items = Rs.30 (Shop Pickup is FREE)</div>"
    +"<button class='wb' onclick='sendWA()'>WhatsApp pe Order Bhejo</button>"
    +"</div>";
}
