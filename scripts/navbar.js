const menu_items = [
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Hebrew/">Hebrew <emo>🇮🇱</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Greek/">Greek <emo>🇬🇷🇨🇾</emo> </a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Arabic/">Arabic <emo>🇸🇦</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Syriac/">Syriac <emo>🇸🇾</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Aramaic/">Aramaic <emo>🇮🇶</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Mandaic/">Mandaic <emo>🇮🇷🇮🇶</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Coptic/">Coptic <emo>🇪🇬</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Russian/">Russian <emo>🇷🇺</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Bulgarian/">Bulgarian <emo>🇧🇬</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Korean/">Korean <emo>🇰🇵🇰🇷</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Chinese/">Chinese <emo>🇨🇳</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Latin/">Latin <emo>🇻🇦</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Armenian/">Armenian <emo>🇦🇲</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Georgian/">Georgian <emo>🇬🇪</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Geez/">Ge\'ez <emo>🇪🇹🇪🇷</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Nabataean/">Nabataean <emo>🇯🇴</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Persian/">Persian <emo>🇹🇯🇮🇷🇦🇫</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Jamtish/">Jamtish <emo>🇳🇴🇸🇪</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Japanese/">Japanese <emo>🇯🇵</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Icelandic/">Icelandic <emo>🇮🇸</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Faroese/">Faroese <emo>🇫🇴</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Czech/">Czech <emo>🇨🇿</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Turkish/">Turkish <emo>🇹🇷</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Sanskrit/">Sanskrit <emo>🇮🇳</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Avestan/">Avestan <emo>🇮🇷</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Hungarian/">Hungarian <emo>🇭🇺</emo></a>',
'<a class="waves-effect menu-item" href="https://KasperEvert.github.io/Mr.WorldWide/lang/Polish/">Polish <emo>🇵🇱</emo></a>'];
let menu_items_darkmode = [];
for (let i = 0; i < menu_items.length; i++) { menu_items_darkmode.push(menu_items[i].replaceAll('/">', '/?darkmode=true">')) }
const LANGNAME = document.getElementById("LANGNAME").innerHTML;
let hasDarkmode = false;

if (window.location.href.includes("?")) {
    let args = window.location.href.split("?");
    for (let i = 0; i < args.length; i++) {
        if (args[i] == "darkmode=true") {
            hasDarkmode = true; /* It can be good to have the args be
                        checked before content loads in some senarios,
                        but here we need to send it to DOMContentLoaded.*/
        }
    }
}

function nightmode() {
    if (document.getElementById("nightmode").innerHTML == "") {
        hasDarkmode = true;
        document.getElementById("nightmode").innerHTML = `
        <style>
            body {
                background-color: #212121;
                color: white;
            }
            .sidenav {
                background-color: #262626;
            }
            .sidenav li > a {
                color: white !important;
            }
            textarea {
                color: white !important;
            }
            .collection-item {
                background-color: #212121 !important;
            }
            #menu a {
                color: white !important;
            }
            .invert_on_nightmode {
              filter: invert(1);
            }
        </style>
        `
    }
    else {
        hasDarkmode = false;
        document.getElementById("nightmode").innerHTML = "";
    }
    if (LANGNAME == "Home page") { updateMenu(); }
    if (document.getElementById("langOptions")) {
            if (hasDarkmode) {
                let reconstructed = "";
                let current = document.getElementById("langOptions").innerHTML.split("\n");
                for (let i = 0; i < current.length; i++) { current[i] = current[i].trim() }

                for (let i = 0; i < current.length; i++) {
                    if (current[i].includes("KasperEvert.github.io/Mr.WorldWide")) {
                        reconstructed += current[i].replaceAll('/" class="',
                            '/?darkmode=true" class="').replaceAll('.html" class="collection-',
                            '.html?darkmode=true" class="collection-') + "\n";
                    }
                    else {
                        reconstructed += current[i] + "\n";
                    }
                }
                document.getElementById("langOptions").innerHTML = reconstructed;
            }
            else {
                document.getElementById("langOptions").innerHTML =
                    document.getElementById("langOptions").innerHTML.replaceAll("?darkmode=true", "");
            }
    }
    if (hasDarkmode) {
        if (document.getElementById("1kbtn_area")) {
            document.getElementById("1kbtn_area").innerHTML =
                document.getElementById("1kbtn_area").innerHTML.replaceAll("1000words.html", "1000words.html?darkmode=true");
        }
    }
    else {
        if (document.getElementById("1kbtn_area")) {
            document.getElementById("1kbtn_area").innerHTML =
                document.getElementById("1kbtn_area").innerHTML.replaceAll("1000words.html?darkmode=true", "1000words.html");
        }
    }
    updateNavbar();
}

function updateNavbar() {
    let menu_items_use = [];
    if (hasDarkmode) {
        menu_items_use = menu_items_darkmode;
    }
    else {
        menu_items_use = menu_items;
    }
    var slide =  `
    <nav>
      <div class="nav-wrapper">
        <ul id="nav-mobile" class="left">
          <li><a href="#" data-target="slide-out" class="sidenav-trigger show-on-large">
            <i class="material-icons">menu</i>
          </a></li>
        </ul>
        <ul id="nav-mobile" class="center">
          <li>Mr. WorldWide, ${LANGNAME}</li>
        </ul>
      </div>
    </nav>
    <ul id="slide-out" class="sidenav">
      <li><a class="subheader">Mr. WorldWide </a></li>
      <li><div class="divider"></div></li>`;
    for (var i = 0; i < menu_items_use.length; i++) {
      slide += `<li>${menu_items_use[i]}<br></li>\n`;
    }
    if (hasDarkmode) {
        slide += `
          <li><a class="waves-effect" href="https://KasperEvert.github.io/Mr.WorldWide/?darkmode=true">Home page</a><br></li>
          <li><a class="waves-effect sidenav-close" href="javascript:nightmode()">Toggle Nightmode <emo>🌙</emo></a><br></li>
        </ul>`;
    }
    else {
        slide += `
          <li><a class="waves-effect" href="https://KasperEvert.github.io/Mr.WorldWide/">Home page</a><br></li>
          <li><a class="waves-effect sidenav-close" href="javascript:nightmode()">Toggle Nightmode <emo>🌙</emo></a><br></li>
        </ul>`;
    }

    document.getElementById("mainHead").innerHTML = slide;
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
}

document.addEventListener('DOMContentLoaded', function() {
    if (hasDarkmode == true) {
        nightmode();
    }
    else {
        updateNavbar();
    }
});
