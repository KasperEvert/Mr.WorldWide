function updateMenu() {
    document.getElementById("menu").innerHTML = "";
    let menu_html = "<table><tbody>\n";
    let isNewCol = true;
    let menu_items_use = [];
    if (hasDarkmode) {
        menu_items_use = menu_items_darkmode;
    }
    else {
        menu_items_use = menu_items; // menu_items is from navbar.js
    }
    for (var i = 0; i < menu_items_use.length; i++) {
      if (isNewCol) {
        menu_html += "<tr><td>";
      }
      else {
          menu_html += "<td>"
      }
      menu_html += `${menu_items_use[i]}</td> \n`;
      if (!isNewCol) {
        menu_html += "</tr>\n";
      }
      isNewCol = !isNewCol;
    }
    if (!isNewCol) {
      menu_html += "<td></td></tr>\n";
    }
    menu_html += "</tbody></table>";
    document.getElementById("menu").innerHTML = menu_html;
}
document.addEventListener('DOMContentLoaded', function() {
    updateMenu();
});
