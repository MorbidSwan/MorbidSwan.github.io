searchParams = new URLSearchParams(window.location.search);
urlPass = searchParams.get("pass");
pagePass = document.getElementById("pagePass").content;
locked = document.getElementById("pagePass").content;
if (locked && urlPass != pagePass) {
    window.location.replace("morbidswan.site/locked/");
}