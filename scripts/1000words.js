///
/// Source: https://stackoverflow.com/a/5767357
///
function removeItemOnce(arr, value) {
  var index = arr.indexOf(value);
  if (index > -1) {
    arr.splice(index, 1);
  }
  return arr;
}

function removeItemAll(arr, value) {
  var i = 0;
  while (i < arr.length) {
    if (arr[i] === value) {
      arr.splice(i, 1);
    } else {
      ++i;
    }
  }
  return arr;
}
///
/// </>
///

function getNewWords(qNum = 0) {
    let word = "";
    let trans = "";
    let fake1 = "";
    let fake2 = "";
    let fake3 = "";
    let langTag = document.getElementById("LANGTAG").innerHTML;
    let r=1;
    if (qNum === 0) {r=Math.floor(Math.random()*(Object.keys(words).length));}
    else {r=--qNum;}
    let x = 0;
    for(var key in words) {
        if (x == r) {
            word = words[key].word;
            trans = words[key].trans;
            fake1 = words[key].fake1;
            fake2 = words[key].fake2;
            fake3 = words[key].fake3;

            break;
        }
        x += 1;
    }
    let opt1 = [`<a id="fake1" class="waves-effect waves-light btn wordGuessBtn" onclick="wrong()">${fake1}</a>`,
        `<a id="fake2" class="waves-effect waves-light btn wordGuessBtn" onclick="wrong()">${fake2}</a>`,
        `<a id="fake3" class="waves-effect waves-light btn wordGuessBtn" onclick="wrong()">${fake3}</a>`,
        `<a id="trans" class="waves-effect waves-light btn wordGuessBtn" onclick="right()">${trans}</a>`];
    let options = "";
    x=0;
    while (true) {
        if (opt1.length == 0)
            break;
        let r = Math.floor(Math.random() * (opt1.length));
        if (x == 100)
            options += opt1[r] + "<br><br>";
        else
            options += opt1[r];
        removeItemOnce(opt1, opt1[r]);
        x+=1;
    }

    document.getElementById("wordGuess").innerHTML = `
        <h4>Your word:<br>"<${langTag}>${word}</${langTag}>".<br><br></h4>
        <center><div id="wordResult"></div><br>${options}</center>`;
}
function wrong() {
    if (document.getElementById("wordResult").innerHTML != "<b>Correct!</b>")
        document.getElementById("wordResult").innerHTML = "<b>Wrong!</b>";
}
function right() {
    document.getElementById("wordResult").innerHTML = "<b>Correct!</b>";
    document.getElementById("fake1").classList.add('red');
    document.getElementById("fake2").classList.add('red');
    document.getElementById("fake3").classList.add('red');
    document.getElementById("fake1").classList.add('darken-4');
    document.getElementById("fake2").classList.add('darken-4');
    document.getElementById("fake3").classList.add('darken-4');
}
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("SiteContent").innerHTML = `<center><a class="waves-effect waves-light btn" style="font-size: 32px;" onclick="getNewWords()">
        Guess a new word</a></center>
    <div id="wordGuess"></div>`;
    getNewWords();
});
