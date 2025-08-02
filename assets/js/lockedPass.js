searchParams = new URLSearchParams(window.location.search)
urlPass = searchParams.get("pass")
pagePass = {{% page.pass %}}
locked = {{% page.locked %}}
if (locked && urlPass != pagePass) {
    window.location.replace("morbidswan.site/locked/")
}