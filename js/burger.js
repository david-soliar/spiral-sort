function hamburger_toggle(h) {
    h.classList.toggle("lines-change");
    var top = document.getElementById("top-navigation");
    console.log(top)
    if (top.style.display === "grid"){
        top.style.display = "none";
    }
    else {
        top.style.display = "grid";
    }
}